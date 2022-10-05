"""Sorting program for IN Cell Analyzer 2200 output.

THE IDEA:
When doing experiments with the IN Cell Analyzer, the output is one folder with 1.000+ images.
To analyze them, images need to be organized in subfolders. Instead of doing this manually, this program will do the sorting job for you.

It sorts files according to specific patterns in the filenames. Specifically, all images of one field in one well are moved to one folder
- e.g. all images of well A01 field 1 can be found in folder A/01/field 1.

In addition, it removes whitespace from the filename. Otherwise images could not be analyzed.

HOW TO:
This file should be located in the upper-level folder of your output data.
E.g. script location:       C:/user/project/sorting_files.py
Folder with files to sort:  C:/user/project/exmaple_files/image1.tif etc.

To sort your files, open your Terminal and run the script.
For windows, this works via python launcher:
    py  Path/to/script.py (in our example: py C:/user/project/sorting_files.py)
When working with MAC-OS or have added python to your PATH in windows, you can run the script via:
    python Path/to/script.py

Don't hesitate to contact me if there are questions, bugs, comments etc. Thanks and good luck! :)

Contact:
@author: Karla Berger
@date: 2022-10-05
@e-mail: karla.berger@web.de
@github: https://github.com/hildi70/sorting_files
"""

# TODO:
# - add error messages

import os
import sys
import glob
import shutil
import re
import string

# change working directory to current folder:
os.chdir(os.path.dirname(sys.argv[0]))

print("Hi there! Let's sort some data! :)")
file_path = input("Which folder do you want to sort? E.g. \"example_data\" ").rstrip("\n") + "/"
start_well = input("What's the first well to analyze? E.g. \"A1\" ").rstrip("\n")
stop_well = input("What's the last well to analyze? E.g. \"N22\" ").rstrip("\n")
number_fields = input("How many fields are included? E.g. \"2\" ").rstrip("\n")

start_letter = re.search("\D", start_well).group().upper()
stop_letter = re.search("\D", stop_well).group().upper()
letters = string.ascii_uppercase[string.ascii_uppercase.index(start_letter):string.ascii_uppercase.index(stop_letter) + 1]

start_number = re.search("\d+", start_well).group()
stop_number = re.search("\d+", stop_well).group()

# extract well number of randomly selected file
example_number = 0
for file in glob.iglob(file_path + "*.tif"):
    example_file = os.path.basename(file)
    example_number = re.search("\d{1,3}\(", example_file).group()[:-1]
    break

if (len(example_number) > 1):
    numbers = ["%.2d" % i for i in range(int(start_number), int(stop_number) + 1 )]
else:
    numbers = [i for i in range(int(start_number), int(stop_number) + 1 )]

fields = []
for i in range(1, int(number_fields) + 1):
    fields.append("fld " + str(i))


for letter in letters:
    for number in numbers:
        for field in fields:
            pattern = "*" + letter + "*" + str(number) + "*" + field + "*.tif"
            for file in glob.iglob(file_path + pattern):
                file_name = os.path.basename(file)
                new_path = letter + "/" + str(number) + "/" + field + "/"
                new_file_name = file_name.replace(" ", "")
                if not (os.path.exists(file_path + new_path)):
                    os.makedirs(file_path + new_path)
                shutil.move(file_path + file_name, file_path + new_path + new_file_name)

print("Finished!")