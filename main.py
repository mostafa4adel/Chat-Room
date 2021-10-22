from User import *
from loginWindow import *
from portWindow import *
from dialogWindow import *
import socket
# this project i didn't make control module because it is simple enough

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user = User(socket.gethostbyname(socket.gethostname()))
    MainWindow = QtWidgets.QMainWindow()
    mainScreen = MainScreen(MainWindow, user)

    dialogWindow = DialogWindow(MainWindow, user)
    portWindow = PortWindow(MainWindow, dialogWindow, user)
    mainScreen.setNeededWindows(portWindow)
    mainScreen.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
