import os
# import re  # use this later on
import argparse


def find_and_replace(path: str, old_str: str, new_str: str, verbose: bool):
    item_list = []
    try:
        item_list = os.listdir(path)
    except OSError as err:
        print("Error handling the path: {}".format(err))
        exit(1)

    for item in item_list:
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            find_and_replace(item_path, old_str, new_str, verbose)
        elif os.path.isfile(item_path):
            if verbose:
                print("Processing file: {}".format(item_path))

            with open(item_path) as file:
                found_match = False
                tmpfile_path = os.path.join(path, "tmp_file")

                with open(tmpfile_path, "w") as tmp_file:
                    for idx, line in enumerate(file):
                        # TODO: use regex in the next version
                        # for now just use simple replace
                        if old_str in line:
                            if verbose:
                                print("Replacing string in file: {}:{}".format(
                                    item_path, idx))
                            found_match = True
                            new_line = line.replace(old_str, new_str)
                            tmp_file.write(new_line)
                        else:
                            tmp_file.write(line)

                if found_match:
                    try:
                        os.replace(tmpfile_path, item_path)
                    except OSError as err:
                        print("Unable to replace the string: {}".format(err))
                        exit(1)


def main():
    arg_parser = argparse.ArgumentParser(
        description="PFR - Python Find and Replace")
    arg_parser.add_argument("--path", dest="path",
                            type=str, required=True, help="Search path")
    arg_parser.add_argument("--old-str", dest="old_str",
                            type=str, required=True, help="Search string")
    arg_parser.add_argument("--new-str", dest="new_str",
                            type=str, required=True, help="New string")
    arg_parser.add_argument("--verbose", dest="verbose", action="store_true")

    args = arg_parser.parse_args()
    path = args.path
    old_str = args.old_str
    new_str = args.new_str
    verbose = args.verbose

    find_and_replace(path, old_str, new_str, verbose)


if __name__ == "__main__":
    main()
