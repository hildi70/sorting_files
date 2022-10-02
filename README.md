# sorting_files
Small program to sort files. Specifically, it sorts IN Cell Analyzer output files into subfolders.

## THE IDEA:
When doing experiments with the IN Cell Analyzer, the output is one folder with 1.000+ images.
To analyze them, images need to be organized in subfolders. Instead of doing this manually, this program will do the sorting job for you.

It sorts files according to specific patterns in the filenames. Specifically, all images of one field in one well are moved to one folder.
This means: all images of well A01 field 1 can be found in folder A/01/field 1 and so on.

In addition, it removes whitespace from the filename. Otherwise images could not be analyzed.

## HOW TO:
This file should be located in the upper-level folder of your output data.

E.g. script location: C:/user/project/sorting_files.py

Folder with files to sort: C:/user/project/exmaple_files/image1.tif etc.

To sort your files, open your Terminal and run the script.
For windows, this works via python launcher:
```shell
py  Path/to/script.py
```

When working with MAC-OS or have added python to your PATH in windows, you can run the script via:
```shell
python Path/to/script.py
```

Don't hesitate to contact me if there are questions, bugs, comments etc. Thanks and good luck! :)
