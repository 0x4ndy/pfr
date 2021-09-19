from genericpath import isdir
import os
#import re  # use this later on


def find_and_replace(path: str, old_str: str, new_str: str):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):  # make sure to handle the OSError exception
            find_and_replace(item_path, old_str, new_str)
        elif os.path.isfile(item_path):
            print("Processing file: {}".format(item_path))

            with open(item_path) as file:
                found_match = False
                tmpfile_path = os.path.join(path, "tmp_file")

                with open(tmpfile_path, "w") as tmp_file:
                    for idx, line in enumerate(file):
                        # TODO: use regex in the next version
                        # for now just use simple replace
                        if old_str in line:
                            print("Replacing str in file: {}:{}".format(item_path, idx))
                            found_match = True
                            new_line = line.replace(old_str, new_str)
                            tmp_file.write(new_line)
                        else:
                            tmp_file.write(line)

                if found_match:
                    os.replace(tmpfile_path, item_path) # TODO: make sure to handle the OSError exception


def main():
    path = "testdata"
    old_str = "22222"
    new_str = "11111"
    print("Replacing: {} with {}; in: {}".format(old_str, new_str, path))
    find_and_replace(path, old_str, new_str)


if __name__ == "__main__":
    main()
