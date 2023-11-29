from PyQt6.QtWidgets import *
from gui import *
from televisionRemote import *


# Logic when using the GUI
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Sets up GUI logic. Creates Television object. Contains button logic.
        """
        super().__init__()
        self.setupUi(self)

        # create tele
        self.tele = Television()
        print(self.tele)

        # power button stuff
        self.powerButton.clicked.connect(lambda: self.tele.power())
        self.powerButton.clicked.connect(lambda: print(self.tele))

        # channel button stuff
        self.chaUpButton.clicked.connect(lambda: self.tele.channel_up())
        self.chaDownButton.clicked.connect(lambda: self.tele.channel_down())

        # volume button stuff
        self.volUpButton.clicked.connect(lambda: self.tele.volume_up())
        self.volDownButton.clicked.connect(lambda: self.tele.volume_down())

        # mute button stuff
        self.muteButton.clicked.connect((lambda: self.tele.mute()))
