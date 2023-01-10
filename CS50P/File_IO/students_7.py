# iterating through a csv file (students.csv) to obtain 'columns', for each element of the students.csv file:

# VERSION 7 - creating a function that returns the student name from the dictionary
# created since version 3 (see 'students_3.py'), into a dictonary (inside of a list), using a single line of code:

students = []

with open("students.csv") as file:
    for line in file:
        name, family = line.rstrip().split(",")
        student = {"name": name, "family": family}
        students.append(student)

# this time, using a lambda (or 'anonymous function') that give it a student, is gonna simply return the name of the student
# this function will allow us to sort the list of students by taking the 'key' of the dictionary within that list.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
