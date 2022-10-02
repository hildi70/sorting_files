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
@date: 2022-10-02
@e-mail: karla.berger@web.de
@github: https://github.com/hildi70/sorting_files
"""

import os
import sys
import glob
import shutil
import re
import string

# change working directory to current folder:
os.chdir(os.path.dirname(sys.argv[0]))

print("Hi there! Let's sort some data! :)")
file_path = input("Which folder do you want to sort? E.g. \"Test\" ").rstrip("\n") + "/"
start_well = input("What's the first well to analyze? E.g. \"A1\" ").rstrip("\n")
stop_well = input("What's the last well to analyze? E.g. \"N22\" ").rstrip("\n")
number_fields = input("How many fields are included? E.g. \"2\" ").rstrip("\n")

start_letter = re.findall('\D', start_well)
stop_letter = re.findall('\D', stop_well)
letters = string.ascii_uppercase[string.ascii_uppercase.index(start_letter[0]):string.ascii_uppercase.index(stop_letter[0]) + 1]

start_number = re.findall('\d+', start_well)
stop_number = re.findall('\d+', stop_well)
numbers = ["%.2d" % i for i in range(int(start_number[0]), int(stop_number[0]) + 1 )]

fields = []
for i in range(1, int(number_fields) + 1):
    fields.append("fld " + str(i))


for letter in letters:
    for number in numbers:
        for field in fields:
            pattern = letter + "*" + number + "*" + field + "*.tif"
            for file in glob.iglob(file_path + pattern):
                file_name = os.path.basename(file) # ohne Leerzeichen
                new_path = letter + "/" + number + "/" + field + "/"
                new_file_name = file_name.replace(" ", "")
                if not (os.path.exists(file_path + new_path)):
                    os.makedirs(file_path + new_path)
                shutil.move(file_path + file_name, file_path + new_path + new_file_name)

print("Finished!")