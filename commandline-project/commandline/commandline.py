import os
import argparse

from datetime import datetime
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()


def write_to_file(file, data):
    with open(file, "w") as file_write:
        file_write.write('\n'.join(data))


def duplicates_arg(way, name_file=None):
    files_list = [f for f in os.listdir(way) if f.endswith('.py')]
    if name_file is None:
        for name in files_list:
            return name
    else:
        write_to_file(name_file, files_list)


def large_arg(way, size, name_file=None):
    files_list = [f for f in os.listdir(way)]
    for name in files_list:
        if os.stat(name).st_size > size:
            if name_file is None:
                return name
            else:
                write_to_file(name_file, files_list)
        else:
            continue


def images_arg(way, name_file=None):
    files_list = [f for f in os.listdir(way) if f.endswith('.jpeg')]
    if name_file is None:
        for name in files_list:
            return name
    else:
        write_to_file(name_file, files_list)


def old_arg(way, name_file=None):
    files_list = [f for f in os.listdir(way)]
    one_year_ago = datetime.now() - relativedelta(years=1)
    for name in files_list:
        file_time = datetime.fromtimestamp(os.path.getmtime(name))
        if file_time < one_year_ago:
            if name_file is None:
                print(name)
            else:
                write_to_file(name_file, files_list)
        else:
            continue


def main():
    parser.add_argument("-o", type=str, help="In which file the results will be written")
    parser.add_argument("-size", type=int, help="Size file")
    parser.add_argument(choices=["duplicates", "large", "images", "old"],
                        dest="argument", help="duplicates - search for identical files in the specified path,"
                                              "large - search files larger than the specified size,"
                                              "images - searches for image files,"
                                              "old - searches for files older than one year")
    parser.add_argument("way", help="File path")

    if parser.parse_args().argument == "duplicates":
        duplicates_arg(parser.parse_args().way, parser.parse_args().o)
    elif parser.parse_args().argument == "large":
        large_arg(parser.parse_args().way, parser.parse_args().size, parser.parse_args().o)
    elif parser.parse_args().argument == "images":
        images_arg(parser.parse_args().way, parser.parse_args().o)
    elif parser.parse_args().argument == "old":
        old_arg(parser.parse_args().way, parser.parse_args().o)
    else:
        print("NOT")
