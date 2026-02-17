"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class RightFrameBuilder:
    """
    This class is responsible for creating right frame in main window.
    """

    def __init__(self, central_widget) -> None:
        self.central_widget = central_widget
        self.right_frame = None
        self.label_sma = None
        self.label_sma_decision = None
        self.label_rsi = None
        self.label_rsi_decision = None
        self.label_bb = None
        self.label_bb_decision = None
        self.label_macd = None
        self.label_macd_decision = None
        self.label_mma = None
        self.label_mma_decision = None
        self.label_adx = None
        self.label_adx_decision = None
        self.label_volume = None
        self.label_volume_decision = None

        self.vertical_layout_6 = None
        self.vertical_layout_3 = None

    def right_frame_builder_setup(self) -> None:
        """
        This method is responsible for create right frame content.
        :return: nothing.
        """
        self.right_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.right_frame.setMinimumSize(QtCore.QSize(80, 0))
        self.right_frame.setMaximumSize(QtCore.QSize(80, 16777215))
        self.right_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.right_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_frame.setObjectName("rightFrame")
        self.vertical_layout_6 = QtWidgets.QVBoxLayout(self.right_frame)
        self.vertical_layout_6.setContentsMargins(3, 3, 3, 3)
        self.vertical_layout_6.setObjectName("verticalLayout_6")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.vertical_layout_3.setSpacing(6)
        self.vertical_layout_3.setObjectName("verticalLayout_3")
        spacer_item39 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item39)
        self.label_sma = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sma.setFont(font)
        self.label_sma.setStyleSheet("color: white;")
        self.label_sma.setObjectName("labelSMA")
        self.vertical_layout_3.addWidget(
            self.label_sma, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_sma_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_sma_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_sma_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_sma_decision.setText("")
        self.label_sma_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_sma_decision.setScaledContents(True)
        self.label_sma_decision.setObjectName("labelSmaDecision")
        self.vertical_layout_3.addWidget(
            self.label_sma_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_rsi = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rsi.setFont(font)
        self.label_rsi.setStyleSheet("color: white;")
        self.label_rsi.setObjectName("labelRSI")
        self.vertical_layout_3.addWidget(
            self.label_rsi, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_rsi_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_rsi_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_rsi_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_rsi_decision.setText("")
        self.label_rsi_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_rsi_decision.setScaledContents(True)
        self.label_rsi_decision.setObjectName("labelRsiDecision")
        self.vertical_layout_3.addWidget(
            self.label_rsi_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_bb = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_bb.setFont(font)
        self.label_bb.setStyleSheet("color: white;")
        self.label_bb.setObjectName("labelBB")
        self.vertical_layout_3.addWidget(
            self.label_bb, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_bb_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_bb_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_bb_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_bb_decision.setText("")
        self.label_bb_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_bb_decision.setScaledContents(True)
        self.label_bb_decision.setObjectName("labelBbDecision")
        self.vertical_layout_3.addWidget(
            self.label_bb_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_macd = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_macd.setFont(font)
        self.label_macd.setStyleSheet("color: white;")
        self.label_macd.setObjectName("labelMACD")
        self.vertical_layout_3.addWidget(
            self.label_macd, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_macd_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_macd_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_macd_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_macd_decision.setText("")
        self.label_macd_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_macd_decision.setScaledContents(True)
        self.label_macd_decision.setObjectName("labelMacdDecision")
        self.vertical_layout_3.addWidget(
            self.label_macd_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_adx = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_adx.setFont(font)
        self.label_adx.setStyleSheet("color: white;")
        self.label_adx.setObjectName("labelADX")
        self.vertical_layout_3.addWidget(
            self.label_adx, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_adx_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_adx_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_adx_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_adx_decision.setText("")
        self.label_adx_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_adx_decision.setScaledContents(True)
        self.label_adx_decision.setObjectName("labelAdxDecision")
        self.vertical_layout_3.addWidget(
            self.label_adx_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_volume = QtWidgets.QLabel(parent=self.right_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_volume.setFont(font)
        self.label_volume.setStyleSheet("color: white;")
        self.label_volume.setObjectName("labelVOLUME")
        self.vertical_layout_3.addWidget(
            self.label_volume, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_volume_decision = QtWidgets.QLabel(parent=self.right_frame)
        self.label_volume_decision.setMinimumSize(QtCore.QSize(45, 45))
        self.label_volume_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_volume_decision.setText("")
        self.label_volume_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_volume_decision.setScaledContents(True)
        self.label_volume_decision.setObjectName("labelVolumeDecision")
        self.vertical_layout_3.addWidget(
            self.label_volume_decision, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        spacer_item40 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vertical_layout_3.addItem(spacer_item40)
        self.vertical_layout_6.addLayout(self.vertical_layout_3)
