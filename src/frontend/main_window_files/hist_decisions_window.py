"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtWidgets, QtGui


class HistDecisionBuilder:
    """
    This class is responsible for creating tab for historical decisions chart.
    """

    def __init__(self) -> None:
        self.hist_decisions_stacked_widget = None
        self.widget_hist_decision_place = None

        self.horizontal_layout_13 = None

    def hist_decision_setup(self) -> None:
        """
        This method is responsible for creating tab content.
        :return: nothing.
        """
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
            QtGui.QPixmap("src\\charts\\histogram_chart.png")
        )
        self.widget_hist_decision_place.setScaledContents(True)
        self.widget_hist_decision_place.setStyleSheet("background-color: black;")
        self.widget_hist_decision_place.setObjectName("widgetHistDecisionPlace")
        self.horizontal_layout_13.addWidget(self.widget_hist_decision_place)
