# iterating through a csv file to obtain 'rows', for each element of the students.csv file:

# VERSION 1
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is coming from {row[1]}'s Family")

# this way we basically create a row of data (in this case, only containing names and surnames basically)
