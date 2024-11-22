# Menu UI

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(800, 536)
        Welcome.setStyleSheet("background-color: rgb(54, 54, 54)")
        self.centralwidget = QtWidgets.QWidget(parent=Welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 240, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 56, 56);\n"
                                 "background-color: rgb(240, 240, 240);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.Authorization = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Authorization.setGeometry(QtCore.QRect(260, 420, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.Authorization.setFont(font)
        self.Authorization.setStyleSheet("color: rgb(239, 239, 239);\n"
                                         "background-color: rgb(91, 91, 91);")
        self.Authorization.setObjectName("Authorization")
        self.Support = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Support.setGeometry(QtCore.QRect(540, 450, 221, 31))
        self.Support.setStyleSheet("background-color: rgb(91, 91, 91);\n"
                                   "color: rgb(239, 239, 239)")
        self.Support.setObjectName("Support")
        Welcome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Welcome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCredits = QtWidgets.QMenu(parent=self.menubar)
        self.menuCredits.setObjectName("menuCredits")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        Welcome.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Welcome)
        self.statusbar.setObjectName("statusbar")
        Welcome.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCredits.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Menu"))
        self.label.setText(_translate("Welcome", "Приветствую!"))
        self.Authorization.setText(_translate("Welcome", "Авторизоваться"))
        self.Support.setText(_translate("Welcome", "Поддержать разработчика"))
