# OS: this module give us the ability to work with operating system related features
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import platform


def main():
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


if __name__ == "__main___":
    main()
