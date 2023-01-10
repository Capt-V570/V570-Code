# iterating through a csv file to obtain 'rows', for each element of the students.csv file:

# VERSION 2 - by assigning, in parallel, two variables at once - 'name' and 'family',
# basically creating 2 columns (rather than rows as in version 1 - see: students.py)!
with open("students.csv") as file:
    for line in file:
        name, family = line.rstrip().split(",")
        print(f"{name} is coming from {family}'s Family")
