import os
import argparse
parser = argparse.ArgumentParser()


def duplicates_arg(way, optional=None):
    name_files = [f for f in os.listdir(way) if f.endswith('.py')]
    if optional is None:
        for name in name_files:
            print(name)
    else:
        with open(optional, "w") as file_write:
            for name in name_files:
                file_write.write(name + "\n")


def large_arg(way, size):
    pass


def images_arg(way):
    pass


def old_arg(way):
    pass


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
else:
    print("NOT")
