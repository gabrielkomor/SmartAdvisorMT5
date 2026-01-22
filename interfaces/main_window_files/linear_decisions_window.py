from PyQt6 import QtWidgets, QtGui


class LinearDecisionsBuilder:
    def __init__(self):
        self.linear_decisions_stacked_widget = None
        self.widget_linear_decisions_place = None

        self.horizontal_layout_14 = None

    def linear_decisions_setup(self):
        self.linear_decisions_stacked_widget = QtWidgets.QWidget()
        self.linear_decisions_stacked_widget.setStyleSheet("background-color: black;")
        self.linear_decisions_stacked_widget.setObjectName(
            "linearDecisionsStackedWidget"
        )
        self.horizontal_layout_14 = QtWidgets.QHBoxLayout(
            self.linear_decisions_stacked_widget
        )
        self.horizontal_layout_14.setObjectName("horizontalLayout_14")
        self.widget_linear_decisions_place = QtWidgets.QLabel(
            parent=self.linear_decisions_stacked_widget
        )
        self.widget_linear_decisions_place.setText("")
        self.widget_linear_decisions_place.setPixmap(
            QtGui.QPixmap("charts\\linear_chart.png")
        )
        self.widget_linear_decisions_place.setScaledContents(True)
        self.widget_linear_decisions_place.setStyleSheet(
            "background-color: rgb(0, 0, 0);"
        )
        self.widget_linear_decisions_place.setObjectName("widgetLinearDecisionsPlace")
        self.horizontal_layout_14.addWidget(self.widget_linear_decisions_place)
