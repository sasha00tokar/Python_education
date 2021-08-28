import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-o", type=str, help="In which file the results will be written")
parser.add_argument("-size", type=int, help="Size file" )
parser.add_argument(choices=["duplicates", "large", "images", "old"],
                    dest="argument", help="duplicates - search for identical files in the specified path,"
                                          "large - search files larger than the specified size,"
                                          "images - searches for image files,"
                                          "old - searches for files older than one year")

parser.add_argument("way", help="File path")

args = parser.parse_args()
print(args)
