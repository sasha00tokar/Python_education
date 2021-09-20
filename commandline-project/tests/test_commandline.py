import os
import os.path
import time
import shutil
from commandline.commandline import identical_files, files_are_larger, files_older_than_a_year, image_files


def make_dir(file_list, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    for name_file in file_list:
        open(os.path.join(directory, name_file), "a")


def test_commandline():
    directory = "folder"
    good_ret = ["file_2.py", "file_1.py"]
    file_list = ["file_1.py", "file_2.py", "file_3"]
    make_dir(file_list, directory)
    result = identical_files(directory)
    assert sorted(result) == sorted(good_ret)


def test_image_files():
    directory = "folder"
    good_ret = ["file_3.jpeg", "file_4.jpeg"]
    file_list = ["file_1.py", "file_3.jpeg", "file_2.py", "file_3", "file_4.jpeg"]
    make_dir(file_list, directory)
    result = image_files(directory)
    assert sorted(result) == sorted(good_ret)


def test_files_are_larger():
    size = 4
    directory = "folder"
    good_ret = ["file_2.py"]
    file_list = ["file_1.py", "file_3.jpeg", "file_2.py", "file_3", "file_4.jpeg"]
    make_dir(file_list, directory)
    with open(directory + "/file_2.py", "w") as f:
        f.write('sanya')
    result = files_are_larger(directory, size)
    assert sorted(result) == sorted(good_ret)


def test_files_older_than_a_year():
    value = 1
    directory = "folder"
    good_ret = ["file_1.py", "file_3.jpeg", "file_2.py", "file_3", "file_4.jpeg"]
    file_list = ["file_1.py", "file_3.jpeg", "file_2.py", "file_3", "file_4.jpeg"]
    make_dir(file_list, directory)
    time.sleep(1)
    result = files_older_than_a_year(directory, value)
    shutil.rmtree(directory)
    assert sorted(result) == sorted(good_ret)


