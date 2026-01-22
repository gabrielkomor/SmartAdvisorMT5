from PyQt6 import QtWidgets, QtGui, QtCore


class DownloadDataBuilder:
    def __init__(self):
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

        self.horizontal_layout_10 = None
        self.vertical_layout_10 = None
        self.horizontal_layout_9 = None
        self.vertical_layout_9 = None
        self.vertical_layout_8 = None
        self.horizontal_layout_6 = None
        self.horizontal_layout_7 = None
        self.vertical_layout_7 = None
        self.horizontal_layout_8 = None
        self.horizontal_layout_slider2 = None

    def download_data_setup(self):
        self.download_data_stacked_widget = QtWidgets.QWidget()
        self.download_data_stacked_widget.setObjectName("downloadDataStackedWidget")
        self.horizontal_layout_10 = QtWidgets.QHBoxLayout(
            self.download_data_stacked_widget
        )
        self.horizontal_layout_10.setObjectName("horizontalLayout_10")
        self.vertical_layout_10 = QtWidgets.QVBoxLayout()
        self.vertical_layout_10.setObjectName("verticalLayout_10")
        spacer_item = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_10.addItem(spacer_item)
        self.horizontal_layout_9 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_9.setObjectName("horizontalLayout_9")
        spacer_item1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_9.addItem(spacer_item1)
        self.vertical_layout_9 = QtWidgets.QVBoxLayout()
        self.vertical_layout_9.setObjectName("verticalLayout_9")
        self.vertical_layout_8 = QtWidgets.QVBoxLayout()
        self.vertical_layout_8.setObjectName("verticalLayout_8")
        self.radio_button_download_data_forex = QtWidgets.QRadioButton(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radio_button_download_data_forex.setFont(font)
        self.radio_button_download_data_forex.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_download_data_forex.setStyleSheet("color: white;")
        self.radio_button_download_data_forex.setChecked(True)
        self.radio_button_download_data_forex.setObjectName(
            "radioButtonDownloadDataForex"
        )
        self.vertical_layout_8.addWidget(self.radio_button_download_data_forex)
        self.radio_button_download_data_stock = QtWidgets.QRadioButton(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radio_button_download_data_stock.setFont(font)
        self.radio_button_download_data_stock.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_download_data_stock.setStyleSheet("color: white;")
        self.radio_button_download_data_stock.setObjectName(
            "radioButtonDownloadDataStock"
        )
        self.vertical_layout_8.addWidget(self.radio_button_download_data_stock)
        self.radio_button_download_data_etf = QtWidgets.QRadioButton(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.radio_button_download_data_etf.setFont(font)
        self.radio_button_download_data_etf.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_download_data_etf.setStyleSheet("color: white;")
        self.radio_button_download_data_etf.setObjectName("radioButtonDownloadDataETF")
        self.vertical_layout_8.addWidget(self.radio_button_download_data_etf)
        spacer_item2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_8.addItem(spacer_item2)
        self.vertical_layout_9.addLayout(self.vertical_layout_8)
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_6.setObjectName("horizontalLayout_6")
        self.label_download_data_symbol = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_symbol.setFont(font)
        self.label_download_data_symbol.setStyleSheet("color: white;")
        self.label_download_data_symbol.setObjectName("labelDownloadDataSymbol")
        self.horizontal_layout_6.addWidget(self.label_download_data_symbol)
        spacer_item3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_6.addItem(spacer_item3)
        self.combo_box_download_data_symbol = QtWidgets.QComboBox(
            parent=self.download_data_stacked_widget
        )
        self.combo_box_download_data_symbol.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.combo_box_download_data_symbol.setFont(font)
        self.combo_box_download_data_symbol.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.combo_box_download_data_symbol.setStyleSheet(
            "color: white;\n" "background-color: rgb(90, 90, 90);"
        )
        self.combo_box_download_data_symbol.setObjectName("comboBoxDownloadDataSymbol")
        self.combo_box_download_data_symbol.addItem("")
        self.combo_box_download_data_symbol.addItem("")
        self.horizontal_layout_6.addWidget(self.combo_box_download_data_symbol)
        self.vertical_layout_9.addLayout(self.horizontal_layout_6)
        spacer_item4 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_9.addItem(spacer_item4)
        self.horizontal_layout_7 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_7.setObjectName("horizontalLayout_7")
        self.label_download_data_time_frame = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_time_frame.setFont(font)
        self.label_download_data_time_frame.setStyleSheet("color: white;")
        self.label_download_data_time_frame.setObjectName("labelDownloadDataTimeFrame")
        self.horizontal_layout_7.addWidget(self.label_download_data_time_frame)
        spacer_item5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_7.addItem(spacer_item5)
        self.combo_box_download_data_time_frame = QtWidgets.QComboBox(
            parent=self.download_data_stacked_widget
        )
        self.combo_box_download_data_time_frame.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.combo_box_download_data_time_frame.setFont(font)
        self.combo_box_download_data_time_frame.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.combo_box_download_data_time_frame.setStyleSheet(
            "color: white;\n" "background-color: rgb(90, 90, 90);"
        )
        self.combo_box_download_data_time_frame.setObjectName(
            "comboBoxDownloadDataTimeFrame"
        )
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.combo_box_download_data_time_frame.addItem("")
        self.horizontal_layout_7.addWidget(self.combo_box_download_data_time_frame)
        self.vertical_layout_9.addLayout(self.horizontal_layout_7)
        spacer_item6 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_9.addItem(spacer_item6)
        self.vertical_layout_7 = QtWidgets.QVBoxLayout()
        self.vertical_layout_7.setObjectName("verticalLayout_7")
        self.label_download_data_time_delta = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_time_delta.setFont(font)
        self.label_download_data_time_delta.setStyleSheet("color: white;")
        self.label_download_data_time_delta.setObjectName("labelDownloadDataTimeDelta")
        self.vertical_layout_7.addWidget(self.label_download_data_time_delta)
        self.horizontal_layout_8 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_8.setObjectName("horizontalLayout_8")
        self.label_download_data_time_delta_min = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        self.label_download_data_time_delta_min.setFont(font)
        self.label_download_data_time_delta_min.setStyleSheet("color: white;")
        self.label_download_data_time_delta_min.setObjectName(
            "labelDownloadDataTimeDeltaMin"
        )
        self.horizontal_layout_8.addWidget(self.label_download_data_time_delta_min)
        self.horizontal_slider_download_data_td = QtWidgets.QSlider(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setPointSize(12)
        self.horizontal_slider_download_data_td.setFont(font)
        self.horizontal_slider_download_data_td.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor)
        )
        self.horizontal_slider_download_data_td.setOrientation(
            QtCore.Qt.Orientation.Horizontal
        )
        self.horizontal_slider_download_data_td.setObjectName(
            "horizontalSliderDownloadDataTD"
        )
        self.horizontal_layout_8.addWidget(self.horizontal_slider_download_data_td)
        self.label_download_data_time_delta_max = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_time_delta_max.setFont(font)
        self.label_download_data_time_delta_max.setStyleSheet("color: white;")
        self.label_download_data_time_delta_max.setObjectName(
            "labelDownloadDataTimeDeltaMax"
        )
        self.horizontal_layout_8.addWidget(self.label_download_data_time_delta_max)
        self.vertical_layout_7.addLayout(self.horizontal_layout_8)
        self.vertical_layout_9.addLayout(self.vertical_layout_7)
        self.label_download_data_value_slider = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_value_slider.setFont(font)
        self.label_download_data_value_slider.setStyleSheet("color: white;")
        self.label_download_data_value_slider.setObjectName(
            "labelDownloadDataValueSlider"
        )
        self.vertical_layout_9.addWidget(self.label_download_data_value_slider)
        spacer_item7 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_9.addItem(spacer_item7)

        self.label_download_data_time_backwards = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        self.label_download_data_time_backwards.setFont(font)
        self.label_download_data_time_backwards.setStyleSheet("color: white;")
        self.vertical_layout_9.addWidget(self.label_download_data_time_backwards)
        self.horizontal_layout_slider2 = QtWidgets.QHBoxLayout()
        self.label_download_data_time_backwards_min = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        self.label_download_data_time_backwards_min.setFont(font)
        self.label_download_data_time_backwards_min.setStyleSheet("color: white;")
        self.horizontal_layout_slider2.addWidget(
            self.label_download_data_time_backwards_min
        )
        self.horizontal_slider_download_data_tb = QtWidgets.QSlider(
            QtCore.Qt.Orientation.Horizontal, parent=self.download_data_stacked_widget
        )
        self.horizontal_slider_download_data_tb.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor)
        )
        self.horizontal_slider_download_data_tb.setMinimum(0)
        self.horizontal_slider_download_data_tb.setMaximum(30)
        self.horizontal_slider_download_data_tb.setValue(0)
        self.horizontal_slider_download_data_tb.setObjectName("slider2")
        self.horizontal_layout_slider2.addWidget(
            self.horizontal_slider_download_data_tb
        )
        self.label_download_data_time_backwards_max = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        self.label_download_data_time_backwards_max.setFont(font)
        self.label_download_data_time_backwards_max.setStyleSheet("color: white;")
        self.horizontal_layout_slider2.addWidget(
            self.label_download_data_time_backwards_max
        )
        self.vertical_layout_9.addLayout(self.horizontal_layout_slider2)
        self.label_download_data_backwards_value = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        self.label_download_data_backwards_value.setFont(font)
        self.label_download_data_backwards_value.setStyleSheet("color: white;")
        self.vertical_layout_9.addWidget(self.label_download_data_backwards_value)
        spacer_item10 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_9.addItem(spacer_item10)
        self.push_button_download_data_dd = QtWidgets.QPushButton(
            parent=self.download_data_stacked_widget
        )
        self.push_button_download_data_dd.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_download_data_dd.setFont(font)
        self.push_button_download_data_dd.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_download_data_dd.setStyleSheet(
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
        self.push_button_download_data_dd.setObjectName("pushButtonDownloadDataDD")
        self.vertical_layout_9.addWidget(self.push_button_download_data_dd)
        self.label_download_data_success = QtWidgets.QLabel(
            parent=self.download_data_stacked_widget
        )
        self.label_download_data_success.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_data_success.setFont(font)
        self.label_download_data_success.setStyleSheet("color: red;")
        self.label_download_data_success.setObjectName("labelDownloadDataSuccess")
        self.vertical_layout_9.addWidget(
            self.label_download_data_success, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.horizontal_layout_9.addLayout(self.vertical_layout_9)
        spacer_item8 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_9.addItem(spacer_item8)
        self.vertical_layout_10.addLayout(self.horizontal_layout_9)
        spacer_item9 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_10.addItem(spacer_item9)
        self.horizontal_layout_10.addLayout(self.vertical_layout_10)
