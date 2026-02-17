"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class BigLeftFrameBuilder:
    """
    This class is responsible for creating a wide navigation menu located on the left side of the main
    application window.
    """

    def __init__(self, central_widget) -> None:
        self.central_widget = central_widget
        self.big_left_frame = None
        self.button_big_show_menu = None
        self.button_big_download_data = None
        self.button_big_candle_chart = None
        self.button_big_signals_history = None
        self.button_big_hist_decisions = None
        self.button_big_linear_decisions = None
        self.button_big_start_trade = None
        self.button_big_exit_application = None

        self.vertical_layout_2 = None
        self.vertical_layout_5 = None

    def big_left_frame_setup(self, icons) -> None:
        """
        This method is responsible for create navigation menu content.
        :param icons: menu icons.
        :return: nothing.
        """
        self.big_left_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.big_left_frame.setMinimumSize(QtCore.QSize(160, 350))
        self.big_left_frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.big_left_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.big_left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.big_left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.big_left_frame.setObjectName("bigLeftFrame")
        self.vertical_layout_5 = QtWidgets.QVBoxLayout(self.big_left_frame)
        self.vertical_layout_5.setContentsMargins(3, 3, 3, 3)
        self.vertical_layout_5.setObjectName("verticalLayout_5")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setSpacing(12)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.button_big_show_menu = QtWidgets.QPushButton(parent=self.big_left_frame)
        self.button_big_show_menu.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_show_menu.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_show_menu.setFont(font)
        self.button_big_show_menu.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_show_menu.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_show_menu.setIcon(icons["icon1"])
        self.button_big_show_menu.setIconSize(QtCore.QSize(30, 30))
        self.button_big_show_menu.setCheckable(True)
        self.button_big_show_menu.setAutoExclusive(True)
        self.button_big_show_menu.setObjectName("pushButtonBigShowMenu")
        self.vertical_layout_2.addWidget(self.button_big_show_menu)
        spacer_item36 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_2.addItem(spacer_item36)
        self.button_big_download_data = QtWidgets.QPushButton(
            parent=self.big_left_frame
        )
        self.button_big_download_data.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_download_data.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_download_data.setFont(font)
        self.button_big_download_data.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_download_data.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_download_data.setIcon(icons["icon2"])
        self.button_big_download_data.setIconSize(QtCore.QSize(30, 30))
        self.button_big_download_data.setCheckable(True)
        self.button_big_download_data.setAutoExclusive(True)
        self.button_big_download_data.setObjectName("pushButtonBigDownloadData")
        self.vertical_layout_2.addWidget(self.button_big_download_data)
        self.button_big_candle_chart = QtWidgets.QPushButton(parent=self.big_left_frame)
        self.button_big_candle_chart.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_candle_chart.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_candle_chart.setFont(font)
        self.button_big_candle_chart.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_candle_chart.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_candle_chart.setIcon(icons["icon3"])
        self.button_big_candle_chart.setIconSize(QtCore.QSize(30, 30))
        self.button_big_candle_chart.setCheckable(True)
        self.button_big_candle_chart.setAutoExclusive(True)
        self.button_big_candle_chart.setObjectName("pushButtonBigCandleChart")
        self.vertical_layout_2.addWidget(self.button_big_candle_chart)
        self.button_big_signals_history = QtWidgets.QPushButton(
            parent=self.big_left_frame
        )
        self.button_big_signals_history.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_signals_history.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_signals_history.setFont(font)
        self.button_big_signals_history.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_signals_history.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_signals_history.setIcon(icons["icon4"])
        self.button_big_signals_history.setIconSize(QtCore.QSize(30, 30))
        self.button_big_signals_history.setCheckable(True)
        self.button_big_signals_history.setAutoExclusive(True)
        self.button_big_signals_history.setObjectName("pushButtonBigSignalsHistory")
        self.vertical_layout_2.addWidget(self.button_big_signals_history)
        self.button_big_hist_decisions = QtWidgets.QPushButton(
            parent=self.big_left_frame
        )
        self.button_big_hist_decisions.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_hist_decisions.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_hist_decisions.setFont(font)
        self.button_big_hist_decisions.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_hist_decisions.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_hist_decisions.setIcon(icons["icon5"])
        self.button_big_hist_decisions.setIconSize(QtCore.QSize(30, 30))
        self.button_big_hist_decisions.setCheckable(True)
        self.button_big_hist_decisions.setAutoExclusive(True)
        self.button_big_hist_decisions.setObjectName("pushButtonBigHistDecisions")
        self.vertical_layout_2.addWidget(self.button_big_hist_decisions)
        self.button_big_linear_decisions = QtWidgets.QPushButton(
            parent=self.big_left_frame
        )
        self.button_big_linear_decisions.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_linear_decisions.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_linear_decisions.setFont(font)
        self.button_big_linear_decisions.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_linear_decisions.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_linear_decisions.setIcon(icons["icon6"])
        self.button_big_linear_decisions.setIconSize(QtCore.QSize(30, 30))
        self.button_big_linear_decisions.setCheckable(True)
        self.button_big_linear_decisions.setAutoExclusive(True)
        self.button_big_linear_decisions.setObjectName("pushButtonBigLinearDecisions")
        self.vertical_layout_2.addWidget(self.button_big_linear_decisions)
        self.button_big_start_trade = QtWidgets.QPushButton(parent=self.big_left_frame)
        self.button_big_start_trade.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_start_trade.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_start_trade.setFont(font)
        self.button_big_start_trade.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_start_trade.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_start_trade.setIcon(icons["icon7"])
        self.button_big_start_trade.setIconSize(QtCore.QSize(30, 30))
        self.button_big_start_trade.setCheckable(True)
        self.button_big_start_trade.setAutoExclusive(True)
        self.button_big_start_trade.setObjectName("pushButtonBigStartTrade")
        self.vertical_layout_2.addWidget(self.button_big_start_trade)
        spacer_item37 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_2.addItem(spacer_item37)
        spacer_item38 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_2.addItem(spacer_item38)
        self.button_big_exit_application = QtWidgets.QPushButton(
            parent=self.big_left_frame
        )
        self.button_big_exit_application.setMinimumSize(QtCore.QSize(120, 50))
        self.button_big_exit_application.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_big_exit_application.setFont(font)
        self.button_big_exit_application.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.button_big_exit_application.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70,70);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.button_big_exit_application.setIcon(icons["icon8"])
        self.button_big_exit_application.setIconSize(QtCore.QSize(30, 30))
        self.button_big_exit_application.setCheckable(True)
        self.button_big_exit_application.setAutoExclusive(True)
        self.button_big_exit_application.setObjectName("pushButtonBigExitApplication")
        self.vertical_layout_2.addWidget(self.button_big_exit_application)
        self.vertical_layout_5.addLayout(self.vertical_layout_2)
