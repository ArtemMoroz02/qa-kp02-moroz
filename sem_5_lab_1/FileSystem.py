from BinaryFile import BinaryFile
from File import File


class FileSystem:
    def __init__(self, dir_max_elems):
        self.dirs = dict()
        self.files = dict()
        self.__dir_max_elems = dir_max_elems

    @property
    def dir_max_elems(self):
        return self.__dir_max_elems

    def create_directory(self, name: str):
        # if not self.contains_directory(name):
        #     self.dirs[name] = Directory(self.__dir_max_elems)
        pass

    def add_file(self, name: str, file: File = BinaryFile("")):
        # if self.contains_file(name):
        #     raise Exception(f"file \"{name}\" already exists")
        # self.files[name] = file
        pass

    def remove_directory(self, name: str):
        # self.dirs.pop(name)
        pass

    def remove_file(self, name: str):
        # self.files.pop(name)
        pass

    def move_directory(self, name: str, new_location):  # TODO error if already exists
        # if self.dirs[name] is new_location:
        #     raise Exception("destination directory is the same as the source one")
        # if new_location.contains_directory(name):
        #     raise Exception("destination directory already contains a folder with this name")
        #
        # new_location.create_directory(name)
        # new_location.__add_directory_subs(self.dirs.pop(name))
        pass

    def __add_directory_subs(self, dir):
        # for key, value in dir.dirs.items():
        #     if key in self.dirs:
        #         raise Exception(f"directory \"{key}\" already exists")
        #     self.dirs[key] = value
        # for key, value in dir.files.items():
        #     if key in self.files:
        #         raise Exception(f"file \"{key}\" already exists")
        #     self.files[key] = value
        pass

    def move_file(self, name: str, new_location):
        # new_location.files[name] = self.files.pop(name)
        pass

    def contains_directory(self, name: str) -> bool:
        # return name in self.dirs
        pass

    def contains_file(self, name: str) -> bool:
        # return name in self.files
        pass

    def list_subs(self, indent=""):  # TODO check
        # for key, value in self.dirs.items():
        #     print(f"{indent}|_ {key}")
        #     value.list_subs(indent + "\t")
        # for key, value in self.files.items():
        #     print(f"{indent}|_ {key}")
        pass

    def size(self):
        # return len(self.dirs) + len(self.files)
        pass


class Directory(FileSystem):
    def check_size(self):
        # if self.size() == self.dir_max_elems:
        #     raise OverflowError("cannot add more elements to this directory")
        pass

    def create_directory(self, name: str):
        # self.check_size()
        # super().create_directory(name)
        pass

    def __add_directory_subs(self, dir):
        # for key, value in dir.dirs.items():
        #     if key in self.dirs:
        #         raise Exception(f"directory \"{key}\" already exists")
        #     self.check_size()
        #     self.dirs[key] = value
        # for key, value in dir.files.items():
        #     if key in self.files:
        #         raise Exception(f"file \"{key}\" already exists")
        #     self.check_size()
        #     self.files[key] = value
        pass

    def add_file(self, name: str, file: File = BinaryFile("")):
        # self.check_size()
        # super().add_file(name, file)
        pass
