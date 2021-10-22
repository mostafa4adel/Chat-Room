
from PyQt5 import QtCore, QtGui, QtWidgets
from loginWindow import *
from User import *
from PyQt5.QtWidgets import QMessageBox


class PortWindow(object):
    def __init__(self, MainWindow, dialogWindow, user: User):
        self.MainWindow = MainWindow
        self.dialogWindow = dialogWindow
        self.user = user

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(600, 624)
        self.MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainWindow.setStyleSheet("background-color:hsl(210, 36%, 96%);;")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 80, 400, 380))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.portNumber = QtWidgets.QLineEdit(self.frame)
        self.portNumber.setGeometry(QtCore.QRect(60, 60, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.portNumber.setFont(font)
        self.portNumber.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.portNumber.setToolTipDuration(0)
        self.portNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.portNumber.setAutoFillBackground(False)
        self.portNumber.setStyleSheet("  height: 3rem;\n"
                                      "  width: 95%;\n"
                                      "  font-size: 1.5rem;\n"
                                      "  color: hsl(205, 78%, 60%);\n"
                                      "  padding: 0.25rem 0.5rem;\n"
                                      "  text-transform: capitalize;")
        self.portNumber.setObjectName("portNumber")
        self.setPortandIp = QtWidgets.QPushButton(self.frame)
        self.setPortandIp.setGeometry(QtCore.QRect(90, 300, 220, 50))
        self.setPortandIp.setStyleSheet("border-radius:20px;\n"
                                        "background-color: hsl(205, 78%, 60%);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.setPortandIp.setObjectName("setPort")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.unAcceptePort = QtWidgets.QLabel(self.frame)
        self.unAcceptePort.setGeometry(QtCore.QRect(60, 120, 181, 21))
        self.unAcceptePort.setObjectName("unAcceptePort")
        self.ipAddress = QtWidgets.QLineEdit(self.frame)
        self.ipAddress.setGeometry(QtCore.QRect(60, 200, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ipAddress.setFont(font)
        self.ipAddress.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ipAddress.setToolTipDuration(0)
        self.ipAddress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ipAddress.setAutoFillBackground(False)
        self.ipAddress.setStyleSheet("  height: 3rem;\n"
                                     "  width: 95%;\n"
                                     "  font-size: 1.5rem;\n"
                                     "  color: hsl(205, 78%, 60%);\n"
                                     "  padding: 0.25rem 0.5rem;\n"
                                     "  text-transform: capitalize;")
        self.ipAddress.setObjectName("ipAddress")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.unAcceptedIpAdress = QtWidgets.QLabel(self.frame)
        self.unAcceptedIpAdress.setGeometry(QtCore.QRect(60, 260, 181, 21))
        self.unAcceptedIpAdress.setObjectName("unAcceptedIpAdress")
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

        self.unAcceptePort.setHidden(True)
        self.unAcceptedIpAdress.setHidden(True)
        self.setPortandIp.clicked.connect(self.setPortandIpAdd)
        self.setPortandIp.setShortcut("Return")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setPortandIp.setText(_translate("MainWindow", "Done"))
        self.label.setText(_translate("MainWindow", "Enter Port Number:"))
        self.unAcceptePort.setText(_translate(
            "MainWindow", "Not Accepted Port Number"))
        self.label_2.setText(_translate("MainWindow", "Enter Ip Address:"))
        self.unAcceptedIpAdress.setText(_translate(
            "MainWindow", "Not Accepted Ip Address"))
        self.actionPort_Number.setText(_translate("MainWindow", "Port Number"))
        self.actionIP_Address.setText(_translate("MainWindow", "IP Address"))

    def setPortandIpAdd(self):
        flage1 = False
        flage2 = False
        if(self.user.isIpAccepted(self.ipAddress.text())):
            flage1 = True
            self.unAcceptedIpAdress.setHidden(True)
        else:
            self.unAcceptedIpAdress.setHidden(False)

        if(self.user.isPortAccepted(self.portNumber.text())):
            flage2 = True
            self.unAcceptePort.setHidden(True)
        else:
            self.unAcceptePort.setHidden(False)

        if(flage1 and flage2):
            self.user.setTheIpandPort(
                self.ipAddress.text(), self.portNumber.text())

        try:
            self.user.setup()
            self.dialogWindow.setupUi()
            self.MainWindow.show()
        except:
            self.errorNoSuchServer()

    def errorNoSuchServer(self):
        msg = QMessageBox()
        msg.setWindowTitle("No Such Server")
        msg.setText(
            "This Server is not the right one")
        x = msg.exec_()
