"""
This file stores functions that are responsible for communication between the application and MetaTrader 5.
In addition, other functions of the application's calculation logic are also called here.
"""

import os
from datetime import datetime, timedelta, timezone

from typing import Any, Tuple
import MetaTrader5 as mt5
import pandas as pd

import src.backend.calc_strategies_methods as calculate_strategies_methods
import src.backend.chart_methods as chart_methods
import src.backend.bsh_history as bsh_history


# log in into MetaTrader5
def log_in(login: int, password: str, server: str) -> bool:
    """
    This function is responsible for logging into MetaTrader 5 account.
    :param login: login.
    :param password: password.
    :param server: server.
    :return: boolean.
    """
    mt5.initialize()
    return mt5.login(login, password, server)


def get_account_info() -> Any:
    """
    This function fetches data about account from MetaTrader 5.
    :return: data.
    """
    account_info = mt5.account_info()
    if account_info is None:
        return None
    return account_info._asdict()


def get_account_symbols() -> Any:
    """
    This function is responsible for fetching symbols data from MetaTrader 5.
    :return: data.
    """
    symbols = mt5.symbols_get()
    if not symbols:
        return None

    forex = set()
    stocks = set()
    etfs = set()
    visible_symbols = set(symbol.name for symbol in symbols if symbol.visible)

    for symbol in visible_symbols:
        info = mt5.symbol_info(symbol)
        if not info:
            continue

        market_path = info.path.lower()

        if "sp500" in symbol.lower():
            etfs.add(symbol)
        elif "forex" in market_path or "fx" in market_path:
            forex.add(symbol)
        elif "etf" in market_path or "funds" in market_path:
            etfs.add(symbol)
        else:
            stocks.add(symbol)

    return {"forex": forex, "stock": stocks, "etf": etfs}


def get_account_open_positions() -> pd.DataFrame:
    """
    This function is responsible for fetching opened positions from MetaTrader 5.
    :return: data.
    """
    positions = mt5.positions_get()

    if positions is None or len(positions) == 0:
        return None

    positions_dict = [position._asdict() for position in positions]
    positions_df = pd.DataFrame(positions_dict, columns=positions[0]._asdict().keys())
    return positions_df


def download_data(
    symbol: str, days: int, time_frame: int, time_backward: int
) -> pd.DataFrame:
    """
    This function is used to download historical stock market data from the MetaTrader 5 application.
    :param symbol: symbol of selected shares
    :param days: number of days
    :param time_frame: determines the time frame
    :param time_backward: specifies the number of days back
    :return: open high low close stock market data
    """
    start: datetime = (
        datetime.now(timezone.utc)
        - timedelta(days=days)
        - timedelta(days=time_backward)
    )
    end: datetime = (
        datetime.now(timezone.utc) + timedelta(hours=2) - timedelta(days=time_backward)
    )
    ohlc_data: pd.DataFrame = pd.DataFrame(
        mt5.copy_rates_range(symbol, time_frame, start, end)
    )

    if ohlc_data.empty:
        print(f"No data for symbol: {symbol}.")
        return pd.DataFrame()

    ohlc_data["time"] = pd.to_datetime(ohlc_data["time"], unit="s", utc=True)
    ohlc_data["time"] = ohlc_data["time"].dt.tz_localize(None)
    return ohlc_data


def prepare_data(ohlc_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function is responsible for prepare data for calculations and display them.
    :param ohlc_data: raw data.
    :return: prepared data.
    """
    ohlc_data.rename(
        columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
        },
        inplace=True,
    )

    ohlc_data = ohlc_data.dropna(subset=["Open", "High", "Low", "Close"])
    ohlc_data.set_index("time", inplace=True)
    ohlc_data.reset_index(inplace=True)
    return ohlc_data


def log_out() -> None:
    """
    This function is responsible for log out from MetaTrader 5.
    :return: nothing.
    """
    mt5.shutdown()


def create_history_charts(days: int, data: pd.DataFrame) -> None:
    """
    This function is responsible for calculating history data.
    :param days: number of days.
    :param data: data.
    :return: nothing.
    """
    if days > 86:
        history_data_size = 80
    elif days > 7:
        history_data_size = days - 5
    else:
        history_data_size = days

    show_charts = False
    history_data, shape = bsh_history.calculate_history_data(data, history_data_size)

    if shape > 65:
        history_data = history_data[-60:]
        shape = 60

    bsh_history.create_linear_chart(history_data, shape, show_charts)
    bsh_history.create_all_linear_chart(history_data, shape, show_charts)
    bsh_history.create_histogram_chart(history_data, show_charts)


# main program loop
def run_calculations(
    symbol: str, days: int, time_frm: str, forex: bool, time_backward: int
) -> Tuple[bool, Any]:
    """
    This function is responsible for call all important backend functions which makes calculations on data.
    :param symbol: transaction symbol.
    :param days: number of days.
    :param time_frm: chosen time frame.
    :param forex: forex data.
    :param time_backward: number of backward days.
    :return: calculated data.
    """
    time_types = {
        "1 Min": mt5.TIMEFRAME_M1,
        "5 Min": mt5.TIMEFRAME_M5,
        "15 Min": mt5.TIMEFRAME_M15,
        "30 Min": mt5.TIMEFRAME_M30,
        "1 H": mt5.TIMEFRAME_H1,
        "3 H": mt5.TIMEFRAME_H3,
        "6 H": mt5.TIMEFRAME_H6,
        "12 H": mt5.TIMEFRAME_H12,
    }

    time_frame = time_types[time_frm]

    match time_frm:
        case "1 Min":
            time_break = 1
        case "5 Min":
            time_break = 2
        case "15 Min":
            time_break = 3
        case "30 Min":
            time_break = 4
        case "1 H":
            time_break = 5
        case "3 H":
            time_break = 6
        case "6 H":
            time_break = 7
        case _:
            time_break = 0

    if forex:
        time_break = 0

    data = download_data(
        symbol=symbol, days=days, time_frame=time_frame, time_backward=time_backward
    )

    if not data.empty:
        # prepare data for calculations and display
        prepare_data(ohlc_data=data)

        # calculate strategies
        strategies = calculate_strategies_methods.calculate_strategies(data=data)

        # calculate experts signals
        signals_buy, signals_sell, signals_hold = (
            calculate_strategies_methods.calculate_signals(
                data=data, strategies=strategies
            )
        )

        additive_sign, majority_sign, median_sign = (
            calculate_strategies_methods.interpret_strategies_result(
                signals_buy=signals_buy,
                signals_sell=signals_sell,
                signals_hold=signals_hold,
            )
        )

        # create chart
        file_path = os.path.abspath("src\\charts\\chart.html")
        chart_methods.create_html_chart(
            ohlc_data=data,
            file_path=file_path,
            name=symbol,
            strategies=strategies,
            time_breaks=time_break,
        )

        create_history_charts(days + time_backward, data)

        decisions = {
            "buy": signals_buy,
            "sell": signals_sell,
            "hold": signals_hold,
            "additive": additive_sign,
            "majority": majority_sign,
            "median": median_sign,
        }

        return True, decisions
    return False, 0
