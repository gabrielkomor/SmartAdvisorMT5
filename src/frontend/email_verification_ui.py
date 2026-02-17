"""
This file contains a class that creates the user's email address verification window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class EmailVerificationUi(object):
    """
    This class is responsible for create email verification window.
    """
    user_secret = ""

    def __init__(self):
        self.horizontal_layout_2 = None
        self.left_frame = None
        self.vertical_layout_2 = None
        self.label_image = None
        self.right_frame = None
        self.vertical_layout_3 = None
        self.vertical_layout = None
        self.email_label_1 = None
        self.email_label_2 = None
        self.text_otp_code = None
        self.label_error = None
        self.horizontal_layout = None
        self.push_button_verify = None
        self.push_button_back = None
        self.window = None
        self.ui = None

    def setup_ui(self, form) -> None:
        """
        This method is responsible for create window elements.
        :param form: window.
        :return: nothing.
        """
        form.setObjectName("Form")
        form.resize(754, 418)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        form.setFont(font)
        form.setStyleSheet("background-color:rgb(54, 54, 54);")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(form)
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        self.left_frame = QtWidgets.QFrame(parent=form)
        self.left_frame.setMinimumSize(QtCore.QSize(400, 400))
        self.left_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_frame.setObjectName("leftFrame")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.left_frame)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.label_image = QtWidgets.QLabel(parent=self.left_frame)
        self.label_image.setMinimumSize(QtCore.QSize(300, 150))
        self.label_image.setStyleSheet("border-radius: 10px;")
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("src\\assets\\StartLogo.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("labelImage")
        self.vertical_layout_2.addWidget(self.label_image)
        self.horizontal_layout_2.addWidget(self.left_frame)
        self.right_frame = QtWidgets.QFrame(parent=form)
        self.right_frame.setMinimumSize(QtCore.QSize(330, 400))
        self.right_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.right_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_frame.setObjectName("rightFrame")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.right_frame)
        self.vertical_layout_3.setObjectName("verticalLayout_3")
        spacer_item = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("verticalLayout")
        self.email_label_1 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_1.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email_label_1.setFont(font)
        self.email_label_1.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_1.setObjectName("emailLabel_1")
        self.vertical_layout.addWidget(
            self.email_label_1,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.email_label_2 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email_label_2.setFont(font)
        self.email_label_2.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_2.setObjectName("emailLabel_2")
        self.vertical_layout.addWidget(
            self.email_label_2,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        spacer_item1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item1)
        self.vertical_layout_3.addLayout(self.vertical_layout)
        self.text_otp_code = QtWidgets.QTextEdit(parent=self.right_frame)
        self.text_otp_code.setMinimumSize(QtCore.QSize(50, 45))
        self.text_otp_code.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.text_otp_code.setFont(font)
        self.text_otp_code.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor)
        )
        self.text_otp_code.setStyleSheet(
            "QTextEdit {\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "}\n"
            "\n"
            "QTextEdit:hover {\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.text_otp_code.setObjectName("textOtpCode")
        self.vertical_layout_3.addWidget(self.text_otp_code)
        self.label_error = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n"
            "color: red;\n"
            "margin-top: 5px;\n"
            "margin-bottom: 5px;"
        )
        self.label_error.setObjectName("labelError")
        self.vertical_layout_3.addWidget(
            self.label_error,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        spacer_item2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item2)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize
        )
        self.horizontal_layout.setObjectName("horizontalLayout")
        self.push_button_verify = QtWidgets.QPushButton(parent=self.right_frame)
        self.push_button_verify.setMinimumSize(QtCore.QSize(140, 45))
        self.push_button_verify.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.push_button_verify.setFont(font)
        self.push_button_verify.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_verify.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70, 70); \n"
            "    padding: 5px 10px; \n"
            "    font-size: 14px; \n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120); \n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70); \n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            ""
        )
        self.push_button_verify.setObjectName("pushButtonVerify")
        self.horizontal_layout.addWidget(self.push_button_verify)
        spacer_item3 = QtWidgets.QSpacerItem(
            30,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout.addItem(spacer_item3)
        self.push_button_back = QtWidgets.QPushButton(parent=self.right_frame)
        self.push_button_back.setMinimumSize(QtCore.QSize(140, 45))
        self.push_button_back.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.push_button_back.setFont(font)
        self.push_button_back.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_back.setStyleSheet(
            "QPushButton {\n"
            "    color: white;\n"
            "    background-color: rgb(90, 90, 90);\n"
            "    border-radius: 10px;\n"
            "    border: 2px solid rgb(70, 70, 70); \n"
            "    padding: 5px 10px; \n"
            "    font-size: 14px; \n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(120, 120, 120); \n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(70, 70, 70); \n"
            "    border: 2px solid rgb(0, 0, 0);\n"
            "}"
        )
        self.push_button_back.setObjectName("pushButtonBack")
        self.horizontal_layout.addWidget(self.push_button_back)
        self.vertical_layout_3.addLayout(self.horizontal_layout)
        self.horizontal_layout_2.addWidget(self.right_frame)

        self.re_translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        self.push_button_verify.clicked.connect(lambda: self.evu_verify_btn(form))
        self.push_button_back.clicked.connect(self.evu_back_btn)
        self.push_button_back.clicked.connect(form.close)

    def evu_back_btn(self) -> None:
        """
        This method is responsible for creating button on ui.
        :return: nothing.
        """
        import src.frontend.sign_in_ui as sign_in_window

        self.window = QtWidgets.QWidget()
        self.ui = sign_in_window.SignInUi()
        self.ui.setup_ui(self.window)
        self.window.show()

    def evu_verify_btn(self, active_window) -> None:
        """
        This method is responsible for creating button on ui ond these functionality.
        :param active_window: window.
        :return: nothing.
        """
        from src.frontend.sign_in_ui import SignInUi

        user_code = self.text_otp_code.toPlainText()

        if user_code == SignInUi.global_otp:
            from src.backend.encryption_file import encrypt_email, encrypt
            from src.backend.google_authenticator import create_qr_code
            from src.backend.data_base_connection import save_secret_in_db
            from src.frontend.sign_in_ui import SignInUi

            email = SignInUi.global_email
            username = email.split("@")[0]
            secret = create_qr_code(username)

            EmailVerificationUi.user_secret = secret
            encrypted_secret = encrypt(secret)
            hashed_email = encrypt_email(email)
            save_secret_in_db("users", hashed_email, encrypted_secret)

            import src.frontend.setup_two_step_login_ui as set_up_two_step_window

            self.window = QtWidgets.QWidget()
            self.ui = set_up_two_step_window.SetUpTwoStepLoginUi()
            self.ui.setup_ui(self.window)
            self.window.show()
            active_window.close()
        else:
            self.label_error.setText("Code is incorrect")

    def re_translate_ui(self, form) -> None:
        """
        This function is responsible for displaying texts on ui.
        :param form: window.
        :return: nothing.
        """
        _translate = QtCore.QCoreApplication.translate
        form.setWindowIcon(QtGui.QIcon("src\\assets\\Icon.png"))
        form.setWindowTitle(_translate("Form", "Smart Advisor MT5"))
        self.email_label_1.setText(_translate("Form", "Verification code has"))
        self.email_label_2.setText(_translate("Form", "been sent to your email"))
        self.text_otp_code.setPlaceholderText(
            _translate("Form", "Enter verification code")
        )
        self.push_button_verify.setText(_translate("Form", "Verify code"))
        self.push_button_back.setText(_translate("Form", "Back"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = EmailVerificationUi()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec())
