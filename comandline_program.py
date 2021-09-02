import os
import re
import argparse

from datetime import datetime
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()


def write_to_file(file, data):
    with open(file, "w") as file_write:
        for name in data:
            file_write.write(name + "\n")


def duplicates_arg(way, optional=None):
    name_files = [f for f in os.listdir(way) if f.endswith('.py')]
    if optional is None:
        for name in name_files:
            return name
    else:
        write_to_file(optional, name_files)


def large_arg(way, size , optional=None):
    name_files = [f for f in os.listdir(way)]
    for name in name_files:
        if os.stat(name).st_size > size:
            if optional is None:
                return name
            else:
                write_to_file(optional, name_files)
        else:
            continue


def images_arg(way, optional=None):
    name_files = [f for f in os.listdir(way) if f.endswith('.jpeg')]
    if optional is None:
        for name in name_files:
            return name
    else:
        write_to_file(optional, name_files)


def old_arg(way, optional=None):
    name_files = [f for f in os.listdir(way)]
    one_year_ago = datetime.now() - relativedelta(years=1)
    for name in name_files:
        file_time = datetime.fromtimestamp(os.path.getmtime(name))
        if file_time < one_year_ago:
            if optional is None:
                print(name)
            else:
                write_to_file(optional, name_files)
        else:
            continue


parser.add_argument("-o", type=str, help="In which file the results will be written")
parser.add_argument("-size", type=int, help="Size file" )
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
