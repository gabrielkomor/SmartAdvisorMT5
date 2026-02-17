"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtCore, QtWidgets, QtGui


class TopFrameBuilder:
    def __init__(self, central_widget):
        self.centralWidget = central_widget
        self.top_frame = None
        self.app_icon_label = None
        self.app_name_label = None
        self.user_name_label = None
        self.push_button_user = None

        self.horizontal_layout_4 = None
        self.horizontal_layout = None

    def top_frame_setup(self):
        self.top_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.top_frame.setMinimumSize(QtCore.QSize(960, 85))
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.top_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.top_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_frame.setObjectName("topFrame")
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontal_layout_4.setContentsMargins(6, 3, 6, 3)
        self.horizontal_layout_4.setObjectName("horizontalLayout_4")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontalLayout")
        self.app_icon_label = QtWidgets.QLabel(parent=self.top_frame)
        self.app_icon_label.setMinimumSize(QtCore.QSize(75, 75))
        self.app_icon_label.setMaximumSize(QtCore.QSize(75, 75))
        self.app_icon_label.setText("")
        self.app_icon_label.setPixmap(QtGui.QPixmap("src\\assets\\Icon.png"))
        self.app_icon_label.setScaledContents(True)
        self.app_icon_label.setObjectName("appIconLabel")
        self.horizontal_layout.addWidget(self.app_icon_label)
        spacer_item31 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout.addItem(spacer_item31)
        self.app_name_label = QtWidgets.QLabel(parent=self.top_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.app_name_label.setFont(font)
        self.app_name_label.setStyleSheet("color: white;")
        self.app_name_label.setObjectName("appNameLabel")
        self.horizontal_layout.addWidget(self.app_name_label)
        spacer_item32 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout.addItem(spacer_item32)
        self.user_name_label = QtWidgets.QLabel(parent=self.top_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_name_label.setFont(font)
        self.user_name_label.setStyleSheet("color: white;")
        self.user_name_label.setObjectName("userNameLabel")
        self.horizontal_layout.addWidget(self.user_name_label)
        self.push_button_user = QtWidgets.QPushButton(parent=self.top_frame)
        self.push_button_user.setMinimumSize(QtCore.QSize(60, 60))
        self.push_button_user.setMaximumSize(QtCore.QSize(60, 60))
        self.push_button_user.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.push_button_user.setStyleSheet(
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
        self.push_button_user.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("src\\assets\\userIcon.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.push_button_user.setIcon(icon)
        self.push_button_user.setIconSize(QtCore.QSize(30, 30))
        self.push_button_user.setCheckable(True)
        self.push_button_user.setAutoExclusive(True)
        self.push_button_user.setObjectName("pushButtonUser")
        self.horizontal_layout.addWidget(self.push_button_user)
        self.horizontal_layout_4.addLayout(self.horizontal_layout)
