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

        # hide channels
        self.Channel0Image.setVisible(False)
        self.Channel1Image.setVisible(False)
        self.Channel2Image.setVisible(False)
        self.Channel3Image.setVisible(False)

        # power button stuff
        self.powerButton.clicked.connect(lambda: self.channel_control(3))

        # channel button stuff
        self.chaUpButton.clicked.connect(lambda: self.channel_control(1))
        self.chaDownButton.clicked.connect(lambda: self.channel_control(2))

        # volume button stuff
        self.volUpButton.clicked.connect(lambda: self.volume_control(1))
        self.volDownButton.clicked.connect(lambda: self.volume_control(2))

        # mute button stuff
        self.muteButton.clicked.connect((lambda: self.volume_control(3)))

    def volume_control(self, bruh: int) -> None:
        """
        Controls volume and slider
        :param bruh: Determines which part to execute
        """
        if bruh == 1 and self.tele.get_status():
            self.tele.volume_up()
            self.volumeSlider.setValue(self.tele.get_volume())
        elif bruh == 2 and self.tele.get_status():
            self.tele.volume_down()
            self.volumeSlider.setValue(self.tele.get_volume())
        elif bruh == 3 and self.tele.get_status():
            self.tele.mute()
            if self.tele.get_mute():
                self.volumeSlider.setValue(0)
            else:
                self.volumeSlider.setValue(self.tele.get_volume())

    def channel_control(self, bruh: int) -> None:
        """
        Controls which channel appears on screen
        :param bruh: Determines which part to execute
        """
        imgList = [self.Channel0Image, self.Channel1Image, self.Channel2Image, self.Channel3Image]
        for img in imgList:
            img.setVisible(False)

        if bruh == 1 and self.tele.get_status():
            imgList[self.tele.get_channel()].setVisible(False)
            self.tele.channel_up()
            imgList[self.tele.get_channel()].setVisible(True)
        elif bruh == 2 and self.tele.get_status():
            imgList[self.tele.get_channel()].setVisible(False)
            self.tele.channel_down()
            imgList[self.tele.get_channel()].setVisible(True)
        elif bruh == 3:
            self.tele.power()
            if self.tele.get_status():
                imgList[self.tele.get_channel()].setVisible(True)
            else:
                imgList[self.tele.get_channel()].setVisible(False)

    # use setVisible to change visibility of channels
    # self.powerButtonImage.setVisible(False)
