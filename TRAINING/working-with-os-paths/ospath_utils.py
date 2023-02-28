# OS: this module give us the ability to work with operating system related features
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import platform

# print(os.name)
# print(platform.system())
# print(platform.release())


def os_and_path_operations():
    # Print the name of the OS:
    print(os.name)
    # Print platform name
    print(platform.system())
    # Print version of OS:
    print(platform.release())

    # Check for item existence:
    print("Item exists: ", str(path.exists("textfile.txt")))
    print("Item is a file:", path.isfile("textfile.txt"))
    print("Item is a directory:", path.isdir("textfile.txt"))

    # Work with file paths:
    print("Item's path:", path.realpath("textfile.txt"))
    # Separate file name from path:
    print("Item's path and name:", path.split(path.realpath("textfile.txt")))


def time_operations():
    # Get the modification time:
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago a file was modified:
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("textfile.txt")
    )
    print("It has been", td, "since the file was last modified")
    print("or in seconds:", td.total_seconds())


os_and_path_operations()
time_operations()
