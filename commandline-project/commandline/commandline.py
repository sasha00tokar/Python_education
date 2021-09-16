import os
import argparse

from datetime import datetime
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()


def write_to_file(file, data):
    with open(file, "w") as file_write:
        file_write.write('\n'.join(data))


def identical_files(way):
    files_list = [f for f in os.listdir(way) if f.endswith('.py')]
    return [str(name) for name in files_list]


def files_are_larger(way, size):
    files_list = [f for f in os.listdir(way)]
    return [str(name) for name in files_list if os.stat(way + '/' + name).st_size > size]


def image_files(way):
    files_list = [f for f in os.listdir(way) if f.endswith('.jpeg')]
    return [str(name) for name in files_list]


def files_older_than_a_year(way):
    files_list = [f for f in os.listdir(way)]
    one_year_ago = datetime.now() - relativedelta(years=1)
    return [str(name) for name in files_list
            if datetime.fromtimestamp(os.path.getmtime(way + '/' + name)) < one_year_ago]


def main():
    parser.add_argument("-o", type=str, help="In which file the results will be written")
    parser.add_argument("-size", type=int, help="Size file")
    parser.add_argument(choices=["duplicates", "large", "images", "old"],
                        dest="argument", help="duplicates - search for identical files in the specified path,"
                                              "large - search files larger than the specified size,"
                                              "images - searches for image files,"
                                              "old - searches for files older than one year")
    parser.add_argument("way", help="File path")
    command = parser.parse_args()
    file_data = None

    if command.argument == "duplicates":
        file_data = identical_files(command.way)
    elif command.argument == "large":
        file_data = files_are_larger(command.way, command.size)
    elif command.argument == "images":
        file_data = image_files(command.way)
    elif command.argument == "old":
        file_data = files_older_than_a_year(command.way)
    else:
        print("NOT")

    if command.o is not None:
        write_to_file(command.o, file_data)
