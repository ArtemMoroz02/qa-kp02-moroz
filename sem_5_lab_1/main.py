# from FileSystem import FileSystem
# from BinaryFile import BinaryFile
# from LogText import LogText
# from Buffer import Buffer
#
# file_system = FileSystem(10)
# file_system.create_directory("first nested folder")
#
# first_dir = file_system.dirs["first nested folder"]
# first_dir.add_file("binary file", BinaryFile("immutable"))
#
# first_dir.create_directory("second nested folder")
# second_dir = first_dir.dirs["second nested folder"]
# second_dir.add_file("log text file", LogText("to be appended"))
# second_dir.add_file("buffer file", Buffer(10))
#
# file_system.list_subs()
