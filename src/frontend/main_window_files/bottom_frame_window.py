"""
This is an auxiliary file that stores a fragment of the graphical interface of the main application window.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class BottomFrameBuilder:
    """
    This class is responsible for creating bottom bar in main application window.
    """

    def __init__(self, central_widget) -> None:
        self.central_widget = central_widget
        self.bottom_frame = None
        self.label_additive = None
        self.label_additive_decision = None
        self.label_majority = None
        self.label_majority_decision = None
        self.label_median = None
        self.label_median_decision = None

        self.horizontal_layout_2 = None
        self.horizontal_layout_3 = None

    def bottom_frame_setup(self) -> None:
        """
        This method is responsible for creating bottom bar content.
        :return: nothing.
        """
        self.bottom_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.bottom_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.bottom_frame.setStyleSheet(
            "background-color: rgb(72, 72, 72);\n" "border-radius: 10px;"
        )
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_frame.setObjectName("bottomFrame")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontal_layout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontal_layout_3.setObjectName("horizontalLayout_3")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        spacer_item41 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_2.addItem(spacer_item41)
        self.label_additive = QtWidgets.QLabel(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_additive.setFont(font)
        self.label_additive.setStyleSheet("color: white;")
        self.label_additive.setObjectName("labelAdditive")
        self.horizontal_layout_2.addWidget(self.label_additive)
        self.label_additive_decision = QtWidgets.QLabel(parent=self.bottom_frame)
        self.label_additive_decision.setMinimumSize(QtCore.QSize(30, 30))
        self.label_additive_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_additive_decision.setText("")
        self.label_additive_decision.setPixmap(
            QtGui.QPixmap("src\\assets\\holdIcon.png")
        )
        self.label_additive_decision.setScaledContents(True)
        self.label_additive_decision.setObjectName("labelAdditiveDecision")
        self.horizontal_layout_2.addWidget(self.label_additive_decision)
        spacer_item42 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_2.addItem(spacer_item42)
        self.label_majority = QtWidgets.QLabel(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_majority.setFont(font)
        self.label_majority.setStyleSheet("color: white;")
        self.label_majority.setObjectName("labelMajority")
        self.horizontal_layout_2.addWidget(self.label_majority)
        self.label_majority_decision = QtWidgets.QLabel(parent=self.bottom_frame)
        self.label_majority_decision.setMinimumSize(QtCore.QSize(30, 30))
        self.label_majority_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_majority_decision.setText("")
        self.label_majority_decision.setPixmap(
            QtGui.QPixmap("src\\assets\\holdIcon.png")
        )
        self.label_majority_decision.setScaledContents(True)
        self.label_majority_decision.setObjectName("labelMajorityDecision")
        self.horizontal_layout_2.addWidget(self.label_majority_decision)
        spacer_item43 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_2.addItem(spacer_item43)
        self.label_median = QtWidgets.QLabel(parent=self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_median.setFont(font)
        self.label_median.setStyleSheet("color: white;")
        self.label_median.setObjectName("labelMedian")
        self.horizontal_layout_2.addWidget(self.label_median)
        self.label_median_decision = QtWidgets.QLabel(parent=self.bottom_frame)
        self.label_median_decision.setMinimumSize(QtCore.QSize(30, 30))
        self.label_median_decision.setMaximumSize(QtCore.QSize(60, 60))
        self.label_median_decision.setText("")
        self.label_median_decision.setPixmap(QtGui.QPixmap("src\\assets\\holdIcon.png"))
        self.label_median_decision.setScaledContents(True)
        self.label_median_decision.setObjectName("labelMedianDecision")
        self.horizontal_layout_2.addWidget(self.label_median_decision)
        spacer_item44 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontal_layout_2.addItem(spacer_item44)
        self.horizontal_layout_3.addLayout(self.horizontal_layout_2)
