from File import File


class BinaryFile(File):
    def __init__(self, info: str):
        super().__init__(info)

    def readfile(self) -> str:
        return self.__info
