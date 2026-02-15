from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette


class LogInUi(object):
    login_email = ""

    def __init__(self):
        self.horizontal_layout_2 = None
        self.left_frame = None
        self.vertical_layout_2 = None
        self.label_image = None
        self.right_frame = None
        self.vertical_layout = None
        self.welcome_label = None
        self.email_label = None
        self.text_email = None
        self.password_label = None
        self.text_password = None
        self.label_error = None
        self.horizontal_layout = None
        self.push_button_log_in = None
        self.push_button_sign_in = None
        self.window = None
        self.ui = None

    def setup_ui(self, form):
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
        self.label_image.setPixmap(QtGui.QPixmap("assets\\StartLogo.png"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("labelImage")
        self.vertical_layout_2.addWidget(self.label_image)
        self.horizontal_layout_2.addWidget(
            self.left_frame,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.right_frame = QtWidgets.QFrame(parent=form)
        self.right_frame.setMinimumSize(QtCore.QSize(330, 400))
        self.right_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.right_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_frame.setObjectName("rightFrame")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.right_frame)
        self.vertical_layout.setObjectName("verticalLayout")
        self.welcome_label = QtWidgets.QLabel(parent=self.right_frame)
        self.welcome_label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);"
        )
        self.welcome_label.setObjectName("welcomeLabel")
        self.vertical_layout.addWidget(
            self.welcome_label,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.email_label = QtWidgets.QLabel(parent=self.right_frame)
        self.email_label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet(
            "color: white;\n"
            "background-color: rgba(0,0,0,0);\n"
            "margin-top: 10px;\n"
            ""
        )
        self.email_label.setObjectName("emailLabel")
        self.vertical_layout.addWidget(
            self.email_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.text_email = QtWidgets.QTextEdit(parent=self.right_frame)
        self.text_email.setMinimumSize(QtCore.QSize(50, 45))
        self.text_email.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.text_email.setFont(font)
        self.text_email.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor)
        )
        self.text_email.setStyleSheet(
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
        self.text_email.setObjectName("textEmail")
        self.vertical_layout.addWidget(
            self.text_email, 0, QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.password_label = QtWidgets.QLabel(parent=self.right_frame)
        self.password_label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet(
            "color: white;\n" "background-color: rgba(0,0,0,0);\n" "margin-top: 10px;"
        )
        self.password_label.setObjectName("passwordLabel")
        self.vertical_layout.addWidget(
            self.password_label, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.text_password = QtWidgets.QLineEdit(parent=self.right_frame)
        self.text_password.setMinimumSize(QtCore.QSize(50, 45))
        self.text_password.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.text_password.setFont(font)
        self.text_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.text_password.setStyleSheet("""
            QLineEdit {
                color: white;
                border-radius: 10px;
                background-color: rgb(54, 54, 54);
                border: 2px solid transparent;
            }
            QLineEdit:hover {
                color: white;\n
                border-radius: 10px;\n
                background-color: rgb(54, 54, 54);\n
                border: 2px solid rgb(0, 0, 0);\n
            }
        """)
        self.vertical_layout.addWidget(self.text_password)
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
            "margin-top: 10px;\n"
            "margin-bottom: 10px;"
        )
        self.label_error.setObjectName("labelError")
        self.vertical_layout.addWidget(
            self.label_error, 0, QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        spacer_item = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout.addItem(spacer_item)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize
        )
        self.horizontal_layout.setObjectName("horizontalLayout")
        self.push_button_log_in = QtWidgets.QPushButton(parent=self.right_frame)
        self.push_button_log_in.setMinimumSize(QtCore.QSize(140, 50))
        self.push_button_log_in.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.push_button_log_in.setFont(font)
        self.push_button_log_in.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_log_in.setStyleSheet(
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
        self.push_button_log_in.setObjectName("pushButtonLogIn")
        self.horizontal_layout.addWidget(self.push_button_log_in)
        spacer_item1 = QtWidgets.QSpacerItem(
            30,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout.addItem(spacer_item1)
        self.push_button_sign_in = QtWidgets.QPushButton(parent=self.right_frame)
        self.push_button_sign_in.setMinimumSize(QtCore.QSize(140, 50))
        self.push_button_sign_in.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.push_button_sign_in.setFont(font)
        self.push_button_sign_in.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_sign_in.setStyleSheet(
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
        self.push_button_sign_in.setObjectName("pushButtonSignIn")
        self.horizontal_layout.addWidget(self.push_button_sign_in)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.horizontal_layout_2.addWidget(self.right_frame)
        self.re_translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        self.push_button_log_in.clicked.connect(lambda: self.log_in_ui_btn(form))
        self.push_button_sign_in.clicked.connect(self.log_in_ui_sign_in_btn)
        self.push_button_sign_in.clicked.connect(form.close)
        self.set_dark_theme()

    def log_in_ui_btn(self, active_window):
        try:
            from src.backend.data_base_connection import get_password_from_db
            from src.backend.encryption_file import encrypt_email

            user_email = self.text_email.toPlainText()
            user_password = self.text_password.text()
            hashed_email = encrypt_email(user_email)
            db_password = get_password_from_db("users", hashed_email)

            if db_password is None:
                self.label_error.setText("Incorrect email or password")
            else:
                from src.backend.encryption_file import verify_hashed_password

                if verify_hashed_password(user_password, db_password):
                    LogInUi.login_email = user_email

                    import src.frontend.log_in_two_step_ui as two_step_window

                    self.window = QtWidgets.QWidget()
                    self.ui = two_step_window.LogInTwoStepUi()
                    self.ui.setup_ui(self.window)
                    self.window.show()
                    active_window.close()
                else:
                    self.label_error.setText("Incorrect email or password")
        except Exception as error:
            print(f"Error: {error}")
            self.label_error.setText("Incorrect email or password")

    def log_in_ui_sign_in_btn(self):
        import src.frontend.sign_in_ui as sign_in_window

        self.window = QtWidgets.QWidget()
        self.ui = sign_in_window.SignInUi()
        self.ui.setup_ui(self.window)
        self.window.show()

    def re_translate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowIcon(QtGui.QIcon("assets\\Icon.png"))
        form.setWindowTitle(_translate("Form", "Smart Advisor MT5"))
        self.welcome_label.setText(_translate("Form", "Welcome!"))
        self.email_label.setText(_translate("Form", "Email"))
        self.text_email.setPlaceholderText(_translate("Form", "Enter your email"))
        self.password_label.setText(_translate("Form", "Password"))
        self.text_password.setPlaceholderText(_translate("Form", "Enter your password"))
        self.push_button_log_in.setText(_translate("Form", "Log in"))
        self.push_button_sign_in.setText(_translate("Form", "Sign in"))

    @staticmethod
    def set_dark_theme():
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        QApplication.instance().setPalette(dark_palette)


def run_app():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = LogInUi()
    ui.setup_ui(form)
    form.show()
    sys.exit(app.exec())
