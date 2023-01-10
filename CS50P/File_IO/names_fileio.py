name = input("What's your name? ")

# Version 1 - by writing a name in a txt document:
# file = open("names.txt", "w")
# file.write(f"{name}\n")
# file.close()

# NOTE: 'a' for append and save // 'w' for just writing in it once - will be overwritten all the time

# Version 2 - by appending a name to a txt document:
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
