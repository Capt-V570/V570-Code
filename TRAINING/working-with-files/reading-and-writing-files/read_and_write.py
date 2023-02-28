# Read and write files using the build-in Python file methods


def main():
    # # Open a file for writing and create it if it doesn't exist:
    # # NOTE: 'w' -> WRITE access in the file, '+' sign -> create file if not exist
    # my_file = open("textfile.txt", "w+")

    # # Open the file for appending text to the end
    # # NOTE: 'a' APPEND the data to the file
    my_file = open("textfile.txt", "a+")

    # # Write some lines of data to the file:
    for i in range(10):
        my_file.write("this is my NEW text\n")

    # # Close the file when done:
    my_file.close()

    # # Open the file backup and read the content:
    # # NOTE: 'r' READ the file content
    # my_file = open("textfile.txt", "r")

    # # check file mode:
    # if my_file.mode == "r":
    #     # contents = my_file.read()
    #     # print(contents)
    #     file_lines = my_file.readlines()
    #     for x in file_lines:
    # print(x)


if __name__ == "__main__":
    main()
