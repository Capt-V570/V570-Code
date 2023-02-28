import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def create_copy():
    # Checking existing file:
    if path.exists("textfile.txt"):
        # Get the path to the file in the current directory:
        source = path.realpath("textfile.txt")
        # Making a backup copy by appending "bak" to the name:
        backup = source + ".bak"
        # Creating the copy into destination:
        shutil.copy(source, backup)


def rename_file():
    # Checking existing file:
    if path.exists("textfile.txt"):
        # Renaming the original file:
        os.rename("textfile.txt", "newfile.txt")


def archive():
    # Make a duplicate of an existing file:
    if path.exists("textfile.txt.bak"):
        # Get the path to the file in the current directory:
        source = path.realpath("textfile.txt")
        # Create a ZIP archive by splitting root_dir from file path:
        root_dir, tail = path.split(source)
        shutil.make_archive("archive", "zip", root_dir)


def better_archive():
    # Checking existing file:
    if path.exists("textfile.txt.bak"):
        # More fine-grained control over ZIP files, by writing manually files into a newzip variable:
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


create_copy()
rename_file()
archive()
better_archive()
