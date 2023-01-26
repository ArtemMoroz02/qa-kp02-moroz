from abc import ABC


class File(ABC):
    def __init__(self, info):
        self.__info = info

    @property
    def info(self):
        return self.__info
