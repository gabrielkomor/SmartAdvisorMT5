"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

import os

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QColor


class CandleChartBuilder:
    """
    This class is responsible for create candle chart widget for main window.
    """

    def __init__(self) -> None:
        self.candle_chart_stacked_widget = None
        self.horizontal_layout_11 = None
        self.widget_candle_chart_place = None

    def candle_chart_setup(self) -> None:
        """
        This method is responsible for creating candle chart window content.
        :return: nothing.
        """
        self.candle_chart_stacked_widget = QtWidgets.QWidget()
        self.candle_chart_stacked_widget.setStyleSheet(
            "background-color: rgb(0, 0, 0);"
        )
        self.candle_chart_stacked_widget.setObjectName("candleChartStackedWidget")
        self.horizontal_layout_11 = QtWidgets.QHBoxLayout(
            self.candle_chart_stacked_widget
        )
        self.horizontal_layout_11.setObjectName("horizontalLayout_11")
        self.widget_candle_chart_place = QWebEngineView(
            parent=self.candle_chart_stacked_widget
        )
        self.widget_candle_chart_place.page().setBackgroundColor(QColor(0, 0, 0))
        self.widget_candle_chart_place.setUrl(
            QUrl.fromLocalFile(os.path.abspath("src\\charts\\chart.html"))
        )
        self.widget_candle_chart_place.setObjectName("widgetCandleChartPlace")
        self.horizontal_layout_11.addWidget(self.widget_candle_chart_place)
