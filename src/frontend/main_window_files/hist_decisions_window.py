from PyQt6 import QtWidgets, QtGui


class HistDecisionBuilder:
    def __init__(self):
        self.hist_decisions_stacked_widget = None
        self.widget_hist_decision_place = None

        self.horizontal_layout_13 = None

    def hist_decision_setup(self):
        self.hist_decisions_stacked_widget = QtWidgets.QWidget()
        self.hist_decisions_stacked_widget.setStyleSheet("background-color: black;")
        self.hist_decisions_stacked_widget.setObjectName("histDecisionsStackedWidget")
        self.horizontal_layout_13 = QtWidgets.QHBoxLayout(
            self.hist_decisions_stacked_widget
        )
        self.horizontal_layout_13.setObjectName("horizontalLayout_13")
        self.widget_hist_decision_place = QtWidgets.QLabel(
            parent=self.hist_decisions_stacked_widget
        )
        self.widget_hist_decision_place.setText("")
        self.widget_hist_decision_place.setPixmap(
            QtGui.QPixmap("charts\\histogram_chart.png")
        )
        self.widget_hist_decision_place.setScaledContents(True)
        self.widget_hist_decision_place.setStyleSheet("background-color: black;")
        self.widget_hist_decision_place.setObjectName("widgetHistDecisionPlace")
        self.horizontal_layout_13.addWidget(self.widget_hist_decision_place)
