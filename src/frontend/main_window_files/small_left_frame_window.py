"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class SmallLeftFrameBuilder:
    """
    This class is responsible for create smaller version of left navigation application menu.
    """

    def __init__(self, central_widget) -> None:
        self.centralWidget = central_widget
        self.small_left_frame = None
        self.push_button_small_show_menu = None
        self.push_button_small_download = None
        self.push_button_small_candle_chart = None
        self.push_button_small_signals_history = None
        self.push_button_small_hist_decisions = None
        self.push_button_small_linear_decisions = None
        self.push_button_small_start_trade = None
        self.push_button_small_exit_application = None

        self.vertical_layout_4 = None
        self.vertical_layout = None

    def small_left_frame_setup(self) -> None:
        """
        This method is responsible for create left frame content.
        :return: nothing.
        """
        self.small_left_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.small_left_frame.setMinimumSize(QtCore.QSize(60, 475))
        self.small_left_frame.setMaximumSize(QtCore.QSize(60, 16777215))
        self.small_left_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.small_left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.small_left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.small_left_frame.setObjectName("smallLeftFrame")
        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self.small_left_frame)
        self.vertical_layout_4.setContentsMargins(3, 3, 3, 3)
        self.vertical_layout_4.setObjectName("verticalLayout_4")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setSpacing(12)
        self.vertical_layout.setObjectName("verticalLayout")
        self.push_button_small_show_menu = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_show_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_show_menu.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_show_menu.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_show_menu.setStyleSheet(
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
        self.push_button_small_show_menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("src\\assets\\menuIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_show_menu.setIcon(icon1)
        self.push_button_small_show_menu.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_show_menu.setCheckable(True)
        self.push_button_small_show_menu.setAutoExclusive(True)
        self.push_button_small_show_menu.setObjectName("pushButtonSmallShowMenu")
        self.vertical_layout.addWidget(self.push_button_small_show_menu)
        spacer_item33 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item33)
        self.push_button_small_download = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_download.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_download.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_download.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_download.setStyleSheet(
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
        self.push_button_small_download.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("src\\assets\\downloadIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_download.setIcon(icon2)
        self.push_button_small_download.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_download.setCheckable(True)
        self.push_button_small_download.setAutoExclusive(True)
        self.push_button_small_download.setObjectName("pushButtonSmallDownload")
        self.vertical_layout.addWidget(self.push_button_small_download)
        self.push_button_small_candle_chart = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_candle_chart.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_candle_chart.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_candle_chart.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_candle_chart.setStyleSheet(
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
        self.push_button_small_candle_chart.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("src\\assets\\candleStickIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_candle_chart.setIcon(icon3)
        self.push_button_small_candle_chart.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_candle_chart.setCheckable(True)
        self.push_button_small_candle_chart.setAutoExclusive(True)
        self.push_button_small_candle_chart.setObjectName("pushButtonSmallCandleChart")
        self.vertical_layout.addWidget(self.push_button_small_candle_chart)
        self.push_button_small_signals_history = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_signals_history.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_signals_history.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_signals_history.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_signals_history.setStyleSheet(
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
        self.push_button_small_signals_history.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("src\\assets\\historyDecisionIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_signals_history.setIcon(icon4)
        self.push_button_small_signals_history.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_signals_history.setCheckable(True)
        self.push_button_small_signals_history.setAutoExclusive(True)
        self.push_button_small_signals_history.setObjectName(
            "pushButtonSmallSignalsHistory"
        )
        self.vertical_layout.addWidget(self.push_button_small_signals_history)
        self.push_button_small_hist_decisions = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_hist_decisions.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_hist_decisions.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_hist_decisions.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_hist_decisions.setStyleSheet(
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
        self.push_button_small_hist_decisions.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("src\\assets\\histPlotIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_hist_decisions.setIcon(icon5)
        self.push_button_small_hist_decisions.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_hist_decisions.setCheckable(True)
        self.push_button_small_hist_decisions.setAutoExclusive(True)
        self.push_button_small_hist_decisions.setObjectName(
            "pushButtonSmallHistDecisions"
        )
        self.vertical_layout.addWidget(self.push_button_small_hist_decisions)
        self.push_button_small_linear_decisions = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_linear_decisions.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_linear_decisions.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_linear_decisions.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_linear_decisions.setStyleSheet(
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
        self.push_button_small_linear_decisions.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("src\\assets\\linearPlotIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_linear_decisions.setIcon(icon6)
        self.push_button_small_linear_decisions.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_linear_decisions.setCheckable(True)
        self.push_button_small_linear_decisions.setAutoExclusive(True)
        self.push_button_small_linear_decisions.setObjectName(
            "pushButtonSmallLinearDecisions"
        )
        self.vertical_layout.addWidget(self.push_button_small_linear_decisions)
        self.push_button_small_start_trade = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_start_trade.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_start_trade.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_start_trade.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_start_trade.setStyleSheet(
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
        self.push_button_small_start_trade.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("src\\assets\\shopIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_start_trade.setIcon(icon7)
        self.push_button_small_start_trade.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_start_trade.setCheckable(True)
        self.push_button_small_start_trade.setAutoExclusive(True)
        self.push_button_small_start_trade.setObjectName("pushButtonSmallStartTrade")
        self.vertical_layout.addWidget(self.push_button_small_start_trade)
        spacer_item34 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item34)
        spacer_item35 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item35)
        self.push_button_small_exit_application = QtWidgets.QPushButton(
            parent=self.small_left_frame
        )
        self.push_button_small_exit_application.setMinimumSize(QtCore.QSize(50, 50))
        self.push_button_small_exit_application.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_small_exit_application.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_small_exit_application.setStyleSheet(
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
        self.push_button_small_exit_application.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("src\\assets\\exitIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_small_exit_application.setIcon(icon8)
        self.push_button_small_exit_application.setIconSize(QtCore.QSize(30, 30))
        self.push_button_small_exit_application.setCheckable(True)
        self.push_button_small_exit_application.setAutoExclusive(True)
        self.push_button_small_exit_application.setObjectName(
            "pushButtonSmallExitApplication"
        )
        self.vertical_layout.addWidget(self.push_button_small_exit_application)
        self.vertical_layout_4.addLayout(self.vertical_layout)
        icons = dict(
            icon1=icon1,
            icon2=icon2,
            icon3=icon3,
            icon4=icon4,
            icon5=icon5,
            icon6=icon6,
            icon7=icon7,
            icon8=icon8,
        )
        return icons
