import pytest
from FileSystem import FileSystem

dir_name = "dir"
file_name = "file"
dir_max_elems = 10


@pytest.fixture
def fs():
    return FileSystem(dir_max_elems)


def test_can_add_and_delete_directory(fs):
    fs.create_directory(dir_name)
    assert dir_name in fs.dirs
    fs.remove_directory(dir_name)
    assert dir_name not in fs.dirs


def test_cannot_add_more_to_directory(fs):
    fs.create_directory(dir_name)
    for x in range(dir_max_elems):
        fs.dirs[dir_name].add_file(file_name + str(x))
    with pytest.raises(OverflowError):
        fs.dirs[dir_name].add_file(file_name + str(dir_max_elems))


def test_cannot_delete_nonexistent_directory(fs):
    fs.create_directory(dir_name)
    fs.remove_directory(dir_name)
    with pytest.raises(KeyError):
        fs.remove_directory(dir_name)


def test_can_add_and_delete_file(fs):
    fs.add_file(file_name)
    assert file_name in fs.files
    fs.remove_file(file_name)
    assert file_name not in fs.files


def test_can_move_directory(fs):  # TODO implement test properly
    new_dir_name = "new_location"
    fs.create_directory(dir_name)
    fs.create_directory(new_dir_name)
    fs.dirs[dir_name].add_file(file_name)
    fs.move_directory(dir_name, fs.dirs[new_dir_name])
    assert dir_name not in fs.dirs
    assert dir_name in fs.dirs[new_dir_name].dirs


def test_can_move_file(fs):
    fs.create_directory(dir_name)
    fs.add_file(file_name)
    fs.move_file(file_name, fs.dirs[dir_name])
    assert file_name not in fs.files
    assert file_name in fs.dirs[dir_name].files


def test_cannot_move_non_existing_directory(fs):
    new_dir_name = "new_location"
    fs.create_directory(dir_name)
    fs.dirs[dir_name].create_directory(new_dir_name)
    fs.create_directory(new_dir_name)
    with pytest.raises(Exception):
        fs.move_directory(fs.dirs[dir_name].dirs[new_dir_name], fs)


def test_cannot_move_non_existing_file(fs):
    fs.create_directory(dir_name)
    fs.dirs[dir_name].add_file(file_name)
    fs.add_file(file_name)
    with pytest.raises(Exception):
        fs.move_file(fs.dirs[dir_name].files[file_name], fs)
