"""
This file is responsible for the logic of the main application window.
"""

import os
import numpy as np
import MetaTrader5 as mt5

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QStandardItem

import src.frontend.log_in_ui as log_in_window
from src.frontend.log_in_ui import LogInUi
from src.backend.metatrader_backend import log_in, get_account_symbols
from src.backend.encryption_file import verify_hashed_password
from src.backend.encryption_file import encrypt_email, encrypt_password
from src.backend.data_base_connection import get_password_from_db, save_password_in_db
from src.backend.metatrader_backend import get_account_info
from src.backend.metatrader_backend import run_calculations
from src.backend.transaction_methods import open_position, close_position
from src.backend.metatrader_backend import get_account_open_positions


class MainWindowBackend:
    """
    This class is responsible for main window logic.
    """

    def __init__(self, gui, user_server, user_login, user_password) -> None:
        self.gui = gui
        self.stock_symbols = None
        self.candle_chart_data = None
        self.history_data = None
        self.user_server = user_server
        self.user_login = user_login
        self.user_password = user_password

    def update_stock_icons_data(self) -> None:
        """
        This method is responsible for update stock icons data in application.
        :return: nothing.
        """
        log_in(self.user_login, self.user_password, self.user_server)
        self.stock_symbols = get_account_symbols()

    def update_slider(self) -> None:
        """
        This method is responsible for update slider data in application.
        :return: nothing.
        """
        min_value, max_value = 0, 0
        try:
            selected_time_frame = (
                self.gui.combo_box_download_data_time_frame.currentText()
            )

            if self.gui.radio_button_download_data_forex.isChecked():
                data = self.gui.forex_data[selected_time_frame]
                min_value, max_value = data[0], data[1]
            elif self.gui.radio_button_download_data_stock.isChecked():
                data = self.gui.stock_data[selected_time_frame]
                min_value, max_value = data[0], data[1]
            elif self.gui.radio_button_download_data_etf.isChecked():
                data = self.gui.etf_data[selected_time_frame]
                min_value, max_value = data[0], data[1]

            self.gui.label_download_data_time_delta_min.setText(f"{min_value}")
            self.gui.label_download_data_time_delta_max.setText(f"{max_value}")
            self.gui.horizontal_slider_download_data_td.setRange(
                int(min_value), int(max_value)
            )
        except Exception as error:
            print(f"Error: {error}")

    def update_slider_value(self) -> None:
        """
        This method is responsible for update slider values.
        :return: nothing.
        """
        slider_value = self.gui.horizontal_slider_download_data_td.value()
        self.gui.label_download_data_value_slider.setText(f"Value: {slider_value} days")

    def update_backward_slider_value(self) -> None:
        """
        This method is responsible for update backward slier values.
        :return: nothing.
        """
        slider_value = self.gui.horizontal_slider_download_data_tb.value()
        self.gui.label_download_data_backwards_value.setText(
            f"Value: -{slider_value} days"
        )

    def update_combobox_value(self) -> None:
        """
        This method is responsible for update combo box values.
        :return: nothing.
        """
        self.update_slider()
        self.gui.combo_box_download_data_symbol.clear()

        if self.gui.radio_button_download_data_forex.isChecked():
            self.gui.combo_box_download_data_symbol.addItems(
                self.stock_symbols["forex"]
            )
        elif self.gui.radio_button_download_data_stock.isChecked():
            self.gui.combo_box_download_data_symbol.addItems(
                self.stock_symbols["stock"]
            )
        elif self.gui.radio_button_download_data_etf.isChecked():
            self.gui.combo_box_download_data_symbol.addItems(self.stock_symbols["etf"])

        self.candle_chart_data = 0
        self.history_data = 0

    def change_user_name(self) -> None:
        """
        This method is responsible for change username in ui.
        :return: nothing.
        """
        user_name = LogInUi.login_email
        user_name = user_name.split("@")[0]
        self.gui.user_name_label.setText(f"{user_name}")

    def change_user_password(self) -> None:
        """
        This method is responsible for changing user password via application form.
        :return: nothing.
        """
        try:
            user_email = LogInUi.login_email
            hashed_email = encrypt_email(user_email)
            old_password = self.gui.line_edit_user_data_old_password.text()
            db_password = get_password_from_db("users", hashed_email)

            if verify_hashed_password(old_password, db_password):
                new_password = self.gui.line_edit_user_data_new_password.text()
                confirm_password = self.gui.line_edit_user_data_confirm_password.text()

                if new_password != confirm_password:
                    self.gui.label_user_data_error.setText("Passwords are different")
                elif len(new_password) < 5:
                    self.gui.label_user_data_error.setText("Password too short")
                else:
                    hashed_password = encrypt_password(new_password)
                    save_password_in_db("users", hashed_email, hashed_password)
                    self.gui.label_user_data_error.setText("Password changed")
            else:
                self.gui.label_user_data_error.setText("Incorrect password")
        except Exception as error:
            print(f"Error: {error}")

    def update_user_data(self) -> None:
        """
        This method is responsible for update user transaction data.
        :return: nothing.
        """
        account_info = get_account_info()
        user_name = LogInUi.login_email
        user_name = user_name.split("@")[0]
        account_balance = account_info["balance"]
        account_profit = account_info["profit"]
        account_equity = account_info["equity"]

        self.gui.label_user_data_name_value.setText(f"{user_name}")
        self.gui.label_user_data_balance_value.setText(f"{account_balance} USD")
        self.gui.label_user_data_profit_value.setText(f"{account_profit} USD")
        self.gui.label_user_data_equity_value.setText(f"{account_equity} USD")

    def change_experts_icons(self, icons) -> None:
        """
        This method is responsible for change experts icons on ui.
        :param icons: images.
        :return: nothing.
        """
        experts_graphics = {
            "sma": lambda path: self.gui.label_sma_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "rsi": lambda path: self.gui.label_rsi_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "bb": lambda path: self.gui.label_bb_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "macd": lambda path: self.gui.label_macd_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            # 'mma': lambda path: self.gui.label_mma_decision.setPixmap(QtGui.QPixmap(path)),
            "adx": lambda path: self.gui.label_adx_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "vol": lambda path: self.gui.label_volume_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
        }

        for expert, icon in zip(experts_graphics.keys(), icons):
            experts_graphics[expert](f"src\\assets\\{icon}Icon.png")

    def change_aggregation_icons(self, icons) -> None:
        """
        This method is responsible for changing icons for aggregation methods in ui.
        :param icons: images.
        :return: nothing.
        """
        aggregation_graphics = {
            "additive": lambda path: self.gui.label_additive_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "majority": lambda path: self.gui.label_majority_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
            "median": lambda path: self.gui.label_median_decision.setPixmap(
                QtGui.QPixmap(path)
            ),
        }

        for aggregation, icon in zip(aggregation_graphics.keys(), icons):
            aggregation_graphics[aggregation](f"src\\assets\\{icon}Icon.png")

    def download_data_button(self) -> None:
        """
        This method is responsible for download data button logic.
        :return: nothing.
        """
        try:
            forex = False
            error = False
            self.gui.label_download_data_success.setText("Downloading data...")
            QtWidgets.QApplication.processEvents()
            selected_symbol = self.gui.combo_box_download_data_symbol.currentText()
            selected_time_frame = (
                self.gui.combo_box_download_data_time_frame.currentText()
            )
            selected_slider_value = self.gui.horizontal_slider_download_data_td.value()
            selected_slider_backward_value = (
                self.gui.horizontal_slider_download_data_tb.value()
            )

            if self.gui.radio_button_download_data_forex.isChecked():
                forex = True

            decisions = run_calculations(
                selected_symbol,
                int(selected_slider_value),
                selected_time_frame,
                forex,
                selected_slider_backward_value,
            )

            if not decisions[0]:
                self.gui.label_download_data_success.setText("No data for symbol")
                error = True

            if not error:
                self.gui.label_download_data_success.setText("Creating charts...")
                QtWidgets.QApplication.processEvents()

            self.gui.widget_candle_chart_place.setUrl(
                QUrl.fromLocalFile(os.path.abspath("src\\charts\\chart.html"))
            )
            self.gui.widget_hist_decision_place.setPixmap(
                QtGui.QPixmap("src\\charts\\histogram_chart.png")
            )
            self.gui.widget_linear_decisions_place.setPixmap(
                QtGui.QPixmap("src\\charts\\linear_chart.png")
            )
            self.gui.widget_signals_history_place.setPixmap(
                QtGui.QPixmap("src\\charts\\all_linear_chart.png")
            )

            if not error:
                experts_icons = np.array(["", "", "", "", "", "", "", ""], dtype="U4")
                buy_sig = decisions[1]["buy"]
                sell_sign = decisions[1]["sell"]
                hold_sign = decisions[1]["hold"]

                for i, (buy, sell, hold) in enumerate(
                    zip(buy_sig, sell_sign, hold_sign)
                ):
                    if hold > buy and hold > sell:
                        experts_icons[i] = "hold"
                    elif buy > hold and buy > sell:
                        experts_icons[i] = "buy"
                    elif sell > hold and sell > buy:
                        experts_icons[i] = "sell"
                    elif round(buy, 3) == round(sell, 3) == round(hold, 3):
                        experts_icons[i] = "mix"
                    else:
                        experts_icons[i] = "bysl"

                aggregation_icons = np.array(["", "", ""], dtype="U4")
                additive_sig = decisions[1]["additive"]
                majority_sig = decisions[1]["majority"]
                median_sig = decisions[1]["median"]

                additive = np.where(additive_sig == 1)[0]
                majority = np.where(majority_sig == 1)[0]
                median = np.where(median_sig == 1)[0]

                index = 0
                for element in (additive, majority, median):
                    if element == 2:
                        aggregation_icons[index] = "hold"
                    elif element == 1:
                        aggregation_icons[index] = "sell"
                    else:
                        aggregation_icons[index] = "buy"
                    index += 1

                self.change_experts_icons(experts_icons)
                self.change_aggregation_icons(aggregation_icons)

                self.gui.label_download_data_success.setText("Success")

        except Exception as error:
            print(f"error: {error}")
            self.gui.label_download_data_success.setText("Data download error")

    def make_transaction(self) -> None:
        """
        This method is responsible for make transaction button logic.
        :return: nothing.
        """
        trade_symbol = self.gui.line_edit_start_trade_symbol.text()
        trade_volume = self.gui.line_edit_start_trade_volume.text()
        trade_comment = self.gui.line_edit_start_trade_comment.text()
        trade_stop_loss = self.gui.line_edit_start_trade_stop_loss.text()
        trade_take_profit = self.gui.line_edit_start_trade_take_profit.text()
        trade_symbol = trade_symbol.upper()

        if (
            trade_symbol == ""
            or trade_comment == ""
            or trade_volume == ""
            or trade_stop_loss == ""
            or trade_take_profit == ""
        ):
            self.gui.label_start_trade_error.setText("No enough data")
        else:
            try:
                trade_volume = float(trade_volume)
                trade_stop_loss = 1 - (float(trade_stop_loss) / 100)
                trade_take_profit = 1 + (float(trade_take_profit) / 100)

                if self.gui.radio_button_start_trade_buy.isChecked():
                    if open_position(
                        "buy",
                        trade_symbol,
                        trade_volume,
                        trade_comment,
                        trade_stop_loss,
                        trade_take_profit,
                    ):
                        price = mt5.symbol_info_tick(trade_symbol).bid
                        trade_stop_loss = price * trade_stop_loss
                        trade_take_profit = price * trade_take_profit
                        self.add_row(
                            trade_symbol,
                            price,
                            trade_volume,
                            "buy",
                            round(trade_stop_loss, 5),
                            round(trade_take_profit, 5),
                            trade_comment,
                            "Nan",
                        )
                        self.gui.label_start_trade_error.setText(
                            "Long position was opened"
                        )
                        QtWidgets.QApplication.processEvents()
                    else:
                        self.gui.label_start_trade_error.setText(
                            "The purchase cannot be made"
                        )
                elif self.gui.radio_button_start_trade_sell.isChecked():
                    if open_position(
                        "sell",
                        trade_symbol,
                        trade_volume,
                        trade_comment,
                        trade_stop_loss,
                        trade_take_profit,
                    ):
                        price = mt5.symbol_info_tick(trade_symbol).bid
                        temp = trade_stop_loss
                        trade_stop_loss = price * trade_take_profit
                        trade_take_profit = price * temp
                        self.add_row(
                            trade_symbol,
                            price,
                            trade_volume,
                            "sell",
                            round(trade_stop_loss, 5),
                            round(trade_take_profit, 5),
                            trade_comment,
                            "Nan",
                        )
                        self.gui.label_start_trade_error.setText(
                            "Short position was opened"
                        )
                        QtWidgets.QApplication.processEvents()
                    else:
                        self.gui.label_start_trade_error.setText(
                            "The purchase cannot be made"
                        )
                elif self.gui.radio_button_start_trade_close.isChecked():
                    close_pos = close_position(
                        trade_symbol, trade_volume, trade_comment
                    )
                    if close_pos[0]:
                        self.remove_row_by_symbol(
                            trade_symbol, trade_volume, trade_comment
                        )
                        self.gui.label_start_trade_error.setText(
                            f"Position was closed: {close_pos[1]}"
                        )
                        QtWidgets.QApplication.processEvents()
                    else:
                        self.gui.label_start_trade_error.setText(
                            "The purchase not exist"
                        )

            except Exception as error:
                self.gui.label_start_trade_error.setText("Incorrect data")
                print(f"Error: {error}")

    def add_row(self, symbol, price, volume, action_type, sl, tp, comment, profit) -> None:
        """
        This method is responsible for adding new row in trading table.
        :param symbol: transaction symbol.
        :param price: transaction price.
        :param volume: transaction volume.
        :param action_type: buy / sell / hold.
        :param sl: stop loss.
        :param tp: take profit.
        :param comment: transaction comment.
        :param profit: transaction profit.
        :return: nothing.
        """
        row = [
            QStandardItem(str(symbol)),
            QStandardItem(str(price)),
            QStandardItem(str(action_type)),
            QStandardItem(str(volume)),
            QStandardItem(str(sl)),
            QStandardItem(str(tp)),
            QStandardItem(str(comment)),
            QStandardItem(str(profit)),
        ]
        self.gui.table_model.appendRow(row)

    def remove_row_by_symbol(self, symbol, volume, comment) -> None:
        """
        This method is responsible for remove row from transaction table.
        :param symbol: transaction symbol.
        :param volume: transaction volume.
        :param comment: transaction comment.
        :return: nothing.
        """
        row_count = self.gui.table_model.rowCount()

        for row in reversed(range(row_count)):
            if (
                self.gui.table_model.item(row, 0).text() == str(symbol)
                and self.gui.table_model.item(row, 3).text() == str(volume)
                and self.gui.table_model.item(row, 6).text() == str(comment)
            ):
                self.gui.table_model.removeRow(row)

        self.gui.table_view_start_trade.setModel(self.gui.table_model)
        self.gui.table_view_start_trade.viewport().update()

    def insert_opened_positions(self) -> None:
        """
        This method is responsible for adding new opened transaction position into table.
        :return: nothing.
        """
        positions = get_account_open_positions()
        self.gui.table_model.removeRows(0, self.gui.table_model.rowCount())

        if positions is not None:
            position_type = positions["type"].tolist()
            position_type = ["buy" if i == 0 else "sell" for i in position_type]
            price = tuple(positions["price_current"])
            sl = tuple(positions["sl"])
            tp = tuple(positions["tp"])
            symbols = tuple(positions["symbol"])
            volume = tuple(positions["volume"])
            comment = tuple(positions["comment"])
            profit = tuple(positions["profit"])

            # 1 = buy, 2 = sell
            for i in range(len(symbols)):
                self.add_row(
                    str(symbols[i]),
                    str(price[i]),
                    str(volume[i]),
                    str(position_type[i]),
                    str(round(sl[i], 4)),
                    str(round(tp[i], 4)),
                    str(comment[i]),
                    str(profit[i]),
                )

    def close_app(self, active_window) -> None:
        """
        This method is responsible for close main window application and delete charts.
        :param active_window: main window.
        :return: nothing.
        """
        charts = np.array(
            [
                "chart.html",
                "histogram_chart.png",
                "linear_chart.png",
                "all_linear_chart.png",
            ]
        )

        for chart in charts:
            if os.path.exists(f"src\\charts\\{chart}"):
                os.remove(f"src\\charts\\{chart}")

        self.gui.window = QtWidgets.QWidget()
        self.gui.ui = log_in_window.LogInUi()
        self.gui.ui.setup_ui(self.gui.window)
        self.gui.window.show()
        active_window.close()
        active_window.deleteLater()
