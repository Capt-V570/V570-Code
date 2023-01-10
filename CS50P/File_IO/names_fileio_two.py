# Version 1 - reading the content of a txt document:
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hello,", line.rstrip())


# Version 2 - more elegant:
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
