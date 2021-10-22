
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from portWindow import *
from dialogWindow import *
from User import *


class MainScreen(object):
    def __init__(self, MainWindow, user: User):
        self.MainWindow = MainWindow
        self.user = user

    def setNeededWindows(self, portWindow):
        self.portWindow = portWindow

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(600, 624)
        self.MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainWindow.setStyleSheet("background-color:hsl(210, 36%, 96%);")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 120, 400, 300))

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(90, 150, 220, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("border-radius:20px;"
                                       "background-color: hsl(205, 78%, 60%);"
                                       "font: 14pt \"MS Shell Dlg 2\";"
                                       )
        self.loginButton.setIconSize(QtCore.QSize(20, 20))
        self.loginButton.setObjectName("loginButton")
        self.userName = QtWidgets.QLineEdit(self.frame)
        self.userName.setGeometry(QtCore.QRect(60, 50, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.userName.setFont(font)
        self.userName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.userName.setToolTipDuration(0)
        self.userName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userName.setAutoFillBackground(False)
        self.userName.setStyleSheet("  height: 3rem;\n"
                                    "  width: 95%;\n"
                                    "  font-size: 1.5rem;\n"
                                    "  color: hsl(205, 78%, 60%);\n"
                                    "  padding: 0.25rem 0.5rem;\n"
                                    "  text-transform: capitalize;\n")
        self.userName.setObjectName("userName")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.actionPort_Number = QtWidgets.QAction(self.MainWindow)
        self.actionPort_Number.setObjectName("actionPort_Number")
        self.actionIP_Address = QtWidgets.QAction(self.MainWindow)
        self.actionIP_Address.setObjectName("actionIP_Address")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.loginButton.clicked.connect(self.loginClicked)

        self.loginButton.setShortcut("Return")

    def loginClicked(self):
        print()
        if(self.user.isUserValid(self.userName.text())):
            self.user.setUserName(self.userName.text())
            self.userName.clear()
            self.portWindow.setupUi()
            self.MainWindow.show()
        else:
            self.noIpPortLabel.setHidden(False)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))

        self.label.setText(_translate("MainWindow", "Enter Username:"))
        self.actionPort_Number.setText(_translate("MainWindow", "Port Number"))
        self.actionIP_Address.setText(_translate("MainWindow", "IP Address"))
