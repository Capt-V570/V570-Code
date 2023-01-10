# iterating through a csv file (students.csv) to obtain 'columns', for each element of the students.csv file:

# VERSION 4 - by adding the two variables created in version 3 (see 'students_three.py') into a dictonary (inside of a list),
# using a single line of code:

students = []

with open("students.csv") as file:
    for line in file:
        name, family = line.rstrip().split(",")
        student = {"name": name, "family": family}
        students.append(student)


for student in students:
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
