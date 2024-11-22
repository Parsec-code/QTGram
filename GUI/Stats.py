# Game UI

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Stats(object):
    def setupUi(self, Stats):
        Stats.setObjectName("Stats")
        Stats.resize(418, 619)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stats.sizePolicy().hasHeightForWidth())
        Stats.setSizePolicy(sizePolicy)
        Stats.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                            "color: rgb(239, 239, 239);")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Stats)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.back = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.back.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                "color: rgb(239, 239, 239);\n"
                                "")
        self.back.setObjectName("back")
        self.gridLayout.addWidget(self.back, 1, 0, 1, 1)
        self.table = QtWidgets.QTableView(parent=self.gridLayoutWidget)
        self.table.setStyleSheet("color: rgb(91, 91, 91);\n"
                                 "background-color: rgb(239, 239, 239);")
        self.table.setObjectName("table")
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        self.retranslateUi(Stats)
        QtCore.QMetaObject.connectSlotsByName(Stats)

    def retranslateUi(self, Stats):
        _translate = QtCore.QCoreApplication.translate
        Stats.setWindowTitle(_translate("Stats", "Stats"))
        self.back.setText(_translate("Stats", "<"))
