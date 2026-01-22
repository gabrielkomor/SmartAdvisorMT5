from typing import Tuple, Dict
import pandas as pd
import numpy as np
import scripts.strategy_methods as strategy_methods
import scripts.strategy_functions as strategy_functions
import scripts.interpretation_methods as interpretation_methods


def calculate_strategies(data: pd.DataFrame) -> Dict:
    rsi = strategy_methods.calculate_rsi(data=data, period=14)
    sma_10, sma_10_data = strategy_methods.calculate_sma(data=data, period=10)
    sma_20, sma_20_data = strategy_methods.calculate_sma(data=data, period=20)
    sma_30, sma_30_data = strategy_methods.calculate_sma(data=data, period=30)
    macd_line, macd_signal_line, macd_hist = strategy_methods.calculate_macd(data=data)
    adx, adx_pdi, adx_ndi = strategy_methods.calculate_adx(data=data, period=10)
    # mma_short, mma_long = strategy_methods.calculate_mma(data=data)
    bb_upper, bb_lower, bb_std = strategy_methods.calculate_bollinger_bands(
        data=data, period=20
    )
    fibo_levels, levels = strategy_methods.calculate_fibonacci_levels(data=data)

    strategies = {
        "rsi": rsi,
        "sma_10": sma_10,
        "sma_10_data": sma_10_data,
        "sma_20": sma_20,
        "sma_20_data": sma_20_data,
        "sma_30": sma_30,
        "sma_30_data": sma_30_data,
        "macd_line": macd_line,
        "macd_signal_line": macd_signal_line,
        "macd_hist": macd_hist,
        "adx": adx,
        "adx_pdi": adx_pdi,
        "adx_ndi": adx_ndi,
        # 'mma_short': mma_short,
        # 'mma_long': mma_long,
        "bb_upper": bb_upper,
        "bb_lower": bb_lower,
        "bb_std": bb_std,
        "levels": levels,
        "fibo_lvl": fibo_levels,
    }
    return strategies


def display_strategies_data(strategies: Dict) -> None:
    print()
    print(f'Moving average 10 SMA: {strategies["sma_10"]}')
    print(f'Moving average 20 SMA: {strategies["sma_20"]}')
    print(f'Moving average 30 SMA: {strategies["sma_30"]}')
    print(f'RSI: {strategies["rsi"].iloc[-1]}')
    print(
        f'Bollinger Bands: {strategies["bb_upper"].iloc[-1]}, {strategies["bb_lower"].iloc[-1]}'
    )
    print(f'MACD: {strategies["macd_hist"]}')
    print(f'MMA: {strategies["mma_short"].iloc[-1]}, {strategies["mma_long"].iloc[-1]}')
    print(f'ADX: {strategies["adx"].iloc[-1]}')


def calculate_signals(data: pd.DataFrame, strategies: Dict) -> Tuple:
    signals_buy = np.zeros(7)
    signals_sell = np.zeros(7)
    signals_hold = np.zeros(7)

    strategy_functions.calculate_signals_sma(
        sma_n=strategies["sma_10"],
        sma_m=strategies["sma_30"],
        num=0,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    strategy_functions.calculate_signals_rsi(
        rsi=strategies["rsi"].iloc[-1],
        num=1,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    strategy_functions.calculate_signals_bollinger_bands(
        data=data,
        bb_up_line=strategies["bb_upper"].iloc[-1],
        bb_down_line=strategies["bb_lower"].iloc[-1],
        num=2,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    strategy_functions.calculate_signals_macd(
        hist=strategies["macd_hist"],
        num=3,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    # strategy_functions.calculate_signals_mma(
    #     short_ma=strategies['mma_short'],
    #     long_ma=strategies['mma_long'],
    #     num=4,
    #     signals_buy=signals_buy,
    #     signals_sell=signals_sell,
    #     signals_hold=signals_hold
    # )

    strategy_functions.calculate_signals_adx(
        adx=strategies["adx"],
        pdm=strategies["adx_pdi"],
        ndm=strategies["adx_ndi"],
        num=4,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    strategy_functions.calculate_signals_volume(
        data=data,
        num=5,
        signals_buy=signals_buy,
        signals_sell=signals_sell,
        signals_hold=signals_hold,
    )

    signals_buy[6] = signals_buy[5]
    signals_sell[6] = signals_sell[5]
    signals_hold[6] = signals_hold[5]

    return signals_buy, signals_sell, signals_hold


def display_strategies_results(
    signals_buy: np.array, signals_sell: np.array, signals_hold: np.array
) -> None:
    print()
    print(f'{"Strategy":<10} {"BUY":<10} {"SELL":<10} {"HOLD":<10}')
    print("-" * 40)
    print(
        f'{"SMA":<10} {signals_buy[0]:<10.5f} {signals_sell[0]:<10.5f} {signals_hold[0]:<10.5f}'
    )
    print(
        f'{"RSI":<10} {signals_buy[1]:<10.5f} {signals_sell[1]:<10.5f} {signals_hold[1]:<10.5f}'
    )
    print(
        f'{"BB":<10} {signals_buy[2]:<10.5f} {signals_sell[2]:<10.5f} {signals_hold[2]:<10.5f}'
    )
    print(
        f'{"MACD":<10} {signals_buy[3]:<10.5f} {signals_sell[3]:<10.5f} {signals_hold[3]:<10.5f}'
    )
    # print(f'{"MMA":<10} {signals_buy[4]:<10.5f} {signals_sell[4]:<10.5f} {signals_hold[4]:<10.5f}')
    print(
        f'{"ADX":<10} {signals_buy[5]:<10.5f} {signals_sell[5]:<10.5f} {signals_hold[5]:<10.5f}'
    )
    print(
        f'{"VOL":<10} {signals_buy[6]:<10.5f} {signals_sell[6]:<10.5f} {signals_hold[6]:<10.5f}'
    )
    print(
        f'{"VOL":<10} {signals_buy[7]:<10.5f} {signals_sell[7]:<10.5f} {signals_hold[7]:<10.5f}'
    )
    print()


def interpret_strategies_result(
    signals_buy: np.array, signals_sell: np.array, signals_hold: np.array
) -> (Tuple)[np.ndarray, np.ndarray, np.ndarray]:
    additive = interpretation_methods.additive_method(
        signals_buy, signals_sell, signals_hold
    )
    majority = interpretation_methods.majority_vote_method(
        signals_buy, signals_sell, signals_hold
    )
    median = interpretation_methods.median_method(
        signals_buy, signals_sell, signals_hold
    )
    # interpretationMethods.percentage_method_display(signals_buy, signals_sell, signals_hold)
    return additive, majority, median
