# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\anafa\OneDrive\Desktop\SocketsProgramingProject\loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 624)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color:hsl(210, 36%, 96%);;\n"
"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 120, 400, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(90, 150, 220, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("border-radius:20px;\n"
"background-color: hsl(205, 78%, 60%);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.loginButton.setIconSize(QtCore.QSize(20, 20))
        self.loginButton.setObjectName("loginButton")
        self.userName = QtWidgets.QTextEdit(self.frame)
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
"  box-sizing: border-box;\n"
"  font-size: 1.5rem;\n"
"  color: hsl(205, 78%, 60%);\n"
"  padding: 0.25rem 0.5rem;\n"
"  text-transform: capitalize;\n"
"\n"
"  transition: all 0.3s linear;\n"
"  cursor: pointer;")
        self.userName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.userName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.userName.setLineWidth(12)
        self.userName.setMidLineWidth(0)
        self.userName.setObjectName("userName")
        self.setIpPort = QtWidgets.QPushButton(self.frame)
        self.setIpPort.setGeometry(QtCore.QRect(90, 210, 220, 50))
        self.setIpPort.setStyleSheet("border-radius:20px;\n"
"background-color: hsl(205, 78%, 60%);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.setIpPort.setObjectName("setIpPort")
        self.noIpPortLabel = QtWidgets.QLabel(self.frame)
        self.noIpPortLabel.setGeometry(QtCore.QRect(60, 110, 161, 16))
        self.noIpPortLabel.setObjectName("noIpPortLabel")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPort_Number = QtWidgets.QAction(MainWindow)
        self.actionPort_Number.setObjectName("actionPort_Number")
        self.actionIP_Address = QtWidgets.QAction(MainWindow)
        self.actionIP_Address.setObjectName("actionIP_Address")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.setIpPort.setText(_translate("MainWindow", "Set IP/Port"))
        self.noIpPortLabel.setText(_translate("MainWindow", "Please input IP and Port!"))
        self.label.setText(_translate("MainWindow", "Enter Username:"))
        self.actionPort_Number.setText(_translate("MainWindow", "Port Number"))
        self.actionIP_Address.setText(_translate("MainWindow", "IP Address"))
