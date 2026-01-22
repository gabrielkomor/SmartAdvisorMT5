from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PyQt6.QtWidgets import QApplication

from interfaces.main_window_files.candle_chart_window import CandleChartBuilder
from interfaces.main_window_files.signals_history_window import SignalsHistoryBuilder
from interfaces.main_window_files.start_trade_window import StartTradeBuilder
from interfaces.main_window_files.download_data_window import DownloadDataBuilder
from interfaces.main_window_files.user_window import UserWindowBuilder
from interfaces.main_window_files.hist_decisions_window import HistDecisionBuilder
from interfaces.main_window_files.linear_decisions_window import LinearDecisionsBuilder
from interfaces.main_window_files.top_frame_window import TopFrameBuilder
from interfaces.main_window_files.small_left_frame_window import SmallLeftFrameBuilder
from interfaces.main_window_files.big_left_frame_window import BigLeftFrameBuilder
from interfaces.main_window_files.right_frame_window import RightFrameBuilder
from interfaces.main_window_files.bottom_frame_window import BottomFrameBuilder
from interfaces.main_window_files.main_window_backend import MainWindowBackend
from interfaces.log_in_mt5_ui import LogInMt5Ui


class UiMainWindow(object):
    def __init__(self):
        self.central_widget = None
        self.grid_layout = None
        self.center_frame = None
        self.horizontal_layout_5 = None
        self.stacked_widget = None
        self.user_login = None
        self.user_password = None
        self.user_server = None
        self.download_data_builder = None
        self.download_data_stacked_widget = None
        self.radio_button_download_data_forex = None
        self.radio_button_download_data_stock = None
        self.radio_button_download_data_etf = None
        self.label_download_data_symbol = None
        self.combo_box_download_data_symbol = None
        self.label_download_data_time_frame = None
        self.combo_box_download_data_time_frame = None
        self.label_download_data_time_delta = None
        self.label_download_data_time_delta_min = None
        self.horizontal_slider_download_data_td = None
        self.label_download_data_time_delta_max = None
        self.label_download_data_value_slider = None
        self.push_button_download_data_dd = None
        self.label_download_data_success = None
        self.label_download_data_time_backwards = None
        self.label_download_data_time_backwards_min = None
        self.horizontal_slider_download_data_tb = None
        self.label_download_data_time_backwards_max = None
        self.label_download_data_backwards_value = None
        self.candle_chart_builder = None
        self.candle_chart_stacked_widget = None
        self.horizontal_layout_11 = None
        self.widget_candle_chart_place = None
        self.signals_history_builder = None
        self.signals_history_stacked_widget = None
        self.horizontal_layout_12 = None
        self.widget_signals_history_place = None
        self.hist_decisions_builder = None
        self.hist_decisions_stacked_widget = None
        self.widget_hist_decision_place = None
        self.linear_decisions_builder = None
        self.linear_decisions_stacked_widget = None
        self.widget_linear_decisions_place = None
        self.start_trade_builder = None
        self.start_trade_stacked_widget = None
        self.radio_button_start_trade_buy = None
        self.radio_button_start_trade_sell = None
        self.radio_button_start_trade_close = None
        self.label_start_trade_symbol = None
        self.line_edit_start_trade_symbol = None
        self.label_start_trade_volume = None
        self.line_edit_start_trade_volume = None
        self.label_start_trade_stop_loss = None
        self.line_edit_start_trade_stop_loss = None
        self.label_start_trade_take_profit = None
        self.line_edit_start_trade_take_profit = None
        self.label_start_trade_comment = None
        self.line_edit_start_trade_comment = None
        self.push_button_start_trade = None
        self.label_start_trade_error = None
        self.table_view_start_trade = None
        self.table_model = None
        self.user_window_builder = None
        self.user_data_stacked_widget = None
        self.label_user_data_name = None
        self.label_user_data_name_value = None
        self.label_user_data_balance = None
        self.label_user_data_balance_value = None
        self.label_user_data_profit = None
        self.label_user_data_profit_value = None
        self.label_user_data_equity = None
        self.label_user_data_equity_value = None
        self.line_edit_user_data_old_password = None
        self.line_edit_user_data_new_password = None
        self.line_edit_user_data_confirm_password = None
        self.push_button_user_data_cp = None
        self.label_user_data_error = None
        self.top_frame_builder = None
        self.top_frame = None
        self.app_icon_label = None
        self.app_name_label = None
        self.user_name_label = None
        self.push_button_user = None
        self.small_left_frame_builder = None
        self.small_left_frame = None
        self.push_button_small_show_menu = None
        self.push_button_small_download = None
        self.push_button_small_candle_chart = None
        self.push_button_small_signals_history = None
        self.push_button_small_hist_decisions = None
        self.push_button_small_linear_decisions = None
        self.push_button_small_start_trade = None
        self.push_button_small_exit_application = None
        self.big_left_frame_builder = None
        self.big_left_frame = None
        self.push_button_big_show_menu = None
        self.push_button_big_download_data = None
        self.push_button_big_candle_chart = None
        self.push_button_big_signals_history = None
        self.push_button_big_hist_decisions = None
        self.push_button_big_linear_decisions = None
        self.push_button_big_start_trade = None
        self.push_button_big_exit_application = None
        self.right_frame_builder = None
        self.right_frame = None
        self.label_sma = None
        self.label_sma_decision = None
        self.label_rsi = None
        self.label_rsi_decision = None
        self.label_bb = None
        self.label_bb_decision = None
        self.label_macd = None
        self.label_macd_decision = None
        self.label_adx = None
        self.label_adx_decision = None
        self.label_volume = None
        self.label_volume_decision = None
        self.bottom_frame_builder = None
        self.bottom_frame = None
        self.label_additive = None
        self.label_additive_decision = None
        self.label_majority = None
        self.label_majority_decision = None
        self.label_median = None
        self.label_median_decision = None
        self.app_backend = None
        self.forex_data = None
        self.stock_data = None
        self.etf_data = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1064, 637)
        main_window.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("gridLayout")
        self.center_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.center_frame.setMinimumSize(QtCore.QSize(5, 5))
        self.center_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.center_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.center_frame.setObjectName("centerFrame")
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout(self.center_frame)
        self.horizontal_layout_5.setObjectName("horizontalLayout_5")
        self.stacked_widget = QtWidgets.QStackedWidget(parent=self.center_frame)
        self.stacked_widget.setObjectName("stackedWidget")

        # mt5 login data
        self.user_login = LogInMt5Ui.user_login
        self.user_password = LogInMt5Ui.user_password
        self.user_server = LogInMt5Ui.user_server

        # download data window widget
        self.download_data_builder = DownloadDataBuilder()
        self.download_data_builder.download_data_setup()
        self.download_data_stacked_widget = (
            self.download_data_builder.download_data_stacked_widget
        )
        self.radio_button_download_data_forex = (
            self.download_data_builder.radio_button_download_data_forex
        )
        self.radio_button_download_data_stock = (
            self.download_data_builder.radio_button_download_data_stock
        )
        self.radio_button_download_data_etf = (
            self.download_data_builder.radio_button_download_data_etf
        )
        self.label_download_data_symbol = (
            self.download_data_builder.label_download_data_symbol
        )
        self.combo_box_download_data_symbol = (
            self.download_data_builder.combo_box_download_data_symbol
        )
        self.label_download_data_time_frame = (
            self.download_data_builder.label_download_data_time_frame
        )
        self.combo_box_download_data_time_frame = (
            self.download_data_builder.combo_box_download_data_time_frame
        )
        self.label_download_data_time_delta = (
            self.download_data_builder.label_download_data_time_delta
        )
        self.label_download_data_time_delta_min = (
            self.download_data_builder.label_download_data_time_delta_min
        )
        self.horizontal_slider_download_data_td = (
            self.download_data_builder.horizontal_slider_download_data_td
        )
        self.label_download_data_time_delta_max = (
            self.download_data_builder.label_download_data_time_delta_max
        )
        self.label_download_data_value_slider = (
            self.download_data_builder.label_download_data_value_slider
        )
        self.push_button_download_data_dd = (
            self.download_data_builder.push_button_download_data_dd
        )
        self.label_download_data_success = (
            self.download_data_builder.label_download_data_success
        )
        self.label_download_data_time_backwards = (
            self.download_data_builder.label_download_data_time_backwards
        )
        self.label_download_data_time_backwards_min = (
            self.download_data_builder.label_download_data_time_backwards_min
        )
        self.horizontal_slider_download_data_tb = (
            self.download_data_builder.horizontal_slider_download_data_tb
        )
        self.label_download_data_time_backwards_max = (
            self.download_data_builder.label_download_data_time_backwards_max
        )
        self.label_download_data_backwards_value = (
            self.download_data_builder.label_download_data_backwards_value
        )
        self.stacked_widget.addWidget(self.download_data_stacked_widget)

        # japanese candle chart window widget
        self.candle_chart_builder = CandleChartBuilder()
        self.candle_chart_builder.candle_chart_setup()
        self.candle_chart_stacked_widget = (
            self.candle_chart_builder.candle_chart_stacked_widget
        )
        self.horizontal_layout_11 = self.candle_chart_builder.horizontal_layout_11
        self.widget_candle_chart_place = (
            self.candle_chart_builder.widget_candle_chart_place
        )
        self.stacked_widget.addWidget(self.candle_chart_stacked_widget)

        # many charts window widget
        self.signals_history_builder = SignalsHistoryBuilder()
        self.signals_history_builder.signals_history_setup()
        self.signals_history_stacked_widget = (
            self.signals_history_builder.signals_history_stacked_widget
        )
        self.horizontal_layout_12 = self.signals_history_builder.horizontal_layout_12
        self.widget_signals_history_place = (
            self.signals_history_builder.widget_signals_history_place
        )
        self.stacked_widget.addWidget(self.signals_history_stacked_widget)

        # hist charts window widget
        self.hist_decisions_builder = HistDecisionBuilder()
        self.hist_decisions_builder.hist_decision_setup()
        self.hist_decisions_stacked_widget = (
            self.hist_decisions_builder.hist_decisions_stacked_widget
        )
        self.widget_hist_decision_place = (
            self.hist_decisions_builder.widget_hist_decision_place
        )
        self.stacked_widget.addWidget(self.hist_decisions_stacked_widget)

        # linear chart window widget
        self.linear_decisions_builder = LinearDecisionsBuilder()
        self.linear_decisions_builder.linear_decisions_setup()
        self.linear_decisions_stacked_widget = (
            self.linear_decisions_builder.linear_decisions_stacked_widget
        )
        self.widget_linear_decisions_place = (
            self.linear_decisions_builder.widget_linear_decisions_place
        )
        self.stacked_widget.addWidget(self.linear_decisions_stacked_widget)

        # start trade window widget
        self.start_trade_builder = StartTradeBuilder()
        self.start_trade_builder.start_trade_setup()
        self.start_trade_stacked_widget = (
            self.start_trade_builder.start_trade_stacked_widget
        )
        self.radio_button_start_trade_buy = (
            self.start_trade_builder.radio_button_start_trade_buy
        )
        self.radio_button_start_trade_sell = (
            self.start_trade_builder.radio_button_start_trade_sell
        )
        self.radio_button_start_trade_close = (
            self.start_trade_builder.radio_button_start_trade_close
        )
        self.label_start_trade_symbol = (
            self.start_trade_builder.label_start_trade_symbol
        )
        self.line_edit_start_trade_symbol = (
            self.start_trade_builder.line_edit_start_trade_symbol
        )
        self.label_start_trade_volume = (
            self.start_trade_builder.label_start_trade_volume
        )
        self.line_edit_start_trade_volume = (
            self.start_trade_builder.line_edit_start_trade_volume
        )
        self.label_start_trade_stop_loss = (
            self.start_trade_builder.label_start_trade_stop_loss
        )
        self.line_edit_start_trade_stop_loss = (
            self.start_trade_builder.line_edit_start_trade_stop_loss
        )
        self.label_start_trade_take_profit = (
            self.start_trade_builder.label_start_trade_take_profit
        )
        self.line_edit_start_trade_take_profit = (
            self.start_trade_builder.line_edit_start_trade_take_profit
        )
        self.label_start_trade_comment = (
            self.start_trade_builder.label_start_trade_comment
        )
        self.line_edit_start_trade_comment = (
            self.start_trade_builder.line_edit_start_trade_comment
        )
        self.push_button_start_trade = self.start_trade_builder.push_button_start_trade
        self.label_start_trade_error = self.start_trade_builder.label_start_trade_error
        self.table_view_start_trade = self.start_trade_builder.table_view_start_trade
        self.table_model = self.start_trade_builder.table_model
        self.stacked_widget.addWidget(self.start_trade_stacked_widget)

        # user data and change password window widget
        self.user_window_builder = UserWindowBuilder()
        self.user_window_builder.user_window_setup()
        self.user_data_stacked_widget = (
            self.user_window_builder.user_data_stacked_widget
        )
        self.label_user_data_name = self.user_window_builder.label_user_data_name
        self.label_user_data_name_value = (
            self.user_window_builder.label_user_data_name_value
        )
        self.label_user_data_balance = self.user_window_builder.label_user_data_balance
        self.label_user_data_balance_value = (
            self.user_window_builder.label_user_data_balance_value
        )
        self.label_user_data_profit = self.user_window_builder.label_user_data_profit
        self.label_user_data_profit_value = (
            self.user_window_builder.label_user_data_profit_value
        )
        self.label_user_data_equity = self.user_window_builder.label_user_data_equity
        self.label_user_data_equity_value = (
            self.user_window_builder.label_user_data_equity_value
        )
        self.line_edit_user_data_old_password = (
            self.user_window_builder.line_edit_user_data_old_password
        )
        self.line_edit_user_data_new_password = (
            self.user_window_builder.line_edit_user_data_new_password
        )
        self.line_edit_user_data_confirm_password = (
            self.user_window_builder.line_edit_user_data_confirm_password
        )
        self.push_button_user_data_cp = (
            self.user_window_builder.push_button_user_data_cp
        )
        self.label_user_data_error = self.user_window_builder.label_user_data_error
        self.stacked_widget.addWidget(self.user_data_stacked_widget)

        # layout settings
        self.horizontal_layout_5.addWidget(self.stacked_widget)
        self.grid_layout.addWidget(self.center_frame, 1, 2, 1, 1)

        # top application bar
        self.top_frame_builder = TopFrameBuilder(self.central_widget)
        self.top_frame_builder.top_frame_setup()
        self.top_frame = self.top_frame_builder.top_frame
        self.app_icon_label = self.top_frame_builder.app_icon_label
        self.app_name_label = self.top_frame_builder.app_name_label
        self.user_name_label = self.top_frame_builder.user_name_label
        self.push_button_user = self.top_frame_builder.push_button_user
        self.grid_layout.addWidget(self.top_frame, 0, 0, 1, 4)

        # small left application menu
        self.small_left_frame_builder = SmallLeftFrameBuilder(self.central_widget)
        icons = self.small_left_frame_builder.small_left_frame_setup()
        self.small_left_frame = self.small_left_frame_builder.small_left_frame
        self.push_button_small_show_menu = (
            self.small_left_frame_builder.push_button_small_show_menu
        )
        self.push_button_small_download = (
            self.small_left_frame_builder.push_button_small_download
        )
        self.push_button_small_candle_chart = (
            self.small_left_frame_builder.push_button_small_candle_chart
        )
        self.push_button_small_signals_history = (
            self.small_left_frame_builder.push_button_small_signals_history
        )
        self.push_button_small_hist_decisions = (
            self.small_left_frame_builder.push_button_small_hist_decisions
        )
        self.push_button_small_linear_decisions = (
            self.small_left_frame_builder.push_button_small_linear_decisions
        )
        self.push_button_small_start_trade = (
            self.small_left_frame_builder.push_button_small_start_trade
        )
        self.push_button_small_exit_application = (
            self.small_left_frame_builder.push_button_small_exit_application
        )
        self.grid_layout.addWidget(
            self.small_left_frame, 1, 0, 2, 1, QtCore.Qt.AlignmentFlag.AlignLeft
        )

        # big left application menu
        self.big_left_frame_builder = BigLeftFrameBuilder(self.central_widget)
        self.big_left_frame_builder.big_left_frame_setup(icons)
        self.big_left_frame = self.big_left_frame_builder.big_left_frame
        self.push_button_big_show_menu = (
            self.big_left_frame_builder.button_big_show_menu
        )
        self.push_button_big_download_data = (
            self.big_left_frame_builder.button_big_download_data
        )
        self.push_button_big_candle_chart = (
            self.big_left_frame_builder.button_big_candle_chart
        )
        self.push_button_big_signals_history = (
            self.big_left_frame_builder.button_big_signals_history
        )
        self.push_button_big_hist_decisions = (
            self.big_left_frame_builder.button_big_hist_decisions
        )
        self.push_button_big_linear_decisions = (
            self.big_left_frame_builder.button_big_linear_decisions
        )
        self.push_button_big_start_trade = (
            self.big_left_frame_builder.button_big_start_trade
        )
        self.push_button_big_exit_application = (
            self.big_left_frame_builder.button_big_exit_application
        )
        self.grid_layout.addWidget(
            self.big_left_frame, 1, 1, 2, 1, QtCore.Qt.AlignmentFlag.AlignLeft
        )

        # right application menu
        self.right_frame_builder = RightFrameBuilder(self.central_widget)
        self.right_frame_builder.right_frame_builder_setup()
        self.right_frame = self.right_frame_builder.right_frame
        self.label_sma = self.right_frame_builder.label_sma
        self.label_sma_decision = self.right_frame_builder.label_sma_decision
        self.label_rsi = self.right_frame_builder.label_rsi
        self.label_rsi_decision = self.right_frame_builder.label_rsi_decision
        self.label_bb = self.right_frame_builder.label_bb
        self.label_bb_decision = self.right_frame_builder.label_bb_decision
        self.label_macd = self.right_frame_builder.label_macd
        self.label_macd_decision = self.right_frame_builder.label_macd_decision
        self.label_adx = self.right_frame_builder.label_adx
        self.label_adx_decision = self.right_frame_builder.label_adx_decision
        self.label_volume = self.right_frame_builder.label_volume
        self.label_volume_decision = self.right_frame_builder.label_volume_decision
        self.grid_layout.addWidget(self.right_frame, 1, 3, 2, 1)

        # bottom application bar
        self.bottom_frame_builder = BottomFrameBuilder(self.central_widget)
        self.bottom_frame_builder.bottom_frame_setup()
        self.bottom_frame = self.bottom_frame_builder.bottom_frame
        self.label_additive = self.bottom_frame_builder.label_additive
        self.label_additive_decision = self.bottom_frame_builder.label_additive_decision
        self.label_majority = self.bottom_frame_builder.label_majority
        self.label_majority_decision = self.bottom_frame_builder.label_majority_decision
        self.label_median = self.bottom_frame_builder.label_median
        self.label_median_decision = self.bottom_frame_builder.label_median_decision
        self.grid_layout.addWidget(self.bottom_frame, 2, 2, 1, 1)

        # main app widget
        main_window.setCentralWidget(self.central_widget)
        self.re_translate_ui(main_window)
        self.stacked_widget.setCurrentIndex(0)

        # creating a backend instance
        self.app_backend = MainWindowBackend(
            self, self.user_server, self.user_login, self.user_password
        )

        # buttons connection between small and big app menu
        self.push_button_big_show_menu.pressed.connect(self.small_left_frame.show)
        self.push_button_big_show_menu.pressed.connect(self.big_left_frame.hide)
        self.push_button_small_show_menu.pressed.connect(self.small_left_frame.hide)
        self.push_button_small_show_menu.pressed.connect(self.big_left_frame.show)
        self.push_button_big_show_menu.pressed.connect(self.right_frame.hide)
        self.push_button_big_show_menu.pressed.connect(self.bottom_frame.hide)
        self.push_button_small_show_menu.pressed.connect(self.bottom_frame.show)
        self.push_button_small_show_menu.pressed.connect(self.right_frame.show)

        self.push_button_small_download.toggled["bool"].connect(
            self.push_button_big_download_data.setChecked
        )
        self.push_button_small_candle_chart.toggled["bool"].connect(
            self.push_button_big_candle_chart.setChecked
        )
        self.push_button_small_signals_history.toggled["bool"].connect(
            self.push_button_big_signals_history.setChecked
        )
        self.push_button_small_hist_decisions.toggled["bool"].connect(
            self.push_button_big_hist_decisions.setChecked
        )
        self.push_button_small_linear_decisions.toggled["bool"].connect(
            self.push_button_big_linear_decisions.setChecked
        )
        self.push_button_small_start_trade.toggled["bool"].connect(
            self.push_button_big_start_trade.setChecked
        )
        self.push_button_small_exit_application.toggled["bool"].connect(
            self.push_button_big_exit_application.setChecked
        )
        self.push_button_big_download_data.toggled["bool"].connect(
            self.push_button_small_download.setChecked
        )
        self.push_button_big_candle_chart.toggled["bool"].connect(
            self.push_button_small_candle_chart.setChecked
        )
        self.push_button_big_signals_history.toggled["bool"].connect(
            self.push_button_small_signals_history.setChecked
        )
        self.push_button_big_hist_decisions.toggled["bool"].connect(
            self.push_button_small_hist_decisions.setChecked
        )
        self.push_button_big_linear_decisions.toggled["bool"].connect(
            self.push_button_small_linear_decisions.setChecked
        )
        self.push_button_big_start_trade.toggled["bool"].connect(
            self.push_button_small_start_trade.setChecked
        )
        self.push_button_big_exit_application.toggled["bool"].connect(
            self.push_button_small_exit_application.setChecked
        )
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.set_dark_theme()

        def switch_page_with_animation(new_widget):
            old_widget = self.stacked_widget.currentWidget()
            if old_widget == new_widget:
                return

            stacked_geometry = self.stacked_widget.geometry()
            width = stacked_geometry.width()
            height = stacked_geometry.height()
            new_widget.setGeometry(
                stacked_geometry.x() - width, stacked_geometry.y(), width, height
            )
            self.stacked_widget.setCurrentWidget(new_widget)
            start_rect = QRect(
                stacked_geometry.x() - width, stacked_geometry.y() - 10, width, height
            )
            end_rect = QRect(
                stacked_geometry.x(), stacked_geometry.y() - 10, width, height
            )
            self.animation = QPropertyAnimation(new_widget, b"geometry")
            self.animation.setDuration(300)
            self.animation.setStartValue(start_rect)
            self.animation.setEndValue(end_rect)
            self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
            self.animation.start()

            def stabilize_widget_position():
                new_widget.setGeometry(end_rect)
                new_widget.updateGeometry()

            self.animation.finished.connect(stabilize_widget_position)

        # change stacked widgets buttons
        # hide small manu
        self.small_left_frame.hide()
        # user button
        self.push_button_user.clicked.connect(
            lambda: (
                switch_page_with_animation(self.user_data_stacked_widget),
                self.app_backend.update_user_data(),
            )
        )
        # download button
        self.push_button_big_download_data.clicked.connect(
            lambda: (
                switch_page_with_animation(self.download_data_stacked_widget),
                self.app_backend.update_stock_icons_data(),
            )
        )
        self.push_button_small_download.clicked.connect(
            lambda: (
                switch_page_with_animation(self.download_data_stacked_widget),
                self.app_backend.update_stock_icons_data(),
            )
        )
        # candle chart button
        self.push_button_big_candle_chart.clicked.connect(
            lambda: switch_page_with_animation(self.candle_chart_stacked_widget)
        )
        self.push_button_small_candle_chart.clicked.connect(
            lambda: switch_page_with_animation(self.candle_chart_stacked_widget)
        )
        # signals history button
        self.push_button_big_signals_history.clicked.connect(
            lambda: switch_page_with_animation(self.signals_history_stacked_widget)
        )
        self.push_button_small_signals_history.clicked.connect(
            lambda: switch_page_with_animation(self.signals_history_stacked_widget)
        )
        # hist decisions button
        self.push_button_big_hist_decisions.clicked.connect(
            lambda: switch_page_with_animation(self.hist_decisions_stacked_widget)
        )
        self.push_button_small_hist_decisions.clicked.connect(
            lambda: switch_page_with_animation(self.hist_decisions_stacked_widget)
        )
        # linear decisions button
        self.push_button_big_linear_decisions.clicked.connect(
            lambda: switch_page_with_animation(self.linear_decisions_stacked_widget)
        )
        self.push_button_small_linear_decisions.clicked.connect(
            lambda: switch_page_with_animation(self.linear_decisions_stacked_widget)
        )
        self.push_button_big_start_trade.clicked.connect(
            lambda: (
                switch_page_with_animation(self.start_trade_stacked_widget),
                self.app_backend.insert_opened_positions(),
            )
        )
        self.push_button_small_start_trade.clicked.connect(
            lambda: (
                switch_page_with_animation(self.start_trade_stacked_widget),
                self.app_backend.insert_opened_positions(),
            )
        )

        # user name
        self.app_backend.change_user_name()

        # change password
        self.push_button_user_data_cp.clicked.connect(
            self.app_backend.change_user_password
        )

        # exit button
        self.push_button_big_exit_application.clicked.connect(
            lambda: self.app_backend.close_app(main_window)
        )
        self.push_button_small_exit_application.clicked.connect(
            lambda: self.app_backend.close_app(main_window)
        )

        # download data stacked widget mechanic
        self.push_button_download_data_dd.clicked.connect(
            lambda: self.app_backend.download_data_button()
        )
        self.horizontal_slider_download_data_td.valueChanged.connect(
            self.app_backend.update_slider_value
        )
        self.horizontal_slider_download_data_tb.valueChanged.connect(
            self.app_backend.update_backward_slider_value
        )
        self.radio_button_download_data_forex.toggled.connect(
            self.app_backend.update_combobox_value
        )
        self.radio_button_download_data_stock.toggled.connect(
            self.app_backend.update_combobox_value
        )
        self.radio_button_download_data_etf.toggled.connect(
            self.app_backend.update_combobox_value
        )
        self.combo_box_download_data_time_frame.currentTextChanged.connect(
            self.app_backend.update_slider
        )

        # make transaction mechanics
        self.push_button_start_trade.clicked.connect(self.app_backend.make_transaction)

        self.app_backend.update_stock_icons_data()

        self.combo_box_download_data_symbol.clear()
        self.combo_box_download_data_symbol.addItems(
            self.app_backend.stock_symbols["forex"]
        )
        self.horizontal_slider_download_data_td.setRange(1, 2)
        self.label_download_data_time_delta_min.setText("1")
        self.label_download_data_time_delta_max.setText("2")

        self.app_backend.insert_opened_positions()

        self.forex_data = {
            "1 Min": (1, 2),
            "5 Min": (1, 3),
            "15 Min": (3, 6),
            "30 Min": (5, 20),
            "1 H": (8, 50),
            "3 H": (20, 80),
            "6 H": (60, 150),
            "12 H": (100, 365),
        }

        self.stock_data = {
            "1 Min": (1, 2),
            "5 Min": (3, 8),
            "15 Min": (5, 12),
            "30 Min": (8, 30),
            "1 H": (15, 50),
            "3 H": (25, 120),
            "6 H": (55, 250),
            "12 H": (100, 700),
        }

        self.etf_data = {
            "1 Min": (2, 4),
            "5 Min": (3, 10),
            "15 Min": (8, 30),
            "30 Min": (15, 70),
            "1 H": (20, 120),
            "3 H": (60, 300),
            "6 H": (90, 500),
            "12 H": (120, 1000),
        }

    def re_translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowIcon(QtGui.QIcon("images\\Icon.png"))
        main_window.setWindowTitle(_translate("MainWindow", "Smart Advisor MT5"))
        self.radio_button_download_data_forex.setText(_translate("MainWindow", "Forex"))
        self.radio_button_download_data_stock.setText(_translate("MainWindow", "Stock"))
        self.radio_button_download_data_etf.setText(_translate("MainWindow", "ETF"))
        self.label_download_data_symbol.setText(_translate("MainWindow", "Symbol"))
        self.combo_box_download_data_symbol.setItemText(
            0, _translate("MainWindow", "test")
        )
        self.combo_box_download_data_symbol.setItemText(
            1, _translate("MainWindow", "test2 ")
        )
        self.label_download_data_time_frame.setText(
            _translate("MainWindow", "Time Frame")
        )
        self.combo_box_download_data_time_frame.setItemText(
            0, _translate("MainWindow", "1 Min")
        )
        self.combo_box_download_data_time_frame.setItemText(
            1, _translate("MainWindow", "5 Min")
        )
        self.combo_box_download_data_time_frame.setItemText(
            2, _translate("MainWindow", "15 Min")
        )
        self.combo_box_download_data_time_frame.setItemText(
            3, _translate("MainWindow", "30 Min")
        )
        self.combo_box_download_data_time_frame.setItemText(
            4, _translate("MainWindow", "1 H")
        )
        self.combo_box_download_data_time_frame.setItemText(
            5, _translate("MainWindow", "3 H")
        )
        self.combo_box_download_data_time_frame.setItemText(
            6, _translate("MainWindow", "6 H")
        )
        self.combo_box_download_data_time_frame.setItemText(
            7, _translate("MainWindow", "12 H")
        )
        self.label_download_data_time_delta.setText(
            _translate("MainWindow", "Time Delta")
        )
        self.label_download_data_time_delta_min.setText(_translate("MainWindow", "3"))
        self.label_download_data_time_delta_max.setText(_translate("MainWindow", "15"))
        self.label_download_data_value_slider.setText(
            _translate("MainWindow", "Value: ")
        )
        self.push_button_download_data_dd.setText(
            _translate("MainWindow", "Download Data")
        )
        self.label_download_data_success.setText(_translate("MainWindow", ""))
        self.radio_button_start_trade_buy.setText(_translate("MainWindow", "Buy"))
        self.radio_button_start_trade_sell.setText(_translate("MainWindow", "Sell"))
        self.radio_button_start_trade_close.setText(_translate("MainWindow", "Close"))
        self.label_start_trade_symbol.setText(_translate("MainWindow", "Symbol"))
        self.label_start_trade_volume.setText(_translate("MainWindow", "Volume"))
        self.label_start_trade_stop_loss.setText(
            _translate("MainWindow", "Stop Loss (%)")
        )
        self.label_start_trade_take_profit.setText(
            _translate("MainWindow", "Take Profit (%)")
        )
        self.label_start_trade_comment.setText(_translate("MainWindow", "Comment"))
        self.push_button_start_trade.setText(
            _translate("MainWindow", "Make The Transaction")
        )
        self.label_start_trade_error.setText(_translate("MainWindow", ""))
        self.label_user_data_name.setText(_translate("MainWindow", "Name:"))
        self.label_user_data_name_value.setText(_translate("MainWindow", "None"))
        self.label_user_data_balance.setText(_translate("MainWindow", "Balance:"))
        self.label_user_data_balance_value.setText(_translate("MainWindow", "None USD"))
        self.label_user_data_profit.setText(_translate("MainWindow", "Profit:"))
        self.label_user_data_profit_value.setText(_translate("MainWindow", "None USD"))
        self.label_user_data_equity.setText(_translate("MainWindow", "Equity:"))
        self.label_user_data_equity_value.setText(_translate("MainWindow", "None USD"))
        self.line_edit_user_data_old_password.setPlaceholderText(
            _translate("MainWindow", "Old password")
        )
        self.line_edit_user_data_new_password.setPlaceholderText(
            _translate("MainWindow", "New password")
        )
        self.line_edit_user_data_confirm_password.setPlaceholderText(
            _translate("MainWindow", "Confirm password")
        )
        self.line_edit_start_trade_comment.setPlaceholderText(
            _translate("MainWindow", "e.g. Txt /bsc")
        )
        self.line_edit_start_trade_volume.setPlaceholderText(
            _translate("MainWindow", "e.g. 2.5 /bsc")
        )
        self.line_edit_start_trade_symbol.setPlaceholderText(
            _translate("MainWindow", "e.g. EURPLN /bsc")
        )
        self.line_edit_start_trade_stop_loss.setPlaceholderText(
            _translate("MainWindow", "e.g. 3 /bs")
        )
        self.line_edit_start_trade_take_profit.setPlaceholderText(
            _translate("MainWindow", "e.g. 3 /bs")
        )
        self.push_button_user_data_cp.setText(
            _translate("MainWindow", "Change Password")
        )
        self.label_user_data_error.setText(_translate("MainWindow", ""))
        self.app_name_label.setText(_translate("MainWindow", "Smart Advisor MT5"))
        self.user_name_label.setText(_translate("MainWindow", "None"))
        self.push_button_big_show_menu.setText(_translate("MainWindow", " Hide Menu"))
        self.push_button_big_download_data.setText(
            _translate("MainWindow", "Download Data")
        )
        self.push_button_big_candle_chart.setText(
            _translate("MainWindow", "Candle Chart")
        )
        self.push_button_big_signals_history.setText(
            _translate("MainWindow", "Signals History")
        )
        self.push_button_big_hist_decisions.setText(
            _translate("MainWindow", "Hist Decisions")
        )
        self.push_button_big_linear_decisions.setText(
            _translate("MainWindow", "Linear Decisions")
        )
        self.push_button_big_start_trade.setText(
            _translate("MainWindow", "Start Trade")
        )
        self.push_button_big_exit_application.setText(
            _translate("MainWindow", "Exit Application")
        )
        self.label_sma.setText(_translate("MainWindow", "SMA"))
        self.label_rsi.setText(_translate("MainWindow", "RSI"))
        self.label_bb.setText(_translate("MainWindow", "BB"))
        self.label_macd.setText(_translate("MainWindow", "MACD"))
        self.label_adx.setText(_translate("MainWindow", "ADX"))
        self.label_volume.setText(_translate("MainWindow", "Volume"))
        self.label_additive.setText(_translate("MainWindow", "Additive"))
        self.label_majority.setText(_translate("MainWindow", "Majority"))
        self.label_median.setText(_translate("MainWindow", "Median"))
        self.label_download_data_time_backwards.setText(
            _translate("MainWindow", "Time Backwards")
        )
        self.label_download_data_time_backwards_min.setText(
            _translate("MainWindow", "0")
        )
        self.label_download_data_time_backwards_max.setText(
            _translate("MainWindow", "30")
        )
        self.label_download_data_backwards_value.setText(
            _translate("MainWindow", "Value: -0 days")
        )

    @staticmethod
    def set_dark_theme():
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        QApplication.instance().setPalette(dark_palette)


def run_main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec())
