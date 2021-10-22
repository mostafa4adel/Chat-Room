
from PyQt5 import QtCore, QtGui, QtWidgets
from loginWindow import *
from User import *
from PyQt5.QtWidgets import QMessageBox
import socket


class DialogWindow(object):
    def __init__(self, MainWindow, user: User):
        self.MainWindow = MainWindow
        self.user = user

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(528, 599)
        self.MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainWindow.setStyleSheet("background-color:hsl(210, 36%, 96%);;")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 0, 451, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.message = QtWidgets.QTextEdit(self.frame)
        self.message.setGeometry(QtCore.QRect(100, 340, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message.setFont(font)
        self.message.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.message.setToolTipDuration(0)
        self.message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.message.setAutoFillBackground(False)
        self.message.setStyleSheet("  height: 3rem;\n"
                                   "  width: 95%;\n"
                                   "  font-size: 1.5rem;\n"
                                   "  color: hsl(205, 78%, 60%);\n"
                                   "  padding: 0.25rem 0.5rem;\n")
        self.message.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.message.setFrameShadow(QtWidgets.QFrame.Plain)
        self.message.setLineWidth(12)
        self.message.setMidLineWidth(0)
        self.message.setObjectName("message")
        self.sendMsg = QtWidgets.QPushButton(self.frame)
        self.sendMsg.setGeometry(QtCore.QRect(120, 390, 241, 41))
        self.sendMsg.setStyleSheet("border-radius:20px;\n"
                                   "background-color: hsl(205, 78%, 60%);\n"
                                   "font: 14pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.sendMsg.setObjectName("sendMsg")

        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(160, 490, 151, 41))
        self.close.setStyleSheet("border-radius:20px;\n"
                                 "background-color: hsl(205, 78%, 60%);\n"
                                 "font: 14pt \"MS Shell Dlg 2\";")
        self.close.setObjectName("goBack")

        self.dialog = QtWidgets.QTextBrowser(self.frame)
        self.dialog.setGeometry(QtCore.QRect(100, 51, 281, 261))
        self.dialog.setObjectName("dialog")
        font1 = QtGui.QFont()
        font.setPointSize(10)
        self.dialog.setFont(font1)
        self.dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dialog.setToolTipDuration(0)
        self.dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dialog.setAutoFillBackground(False)
        self.dialog.setStyleSheet("  height: 3rem;\n"
                                  "  width: 95%;\n"
                                  "  font-size: 1.5rem;\n"
                                  "  color: hsl(205, 78%, 60%);\n"
                                  "  padding: 0.25rem 0.5rem;\n")
        self.dialog.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dialog.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dialog.setLineWidth(12)
        self.dialog.setMidLineWidth(0)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 26))
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

        self.sendMsg.clicked.connect(self.sendMsgClicked)
        self.close.clicked.connect(self.closeClicked)

    def closeClicked(self):
        self.user.disconnect()
        exit()

    def sendMsgClicked(self):
        self.user.setMessage(self.message.toPlainText())
        self.user.write()
        self.message.clear()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.sendMsg.setText(_translate("MainWindow", "Send"))

        self.close.setText(_translate("MainWindow", "Close"))
        self.user.setupMessageBox(self.dialog)
