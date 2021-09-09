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


def output_or_write_to_file(name_function, name_file):
    if name_file is not None:
        write_to_file(name_file, name_function)
    else:
        name_function


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
        output_or_write_to_file(identical_files(parser.parse_args().way), parser.parse_args().o)
    elif parser.parse_args().argument == "large":
        output_or_write_to_file(files_are_larger(parser.parse_args().way, parser.parse_args().size),
                                parser.parse_args().o)
    elif parser.parse_args().argument == "images":
        output_or_write_to_file(image_files(parser.parse_args().way), parser.parse_args().o)
    elif parser.parse_args().argument == "old":
        output_or_write_to_file(files_older_than_a_year(parser.parse_args().way), parser.parse_args().o)
    else:
        print("NOT")
