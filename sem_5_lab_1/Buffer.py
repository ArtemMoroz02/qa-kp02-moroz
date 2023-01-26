from File import File
from collections import deque


class Buffer(File):  # MAX_BUF_FILE_SIZE
    def __init__(self, max_buf_file_size):
        super().__init__(deque())
        self.__max_buf_file_size = max_buf_file_size

    def push(self, item):
        if len(self.info) == self.__max_buf_file_size:
            raise OverflowError("cannot add more elements to this buffer file")
        self.info.append(item)

    def pop(self):
        return self.info.popleft()
