import socket
import threading
from PyQt5.QtWidgets import QTextBrowser
import re


class User():
    def __init__(self, OWNIPADDRESS):
        self.HEADER = 64
        self.OWNIPADDRESS = OWNIPADDRESS
        self.message = ''

        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.msgBox = QTextBrowser()
        # using 0 will make system give you a free port
        self.OWNADDR = (self.OWNIPADDRESS, 0)
        # verifying some constants

        self.portNumber = 0  # to whom you will send
        self.ipAddress = 0  # to whom you will send
        self.userName = ""

        self.sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sendingSocket.bind(self.OWNADDR)

        self.connected = False

    def setUserName(self, givenName):
        self.userName = givenName

    def isIpAndPortSet(self):
        if (self.ipAddress == 0 or self.portNumber == 0):
            return False
        else:
            return True

    def isIpAccepted(self, ipAddress):
        try:
            # i assume the ip address given will be in this form 192.168.1.0-till i don't know where
            # edit this if you think it is diffrent

            ipAddress = ipAddress.split('.')
            if(int(ipAddress[0]) == 192):
                if(int(ipAddress[1]) == 168):
                    if(int(ipAddress[2]) == 1):
                        if(int(ipAddress[3])):
                            return True
            return False

        except:
            return False

    def isPortAccepted(self, port):
        try:
            if(int(port) >= 5000 and int(port) <= 65535):
                return True
            else:
                return False
        except:
            return False

    def setTheIpandPort(self, ip, port):
        self.ipAddress = ip
        self.portNumber = int(port)

        print(
            f"Own Ip:{self.OWNIPADDRESS} Own Port:{self.sendingSocket.getsockname()}")

    def isUserValid(self, userName):
        return re.search("^[A-z][A-z|\.|\s]+$", userName)

    def getIpAddress(self):
        return self.ipAddress

    def getPortNumber(self):
        return self.portNumber

    def seeIfConnected(self):
        return self.connected

    def receive(self):
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.sendingSocket.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.sendingSocket.send(self.userName.encode('ascii'))
                else:
                    self.msgBox.append(
                        message.replace(self.userName, 'You', 1))
            except:
                # Close Connection When Error
                print("An error occured!")
                self.sendingSocket.close()
                break

    def setMessage(self, message):
        self.message = '{}: {}'.format(self.userName, message)

    def write(self):
        self.sendingSocket.send(self.message.encode('ascii'))

    def setupMessageBox(self,  messageBox: QTextBrowser):
        self.msgBox = messageBox
        self.msgBox.append("Welcome to the Chat Room")

    def setup(self):
        self.sendingSocket.connect((self.ipAddress, self.portNumber))

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

    def disconnect(self):
        self.setMessage(self.DISCONNECT_MESSAGE)
        self.write()
        self.sendingSocket.close()
