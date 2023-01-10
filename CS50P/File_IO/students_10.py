# iterating through a csv file (students.csv) with the csv library, to unpack each element of the students.csv file:
import csv

# VERSION 10 - creating a function that uses the csv library that read a formatted csv file (students_10.csv) with columns (this case: 'name' and 'family')
# and returns the content of these 2 columns (name, family)  to append a dictionary of students data (within the list) created since version 3 (see 'students_3.py'):

students = []

with open("students_10.csv") as file:
    reader = csv.DictReader(file)
    # NOTE a DictReader returns a dictionary
    for row in reader:
        students.append({"name": row["name"], "family": row["family"]})

# NOTE: by formatting the csv file with the columns names ('name' and 'family', in this case) we allow this code to run more efficiently.

# using a lambda (or 'anonymous function') that give it a student, is gonna simply return the name of the student
# this function will allow us to sort the list of students by taking the 'key' of the dictionary within that list
for student in sorted(students, key=lambda student: student["name"]):
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
