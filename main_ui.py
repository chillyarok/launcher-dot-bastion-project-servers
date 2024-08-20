from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import requests
from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.utils import get_minecraft_directory
import uuid
minecraft_dir = get_minecraft_directory().replace("minecraft","blauncher")
class LaunchThread(QtCore.QThread):

    launch_setup_signal = QtCore.pyqtSignal(str)
    progress_update_signal = QtCore.pyqtSignal(int, int, str)
    state_update_signal = QtCore.pyqtSignal(bool)
    ram_treb_signal = QtCore.pyqtSignal(int,int)
    username = ""
    progress = 0
    progress_max = 0
    progress_label = ''
    max_ram = 0
    treb_ram = 0
    def __init__(self):
        super().__init__()
        self.launch_setup_signal.connect(self.l_setup)
        self.ram_treb_signal.connect(self.ram)
    def ram(self,max,ram):
        self.max_ram = max
        self.treb_ram = ram
    def l_setup(self,username):
        self.username = username

    def update_progress(self,value):
        self.progress = value
        self.progress_update_signal.emit(self.progress,self.progress_max,self.progress_label)

    def update_max(self,value):
        self.progress_max = value
        self.progress_update_signal.emit(self.progress,self.progress_max,self.progress_label)

    def update_progress_label(self,value):
        self.progress_label = value
        self.progress_update_signal.emit(self.progress,self.progress_max,self.progress_label)

    def run(self):
        self.state_update_signal.emit(True)
        vers = "1.20.1"
        install_minecraft_version(versionid=vers,minecraft_directory=minecraft_dir,callback={"setMax":self.update_max,"setProgress":self.update_progress,"setStatus":self.update_progress_label})
        command = get_minecraft_command(version=vers,minecraft_directory=minecraft_dir,options={"username":self.username,'uuid': str(uuid.uuid1()),'token': '','quickPlayMultiplayer':"95.31.220.184:25565",'maxMemory': '4096M','initialMemory': '2048M'})
        process = QtCore.QProcess()
        process.start(command[0], command[1:])
        self.state_update_signal.emit(False)
        self.update_progress(self,0)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1530, 730)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(1530, 730))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_info_line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_info_line.sizePolicy().hasHeightForWidth())
        self.left_info_line.setSizePolicy(sizePolicy)
        self.left_info_line.setMinimumSize(QtCore.QSize(200, 0))
        self.left_info_line.setBaseSize(QtCore.QSize(200, 0))
        self.left_info_line.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.left_info_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_info_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_info_line.setObjectName("left_info_line")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_info_line)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.left_info_line)
        self.logo.setMinimumSize(QtCore.QSize(200, 66))
        self.logo.setStyleSheet("border-image: url(:/logo/BASMINE.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setScaledContents(False)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.servers = QtWidgets.QWidget(self.left_info_line)
        self.servers.setObjectName("servers")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.servers)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bation_smp = QtWidgets.QPushButton(self.servers)
        self.bation_smp.setObjectName("bation_smp")
        self.verticalLayout_4.addWidget(self.bation_smp)
        self.nn = QtWidgets.QPushButton(self.servers)
        self.nn.setObjectName("nn")
        self.verticalLayout_4.addWidget(self.nn)
        self.verticalLayout_2.addWidget(self.servers)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.account = QtWidgets.QWidget(self.left_info_line)
        self.account.setObjectName("account")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.account)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.account_name = QtWidgets.QLabel(self.account)
        self.account_name.setObjectName("account_name")
        self.verticalLayout_5.addWidget(self.account_name)
        self.viyti_iz_accounta = QtWidgets.QPushButton(self.account)
        self.viyti_iz_accounta.setObjectName("viyti_iz_accounta")
        self.verticalLayout_5.addWidget(self.viyti_iz_accounta)
        self.verticalLayout_2.addWidget(self.account)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.left_info_line)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.left_info_line)
        self.main = QtWidgets.QWidget(self.centralwidget)
        self.main.setObjectName("main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.launch_button_zone = QtWidgets.QGridLayout()
        self.launch_button_zone.setObjectName("launch_button_zone")
        self.launch_button = QtWidgets.QPushButton(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.launch_button.sizePolicy().hasHeightForWidth())
        self.launch_button.setSizePolicy(sizePolicy)
        self.launch_button.setMinimumSize(QtCore.QSize(230, 60))
        self.launch_button.setBaseSize(QtCore.QSize(230, 60))
        self.launch_button.setStyleSheet("QPushButton\n"
"{\n"
"border-image: url(:/launch_button/launchimage.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"border-image: url(:/launch_button/launchimage hover.png);\n"
"}\n"
"QPushButton::clicked\n"
"{\n"
"url(:/launch_button/launchimage clicked.png)\n"
"}")
        self.launch_button.setText("")
        self.launch_button.setObjectName("launch_button")
        self.launch_button_zone.addWidget(self.launch_button, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.launch_button_zone.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.launch_button_zone.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.launch_button_zone.addItem(spacerItem4, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.launch_button_zone)
        self.progressBar = QtWidgets.QProgressBar(self.main)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.launch_thread = LaunchThread()
        self.launch_thread.state_update_signal.connect(self.state_update)
        self.launch_thread.progress_update_signal.connect(self.update_progress_bar)
        self.launch_button.clicked.connect(self.launch)

    def state_update(self,value):
        self.launch_button.setDisabled(value)
        self.progressBar.setDisabled(not value)

    def update_progress_bar(self,progress,max_progress,label):
        self.progressBar.setValue(progress)
        self.progressBar.setMaximum(max_progress)
    def launch(self):
        self.launch_thread.launch_setup_signal.emit("yarok")   
        self.launch_thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bation_smp.setText(_translate("MainWindow", "bastion_smp"))
        self.nn.setText(_translate("MainWindow", "PushButton"))
        self.account_name.setText(_translate("MainWindow", "account nickname"))
        self.viyti_iz_accounta.setText(_translate("MainWindow", "Выйти из Аккаунта"))
        self.pushButton_2.setText(_translate("MainWindow", "о нас"))
    import assets.resources
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

        
