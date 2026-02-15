from os import path, remove

from PyQt6 import QtCore, QtGui, QtWidgets


class SetUpTwoStepLoginUi(object):
    def __init__(self):
        self.horizontal_layout_2 = None
        self.left_frame = None
        self.vertical_layout_2 = None
        self.label_image_qr = None
        self.right_frame = None
        self.vertical_layout_3 = None
        self.email_label_1 = None
        self.vertical_layout = None
        self.email_label_2 = None
        self.email_label_3 = None
        self.email_label_4 = None
        self.email_label_5 = None
        self.code_label = None
        self.text_otp_code = None
        self.label_error = None
        self.horizontal_layout = None
        self.push_button_verify = None
        self.code_len = None
        self.window = None
        self.ui = None

    def setup_ui(self, form_app):
        form_app.setObjectName("Form")
        form_app.resize(754, 418)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        form_app.setFont(font)
        form_app.setStyleSheet("background-color:rgb(54, 54, 54);")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(form_app)
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        self.left_frame = QtWidgets.QFrame(parent=form_app)
        self.left_frame.setMinimumSize(QtCore.QSize(400, 400))
        self.left_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_frame.setObjectName("leftFrame")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.left_frame)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.label_image_qr = QtWidgets.QLabel(parent=self.left_frame)
        self.label_image_qr.setMinimumSize(QtCore.QSize(300, 150))
        self.label_image_qr.setStyleSheet("border-radius: 10px;")
        self.label_image_qr.setText("")
        self.label_image_qr.setPixmap(
            QtGui.QPixmap("images\\google_authenticator_qr.png")
        )
        self.label_image_qr.setScaledContents(True)
        self.label_image_qr.setObjectName("labelImageQr")
        self.vertical_layout_2.addWidget(self.label_image_qr)
        self.horizontal_layout_2.addWidget(self.left_frame)
        self.right_frame = QtWidgets.QFrame(parent=form_app)
        self.right_frame.setMinimumSize(QtCore.QSize(330, 400))
        self.right_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.right_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_frame.setObjectName("rightFrame")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.right_frame)
        self.vertical_layout_3.setObjectName("verticalLayout_3")
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
        self.vertical_layout_3.addWidget(
            self.email_label_1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("verticalLayout")
        spacer_item = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item)
        self.vertical_layout.addItem(spacer_item)
        self.email_label_2 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_2.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.email_label_2.setFont(font)
        self.email_label_2.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_2.setObjectName("emailLabel_2")
        self.vertical_layout.addWidget(
            self.email_label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.email_label_3 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_3.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email_label_3.setFont(font)
        self.email_label_3.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_3.setObjectName("emailLabel_3")
        self.vertical_layout.addWidget(
            self.email_label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.vertical_layout.addItem(spacer_item)
        self.vertical_layout.addItem(spacer_item)
        self.email_label_4 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_4.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.email_label_4.setFont(font)
        self.email_label_4.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_4.setObjectName("emailLabel_4")
        self.vertical_layout.addWidget(
            self.email_label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.email_label_5 = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label_5.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.email_label_5.setFont(font)
        self.email_label_5.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.email_label_5.setObjectName("emailLabel_5")
        self.vertical_layout.addWidget(
            self.email_label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        spacer_item1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item1)
        self.code_label = QtWidgets.QLabel(parent=self.right_frame)
        self.code_label.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.code_label.setFont(font)
        self.code_label.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "\n" ""
        )
        self.code_label.setObjectName("codeLabel")
        self.vertical_layout.addWidget(
            self.code_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.vertical_layout_3.addLayout(self.vertical_layout)
        spacer_item2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item2)
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
            self.label_error, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        spacer_item3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item3)
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
        self.vertical_layout_3.addLayout(self.horizontal_layout)
        self.horizontal_layout_2.addWidget(self.right_frame)

        self.re_translate_ui(form_app)
        QtCore.QMetaObject.connectSlotsByName(form_app)

        from src.frontend.email_verification_ui import EmailVerificationUi

        self.code_len = len(EmailVerificationUi.user_secret) // 2
        self.email_label_4.setText(EmailVerificationUi.user_secret[0 : self.code_len])
        self.email_label_5.setText(EmailVerificationUi.user_secret[self.code_len :])
        self.push_button_verify.clicked.connect(
            lambda: self.set_up_two_step_verify_btn(form_app)
        )

    def set_up_two_step_verify_btn(self, active_window):
        try:
            from src.backend.google_authenticator import verify_qr_code
            from src.backend.data_base_connection import get_secret_from_db
            from src.backend.encryption_file import decrypt, encrypt, encrypt_email
            from src.frontend.sign_in_ui import SignInUi

            email = SignInUi.global_email
            hashed_email = encrypt_email(email)
            secret = get_secret_from_db("users", hashed_email)
            decrypted_secret = decrypt(secret)
            code = self.text_otp_code.toPlainText()

            if verify_qr_code(code, decrypted_secret):
                if path.exists("images\\google_authenticator_qr.png"):
                    remove("images\\google_authenticator_qr.png")

                import src.frontend.log_in_ui as log_in_window

                self.window = QtWidgets.QWidget()
                self.ui = log_in_window.LogInUi()
                self.ui.setup_ui(self.window)
                self.window.show()
                active_window.close()
            else:
                self.label_error.setText("Code is incorrect")
        except Exception as error:
            print(f"Error: {error}")

    def re_translate_ui(self, form_app):
        _translate = QtCore.QCoreApplication.translate
        form_app.setWindowIcon(QtGui.QIcon("images\\Icon.png"))
        form_app.setWindowTitle(_translate("Form", "Smart Advisor MT5"))
        self.email_label_1.setText(_translate("Form", "Set up two-step login"))
        self.email_label_2.setText(_translate("Form", "Scan the qr code or"))
        self.email_label_3.setText(_translate("Form", "enter the code below"))
        self.email_label_4.setText(_translate("Form", ""))
        self.email_label_5.setText(_translate("Form", ""))
        self.text_otp_code.setPlaceholderText(
            _translate("Form", "Enter verification code")
        )
        self.push_button_verify.setText(_translate("Form", "Verify code"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = SetUpTwoStepLoginUi()
    ui.setup_ui(form)
    form.show()
    sys.exit(app.exec())
