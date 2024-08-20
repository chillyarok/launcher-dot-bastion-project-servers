from PyQt5 import QtCore
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
