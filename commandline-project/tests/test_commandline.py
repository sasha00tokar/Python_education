from attrdict import AttrDict
import pytest

from commandline.commandline import identical_files, files_are_larger, files_older_than_a_year, image_files


def test_identical_files(mocker):
    mocker.patch("os.listdir", return_value=["file_2.py", "file_1.py", "file_3"])
    assert sorted(identical_files("foo/folder")) == sorted(["file_1.py", "file_2.py"])


def test_image_files(mocker):
    mocker.patch("os.listdir", return_value=["file_1.py", "file_3.jpeg", "file_2.py", "file_3", "file_4.jpeg"])
    assert sorted(image_files("foo/folder")) == sorted(["file_3.jpeg", "file_4.jpeg"])


def test_files_are_larger(mocker):
    mocker.patch("os.listdir", return_value=["file_1.py", "file_3.jpeg", "file_2.py"])
    mocker.patch("os.stat", return_value=AttrDict({"st_size": 5}))
    assert sorted(files_are_larger("foo/folder", 4)) == sorted(["file_1.py", "file_3.jpeg", "file_2.py"])


def test_files_older_than_a_year(mocker):
    mocker.patch("os.listdir", return_value=["file_1.py", "file_3.jpeg", "file_2.py"])
    mocker.patch("os.path.getmtime", return_value=1500000000)
    assert sorted(files_older_than_a_year("foo/folder", 1)) == sorted(["file_1.py", "file_3.jpeg", "file_2.py"])
