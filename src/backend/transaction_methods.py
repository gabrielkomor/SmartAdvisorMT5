"""
This file contains functions responsible for opening and closing investment positions on the financial market.
"""

from typing import Tuple, Any

import MetaTrader5 as mt5


def open_position(
    action_type: str, symbol: str, volume: float, comment: str, sl: float, tp: float
) -> bool:
    """
    This function is responsible for opening transaction positions.
    :param action_type: action type.
    :param symbol: trading symbol.
    :param volume: volume.
    :param comment: transaction comment.
    :param sl: stop loss.
    :param tp: take profit.
    :return: transaction success.
    """
    request = None

    if action_type == "buy":
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_BUY,
            "price": mt5.symbol_info_tick(symbol).ask,
            "sl": mt5.symbol_info_tick(symbol).ask * sl,
            "tp": mt5.symbol_info_tick(symbol).ask * tp,
            "deviation": 20,
            "magic": 234000,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }

    elif action_type == "sell":
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(symbol).bid,
            "sl": mt5.symbol_info_tick(symbol).ask * tp,
            "tp": mt5.symbol_info_tick(symbol).ask * sl,
            "deviation": 20,
            "magic": 234000,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }

    result = mt5.order_send(request)

    if result.retcode == mt5.TRADE_RETCODE_DONE:
        return True
    else:
        return False


def close_position(symbol: str, volume: float, comment: str) -> Tuple[bool, Any]:
    """
    This function is responsible for close trading positions.
    :param symbol: trading symbol.
    :param volume: volume.
    :param comment: position comment.
    :return: closed position.
    """
    positions = mt5.positions_get(symbol=symbol)

    if positions is None:
        return False, 0

    for position in positions:
        if (
            position.symbol == symbol
            and position.volume == volume
            and position.comment == comment
        ):
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": (
                    mt5.ORDER_TYPE_SELL
                    if position.type == mt5.ORDER_TYPE_BUY
                    else mt5.ORDER_TYPE_BUY
                ),
                "price": (
                    mt5.symbol_info_tick(symbol).bid
                    if position.type == mt5.ORDER_TYPE_BUY
                    else mt5.symbol_info_tick(symbol).ask
                ),
                "position": position.ticket,
                "sl": 0.0,
                "tp": 0.0,
                "deviation": 20,
                "magic": 234000,
                "comment": comment,
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }

            result = mt5.order_send(request)
            if result.retcode == mt5.TRADE_RETCODE_DONE:
                return True, position.profit
            else:
                return False, 0
    return False, 0
