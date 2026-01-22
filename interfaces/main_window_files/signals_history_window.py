from PyQt6 import QtWidgets, QtGui


class SignalsHistoryBuilder:
    def __init__(self):
        self.signals_history_stacked_widget = None
        self.horizontal_layout_12 = None
        self.widget_signals_history_place = None

    def signals_history_setup(self):
        self.signals_history_stacked_widget = QtWidgets.QWidget()
        self.signals_history_stacked_widget.setObjectName("signalsHistoryStackedWidget")
        self.horizontal_layout_12 = QtWidgets.QHBoxLayout(
            self.signals_history_stacked_widget
        )
        self.horizontal_layout_12.setObjectName("horizontalLayout_12")
        self.widget_signals_history_place = QtWidgets.QLabel(
            parent=self.signals_history_stacked_widget
        )
        self.widget_signals_history_place.setText("")
        self.widget_signals_history_place.setPixmap(
            QtGui.QPixmap("charts\\all_linear_chart.png")
        )
        self.signals_history_stacked_widget.setStyleSheet("background-color: black;")
        self.widget_signals_history_place.setScaledContents(True)
        self.widget_signals_history_place.setObjectName("widgetSignalsHistoryPlace")
        self.horizontal_layout_12.addWidget(self.widget_signals_history_place)
