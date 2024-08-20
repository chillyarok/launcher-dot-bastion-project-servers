from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import requests
from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.utils import get_minecraft_directory
import uuid
import hard_funcs
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
    def login_menu(self):
        font = QtGui.QFont()
        font.setPointSize(24)
        self.back = QtWidgets.QFrame(MainWindow)
        self.back.setGeometry(QtCore.QRect(400,20,350,563))
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.logo = QtWidgets.QLabel(self.back)
        self.logo.setGeometry(QtCore.QRect(0,100,300,50))
        self.vhod = QtWidgets.QLabel(self.back)
        self.vhod.setGeometry(QtCore.QRect(0,50,300,50))
        self.vhod.setText("Вход")
        self.vhod.setFont(font)

        self.login = QtWidgets.QLineEdit(self.back)
        self.login.setGeometry(QtCore.QRect(25,100,300,50))
        self.login.setFont(font)
        self.login.setPlaceholderText("логин basmine id:")

        self.password = QtWidgets.QLineEdit(self.back)
        self.password.setGeometry(QtCore.QRect(25,170,300,50))
        self.password.setFont(font)
        self.password.setPlaceholderText("пароль basmine id:")
        self.LaunchButton.setDisabled(True)
        self.EnterNickname.setDisabled(True)
        self.settingsb.setDisabled(True)
    def soedinenie_info(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sinfo = QtWidgets.QLabel(MainWindow)
        self.sinfo.setObjectName("lost connection info")
        self.sinfo.setText("Нет соединения с интернетом или сервер недоступен \nпроверьте подключение к интернету")
        self.sinfo.setFont(font)
        self.sinfo.setStyleSheet("background-color: rgb(200, 0, 0);")
        self.sinfo.setGeometry(QtCore.QRect(0,0,500,60)) 
        self.sinfo.setVisible(False)
        
    def nick_to_file(self):
        with open('nick.txt','r') as nfile:
            f = nfile.readline()
            if f == '' or self.EnterNickname.text()!=f:
                with open("nick.txt","r+") as wnick:
                    wnick.seek(0)
                    wnick.truncate()
                    wnick.write(self.EnterNickname.text())

    def filenick(self):
        with open('nick.txt','r') as nfile:
            f = nfile.readline()
            if f == '':
                pass
            else:
                self.EnterNickname.setText(str(f))

    def w_connect(self):
        try:
            requests.get("https://ya.ru/")
            self.LaunchButton.setDisabled(False)
            self.sinfo.setVisible(False)
            
        except:
            self.LaunchButton.setDisabled(True)
            self.sinfo.setVisible(True)
    def settUI(self):
        #main settings menu
        self.settingswidget = QtWidgets.QFrame(self.centralwidget)
        self.settingswidget.setGeometry(QtCore.QRect(0,0,1126, 600))
        self.settingswidget.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.settingswidget.setVisible(False)
        #button for exit settings menu
        self.back_zone = QtWidgets.QLabel(self.settingswidget)
        self.back_zone.setGeometry(QtCore.QRect(400,20,300,563))
        self.back_zone.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal,self.back_zone)
        self.slider.setMinimum(0)
        self.slider.setMaximum(hard_funcs.get_ram_in_gb())
        self.slider.setValue(hard_funcs.get_ram_in_gb()//2)
        self.exitb = QtWidgets.QPushButton(self.back_zone) 
        self.exitb.setGeometry(QtCore.QRect(0,0,40,40)) 
        self.exitb.clicked.connect(lambda: self.settingswidget.setVisible(False))

    def setupUi(self, MainWindow):
        #window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
            #centralwidget {
                display: flex;
                flex-direction: row;
            }
            #leftline, #main {
                flex: 1;
            }
            @media (max-width: 768px) {
                #centralwidget {
                    flex-direction: column;
                }
                #leftline, #main {
                    flex: auto;
                }
                .back {
                    width: 100% !important;
                }
                .login, .password {
                    width: 90% !important;
                }
            }
        """)
        #left line
        self.leftline = QtWidgets.QFrame(self.centralwidget)
        self.leftline.setGeometry(QtCore.QRect(0, 0, 160, 600))
        self.leftline.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.leftline.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftline.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftline.setObjectName("leftline")
        #button for open settings menu
        self.settingsb = QtWidgets.QPushButton(self.leftline)
        self.settingsb.setGeometry(QtCore.QRect(3,3,40,40))
        #nickname enter line
        self.EnterNickname = QtWidgets.QLineEdit(self.leftline)
        self.EnterNickname.setGeometry(QtCore.QRect(2, 560, 150, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EnterNickname.setFont(font)
        self.EnterNickname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.EnterNickname.setText("")
        self.EnterNickname.setObjectName("EnterNickname")
        self.EnterNickname.setPlaceholderText("Введите никнейм")
        #main zone with picture
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(160, 0, 970, 600))
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.main.setStyleSheet("border-image:url(assets/bgimage.jpg);")
        #launch button
        self.LaunchButton = QtWidgets.QPushButton(self.centralwidget)
        self.LaunchButton.setGeometry(QtCore.QRect(520, 500, 231, 61))
        self.LaunchButton.setObjectName("LaunchButton")
        self.LaunchButton.setStyleSheet("QPushButton"
                                        "{"
                                        "border-image:url(assets/launchimage.png);"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        "border-image:url(assets/launchimage hover.png);"
                                        "}"
                                        "QPushButton::clicked"
                                        "{"
                                        "border-image:url(assets/launchimage clicked.png);"
                                        "}"
                                        )
        self.LaunchButton.clicked.connect(self.launch)
        #system funcs
        self.filenick()
        self.soedinenie_info()
        self.thread_starter()
        #progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(160, 578, 970, 21))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.launch_thread = LaunchThread()
        self.launch_thread.state_update_signal.connect(self.state_update)
        self.launch_thread.progress_update_signal.connect(self.update_progress_bar)
        #settings
        #self.settUI() пока не работает
        self.login_menu()
        self.settingsb.clicked.connect(lambda: self.settingswidget.setVisible(True))
        MainWindow.setCentralWidget(self.centralwidget)

        

        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

    def state_update(self,value):
        self.LaunchButton.setDisabled(value)
        self.progressBar.setDisabled(not value)

    def update_progress_bar(self,progress,max_progress,label):
        self.progressBar.setValue(progress)
        self.progressBar.setMaximum(max_progress)

    def launch(self):
        self.launch_thread.launch_setup_signal.emit(self.EnterNickname.text())
        self.nick_to_file()
        self.launch_thread.start()
    
    def thread_starter(self):
        self.w_connect()
        timer = threading.Timer(10.0,self.thread_starter)
        timer.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
