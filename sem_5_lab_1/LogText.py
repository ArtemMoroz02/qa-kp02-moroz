from BinaryFile import BinaryFile


class LogText(BinaryFile):
    def append(self, info: str):
        self.__info += f"\n{info}"
