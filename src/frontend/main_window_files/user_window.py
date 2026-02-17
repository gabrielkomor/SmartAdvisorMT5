"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtWidgets, QtGui, QtCore


class UserWindowBuilder:
    """
    This class is responsible for create user tab in application main window.
    """

    def __init__(self) -> None:
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

        self.horizontal_layout_28 = None
        self.horizontal_layout_27 = None
        self.vertical_layout_14 = None
        self.horizontal_layout_23 = None
        self.horizontal_layout_24 = None
        self.horizontal_layout_25 = None
        self.horizontal_layout_26 = None

    def user_window_setup(self) -> None:
        """
        This method is responsible for create tab content.
        :return: nothing.
        """
        self.user_data_stacked_widget = QtWidgets.QWidget()
        self.user_data_stacked_widget.setObjectName("userDataStackedWidget")
        self.horizontal_layout_28 = QtWidgets.QHBoxLayout(self.user_data_stacked_widget)
        self.horizontal_layout_28.setObjectName("horizontalLayout_28")
        self.horizontal_layout_27 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_27.setObjectName("horizontalLayout_27")
        spacer_item22 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_27.addItem(spacer_item22)
        self.vertical_layout_14 = QtWidgets.QVBoxLayout()
        self.vertical_layout_14.setObjectName("verticalLayout_14")
        spacer_item23 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_14.addItem(spacer_item23)
        self.horizontal_layout_23 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_23.setObjectName("horizontalLayout_23")
        self.label_user_data_name = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_name.setFont(font)
        self.label_user_data_name.setStyleSheet("color: white;")
        self.label_user_data_name.setObjectName("labelUserDataName")
        self.horizontal_layout_23.addWidget(self.label_user_data_name)
        spacer_item24 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_23.addItem(spacer_item24)
        self.label_user_data_name_value = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_name_value.setFont(font)
        self.label_user_data_name_value.setStyleSheet("color: white;")
        self.label_user_data_name_value.setObjectName("labelUserDataNameValue")
        self.horizontal_layout_23.addWidget(self.label_user_data_name_value)
        self.vertical_layout_14.addLayout(self.horizontal_layout_23)
        self.horizontal_layout_24 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_24.setObjectName("horizontalLayout_24")
        self.label_user_data_balance = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_balance.setFont(font)
        self.label_user_data_balance.setStyleSheet("color: white;")
        self.label_user_data_balance.setObjectName("labelUserDataBalance")
        self.horizontal_layout_24.addWidget(self.label_user_data_balance)
        spacer_item25 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_24.addItem(spacer_item25)
        self.label_user_data_balance_value = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_balance_value.setFont(font)
        self.label_user_data_balance_value.setStyleSheet("color: white;")
        self.label_user_data_balance_value.setObjectName("labelUserDataBalanceValue")
        self.horizontal_layout_24.addWidget(self.label_user_data_balance_value)
        self.vertical_layout_14.addLayout(self.horizontal_layout_24)
        self.horizontal_layout_25 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_25.setObjectName("horizontalLayout_25")
        self.label_user_data_profit = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_profit.setFont(font)
        self.label_user_data_profit.setStyleSheet("color: white;")
        self.label_user_data_profit.setObjectName("labelUserDataCredit")
        self.horizontal_layout_25.addWidget(self.label_user_data_profit)
        spacer_item26 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_25.addItem(spacer_item26)
        self.label_user_data_profit_value = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_profit_value.setFont(font)
        self.label_user_data_profit_value.setStyleSheet("color: white;")
        self.label_user_data_profit_value.setObjectName("labelUserDataCreditValue")
        self.horizontal_layout_25.addWidget(self.label_user_data_profit_value)
        self.vertical_layout_14.addLayout(self.horizontal_layout_25)
        self.horizontal_layout_26 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_26.setObjectName("horizontalLayout_26")
        self.label_user_data_equity = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_equity.setFont(font)
        self.label_user_data_equity.setStyleSheet("color: white;")
        self.label_user_data_equity.setObjectName("labelUserDataEquity")
        self.horizontal_layout_26.addWidget(self.label_user_data_equity)
        spacer_item27 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_26.addItem(spacer_item27)
        self.label_user_data_equity_value = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_equity_value.setFont(font)
        self.label_user_data_equity_value.setStyleSheet("color: white;")
        self.label_user_data_equity_value.setObjectName("labelUserDataEquityValue")
        self.horizontal_layout_26.addWidget(self.label_user_data_equity_value)
        self.vertical_layout_14.addLayout(self.horizontal_layout_26)
        spacer_item28 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_14.addItem(spacer_item28)
        self.line_edit_user_data_old_password = QtWidgets.QLineEdit(
            parent=self.user_data_stacked_widget
        )
        self.line_edit_user_data_old_password.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_user_data_old_password.setFont(font)
        self.line_edit_user_data_old_password.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password
        )
        self.line_edit_user_data_old_password.setStyleSheet(
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
        self.line_edit_user_data_old_password.setObjectName(
            "lineEditUserDataOldPassword"
        )
        self.vertical_layout_14.addWidget(self.line_edit_user_data_old_password)
        self.line_edit_user_data_new_password = QtWidgets.QLineEdit(
            parent=self.user_data_stacked_widget
        )
        self.line_edit_user_data_new_password.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_user_data_new_password.setFont(font)
        self.line_edit_user_data_new_password.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password
        )
        self.line_edit_user_data_new_password.setStyleSheet(
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
        self.line_edit_user_data_new_password.setObjectName(
            "lineEditUserDataNewPassword"
        )
        self.vertical_layout_14.addWidget(self.line_edit_user_data_new_password)
        self.line_edit_user_data_confirm_password = QtWidgets.QLineEdit(
            parent=self.user_data_stacked_widget
        )
        self.line_edit_user_data_confirm_password.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_user_data_confirm_password.setFont(font)
        self.line_edit_user_data_confirm_password.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password
        )
        self.line_edit_user_data_confirm_password.setStyleSheet(
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
        self.line_edit_user_data_confirm_password.setObjectName(
            "lineEditUserDataConfirmPassword"
        )
        self.vertical_layout_14.addWidget(self.line_edit_user_data_confirm_password)
        self.push_button_user_data_cp = QtWidgets.QPushButton(
            parent=self.user_data_stacked_widget
        )
        self.push_button_user_data_cp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.push_button_user_data_cp.setFont(font)
        self.push_button_user_data_cp.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_user_data_cp.setStyleSheet(
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
        self.push_button_user_data_cp.setObjectName("pushButtonUserDataCP")
        self.vertical_layout_14.addWidget(self.push_button_user_data_cp)
        self.label_user_data_error = QtWidgets.QLabel(
            parent=self.user_data_stacked_widget
        )
        self.label_user_data_error.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_data_error.setFont(font)
        self.label_user_data_error.setStyleSheet("color: red;")
        self.label_user_data_error.setObjectName("labelUserDataError")
        self.vertical_layout_14.addWidget(
            self.label_user_data_error, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        spacer_item29 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_14.addItem(spacer_item29)
        self.horizontal_layout_27.addLayout(self.vertical_layout_14)
        spacer_item30 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_27.addItem(spacer_item30)
        self.horizontal_layout_28.addLayout(self.horizontal_layout_27)
