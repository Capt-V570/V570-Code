# iterating through a csv (students.csv) file to obtain 'columns', for each element of the students.csv file:

# VERSION 3 - by adding the two variables created in version 2 (see students_2.py) into a list, containing a dictonary:

students = []

with open("students.csv") as file:
    for line in file:
        name, family = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["family"] = family
        students.append(student)


for student in students:
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
