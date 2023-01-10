# Version 1 - reading the content of a txt document and sort the information (names in this case):
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
