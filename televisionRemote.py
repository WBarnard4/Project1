class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Creates variables upon creation of Television
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Changes the power status to the opposite of what it currently is
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        While Television is on, changes the mute status to the opposite of what it currently is
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        While Television is on, increases channel value by 1. If at maximum, reduce to minimum
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        While Television is on, decrease channel value by 1. If at minimum, increase to maximum
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        While Television is on, increases volume value by 1. If at maximum, stay the same.
        If Television is muted, unmute first and continue
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        While Television is on, decreases volume value by 1. If at minimum, stay the same.
        If Television is muted, unmute first and continue
         """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Shows the full status of the Television
        :return: TV Status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
