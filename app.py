from ui import Ui_MainWindow
from launch_thread import LaunchThread
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())