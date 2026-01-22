from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QStandardItemModel


class StartTradeBuilder:
    def __init__(self):
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

        self.horizontal_layout_22 = None
        self.horizontal_layout_21 = None
        self.vertical_layout_13 = None
        self.horizontal_layout_20 = None
        self.vertical_layout_12 = None
        self.vertical_layout_11 = None
        self.horizontal_layout_15 = None
        self.horizontal_layout_16 = None
        self.horizontal_layout_17 = None
        self.horizontal_layout_18 = None
        self.horizontal_layout_19 = None

    def start_trade_setup(self):
        self.start_trade_stacked_widget = QtWidgets.QWidget()
        self.start_trade_stacked_widget.setObjectName("startTradeStackedWidget")
        self.horizontal_layout_22 = QtWidgets.QHBoxLayout(
            self.start_trade_stacked_widget
        )
        self.horizontal_layout_22.setObjectName("horizontalLayout_22")
        self.horizontal_layout_21 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_21.setObjectName("horizontalLayout_21")
        spacer_item10 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_21.addItem(spacer_item10)
        self.vertical_layout_13 = QtWidgets.QVBoxLayout()
        self.vertical_layout_13.setObjectName("verticalLayout_13")
        spacer_item11 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_13.addItem(spacer_item11)
        self.horizontal_layout_20 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_20.setObjectName("horizontalLayout_20")
        self.vertical_layout_12 = QtWidgets.QVBoxLayout()
        self.vertical_layout_12.setObjectName("verticalLayout_12")
        self.vertical_layout_11 = QtWidgets.QVBoxLayout()
        self.vertical_layout_11.setObjectName("verticalLayout_11")
        self.radio_button_start_trade_buy = QtWidgets.QRadioButton(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radio_button_start_trade_buy.setFont(font)
        self.radio_button_start_trade_buy.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_start_trade_buy.setStyleSheet("color: white;")
        self.radio_button_start_trade_buy.setChecked(True)
        self.radio_button_start_trade_buy.setObjectName("radioButtonStartTradeBuy")
        self.vertical_layout_11.addWidget(self.radio_button_start_trade_buy)
        self.radio_button_start_trade_sell = QtWidgets.QRadioButton(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radio_button_start_trade_sell.setFont(font)
        self.radio_button_start_trade_sell.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_start_trade_sell.setStyleSheet("color: white;")
        self.radio_button_start_trade_sell.setObjectName("radioButtonStartTradeSell")
        self.vertical_layout_11.addWidget(self.radio_button_start_trade_sell)
        self.radio_button_start_trade_close = QtWidgets.QRadioButton(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radio_button_start_trade_close.setFont(font)
        self.radio_button_start_trade_close.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.radio_button_start_trade_close.setStyleSheet("color: white;")
        self.radio_button_start_trade_close.setObjectName("radioButtonStartTradeClose")
        self.vertical_layout_11.addWidget(self.radio_button_start_trade_close)
        spacer_item12 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_11.addItem(spacer_item12)
        self.vertical_layout_12.addLayout(self.vertical_layout_11)
        self.horizontal_layout_15 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_15.setObjectName("horizontalLayout_15")
        self.label_start_trade_symbol = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_symbol.setFont(font)
        self.label_start_trade_symbol.setStyleSheet("color: white;")
        self.label_start_trade_symbol.setObjectName("labelStartTradeSymbol")
        self.horizontal_layout_15.addWidget(self.label_start_trade_symbol)
        spacer_item13 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_15.addItem(spacer_item13)
        self.line_edit_start_trade_symbol = QtWidgets.QLineEdit(
            parent=self.start_trade_stacked_widget
        )
        self.line_edit_start_trade_symbol.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_start_trade_symbol.setFont(font)
        self.line_edit_start_trade_symbol.setStyleSheet(
            "QLineEdit {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid transparent;\n"
            "            }\n"
            "            QLineEdit:hover {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid rgb(0, 0, 0);\n"
            "            }"
        )
        self.line_edit_start_trade_symbol.setObjectName("lineEditStartTradeSymbol")
        self.horizontal_layout_15.addWidget(self.line_edit_start_trade_symbol)
        self.vertical_layout_12.addLayout(self.horizontal_layout_15)
        self.horizontal_layout_16 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_16.setObjectName("horizontalLayout_16")
        self.label_start_trade_volume = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_volume.setFont(font)
        self.label_start_trade_volume.setStyleSheet("color: white;")
        self.label_start_trade_volume.setObjectName("labelStartTradeVolume")
        self.horizontal_layout_16.addWidget(self.label_start_trade_volume)
        spacer_item14 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_16.addItem(spacer_item14)
        self.line_edit_start_trade_volume = QtWidgets.QLineEdit(
            parent=self.start_trade_stacked_widget
        )
        self.line_edit_start_trade_volume.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_start_trade_volume.setFont(font)
        self.line_edit_start_trade_volume.setStyleSheet(
            "QLineEdit {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid transparent;\n"
            "            }\n"
            "            QLineEdit:hover {\n"
            "                color: white;\\n\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid rgb(0, 0, 0);\n"
            "            }"
        )
        self.line_edit_start_trade_volume.setObjectName("lineEditStartTradeVolume")
        self.horizontal_layout_16.addWidget(self.line_edit_start_trade_volume)
        self.vertical_layout_12.addLayout(self.horizontal_layout_16)
        self.horizontal_layout_17 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_17.setObjectName("horizontalLayout_17")

        self.label_start_trade_stop_loss = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_stop_loss.setFont(font)
        self.label_start_trade_stop_loss.setStyleSheet("color: white;")
        self.label_start_trade_stop_loss.setObjectName("labelStartTradeStopLoss")
        self.horizontal_layout_17.addWidget(self.label_start_trade_stop_loss)
        spacer_item15 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_17.addItem(spacer_item15)

        self.line_edit_start_trade_stop_loss = QtWidgets.QLineEdit(
            parent=self.start_trade_stacked_widget
        )
        self.line_edit_start_trade_stop_loss.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_start_trade_stop_loss.setFont(font)
        self.line_edit_start_trade_stop_loss.setStyleSheet(
            "QLineEdit {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid transparent;\n"
            "            }\n"
            "            QLineEdit:hover {\n"
            "                color: white;\\n\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid rgb(0, 0, 0);\n"
            "            }"
        )
        self.line_edit_start_trade_stop_loss.setObjectName("lineEditStartTradeStopLoss")
        self.horizontal_layout_17.addWidget(self.line_edit_start_trade_stop_loss)

        self.vertical_layout_12.addLayout(self.horizontal_layout_17)
        self.horizontal_layout_18 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_18.setObjectName("horizontalLayout_18")

        self.label_start_trade_take_profit = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_take_profit.setFont(font)
        self.label_start_trade_take_profit.setStyleSheet("color: white;")
        self.label_start_trade_take_profit.setObjectName("labelStartTradeTakeProfit")
        self.horizontal_layout_18.addWidget(self.label_start_trade_take_profit)
        spacer_item16 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_18.addItem(spacer_item16)
        self.line_edit_start_trade_take_profit = QtWidgets.QLineEdit(
            parent=self.start_trade_stacked_widget
        )
        self.line_edit_start_trade_take_profit.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_start_trade_take_profit.setFont(font)
        self.line_edit_start_trade_take_profit.setStyleSheet(
            "QLineEdit {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid transparent;\n"
            "            }\n"
            "            QLineEdit:hover {\n"
            "                color: white;\\n\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid rgb(0, 0, 0);\n"
            "            }"
        )
        self.line_edit_start_trade_take_profit.setObjectName(
            "lineEditStartTradeTakeProfit"
        )
        self.horizontal_layout_18.addWidget(self.line_edit_start_trade_take_profit)

        self.vertical_layout_12.addLayout(self.horizontal_layout_18)
        self.horizontal_layout_19 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_19.setObjectName("horizontalLayout_19")
        self.label_start_trade_comment = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_comment.setFont(font)
        self.label_start_trade_comment.setStyleSheet("color: white;")
        self.label_start_trade_comment.setObjectName("labelStartTradeComment")
        self.horizontal_layout_19.addWidget(self.label_start_trade_comment)
        spacer_item17 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_19.addItem(spacer_item17)
        self.line_edit_start_trade_comment = QtWidgets.QLineEdit(
            parent=self.start_trade_stacked_widget
        )
        self.line_edit_start_trade_comment.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_start_trade_comment.setFont(font)
        self.line_edit_start_trade_comment.setStyleSheet(
            "QLineEdit {\n"
            "                color: white;\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid transparent;\n"
            "            }\n"
            "            QLineEdit:hover {\n"
            "                color: white;\\n\n"
            "                border-radius: 10px;\n"
            "                background-color: rgb(54, 54, 54);\n"
            "                border: 2px solid rgb(0, 0, 0);\n"
            "            }"
        )
        self.line_edit_start_trade_comment.setObjectName("lineEditStartTradeComment")
        self.horizontal_layout_19.addWidget(self.line_edit_start_trade_comment)
        self.vertical_layout_12.addLayout(self.horizontal_layout_19)
        spacer_item18 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_12.addItem(spacer_item18)
        self.push_button_start_trade = QtWidgets.QPushButton(
            parent=self.start_trade_stacked_widget
        )
        self.push_button_start_trade.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_start_trade.setFont(font)
        self.push_button_start_trade.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_start_trade.setStyleSheet(
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
        self.push_button_start_trade.setObjectName("pushButtonStartTrade")
        self.vertical_layout_12.addWidget(self.push_button_start_trade)
        self.label_start_trade_error = QtWidgets.QLabel(
            parent=self.start_trade_stacked_widget
        )
        self.label_start_trade_error.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_start_trade_error.setFont(font)
        self.label_start_trade_error.setStyleSheet("color: red;")
        self.label_start_trade_error.setObjectName("labelStartTradeError")
        self.vertical_layout_12.addWidget(
            self.label_start_trade_error, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.horizontal_layout_20.addLayout(self.vertical_layout_12)
        spacer_item19 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_20.addItem(spacer_item19)
        self.table_view_start_trade = QtWidgets.QTableView(
            parent=self.start_trade_stacked_widget
        )
        self.table_view_start_trade.setMinimumSize(QtCore.QSize(435, 0))
        self.table_view_start_trade.setMaximumSize(QtCore.QSize(800, 20000))
        self.table_view_start_trade.setStyleSheet(
            "background-color: rgb(100, 100, 100);"
        )
        self.table_view_start_trade.setObjectName("tableViewStartTrade")
        self.horizontal_layout_20.addWidget(self.table_view_start_trade)
        self.vertical_layout_13.addLayout(self.horizontal_layout_20)

        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(
            ["Symbol", "Price", "B/S", "Vol", "SL", "TP", "Comment", "Profit"]
        )

        self.table_view_start_trade.setModel(self.table_model)
        self.table_view_start_trade.setColumnWidth(0, 55)
        self.table_view_start_trade.setColumnWidth(1, 50)
        self.table_view_start_trade.setColumnWidth(2, 38)
        self.table_view_start_trade.setColumnWidth(3, 25)
        self.table_view_start_trade.setColumnWidth(4, 48)
        self.table_view_start_trade.setColumnWidth(5, 48)
        self.table_view_start_trade.setColumnWidth(6, 100)
        self.table_view_start_trade.setColumnWidth(7, 49)

        spacer_item20 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_13.addItem(spacer_item20)
        self.horizontal_layout_21.addLayout(self.vertical_layout_13)
        spacer_item21 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_21.addItem(spacer_item21)
        self.horizontal_layout_22.addLayout(self.horizontal_layout_21)
