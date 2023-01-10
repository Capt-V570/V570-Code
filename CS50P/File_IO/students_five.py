# iterating through a csv file (students.csv) to obtain 'columns', for each element of the students.csv file:

# VERSION 5 - creating a function that returns the student name from the dictionary
# created since version 3 (see 'students_three.py'), into a dictonary (inside of a list), using a single line of code:

students = []

with open("students.csv") as file:
    for line in file:
        name, family = line.rstrip().split(",")
        student = {"name": name, "family": family}
        students.append(student)

# create a function that give it a student, this function is gonna simply return the name of the student
def get_name(student):
    return student["name"]


# the function created above will allow us to sort (thanks to 'sorted()') the list of students,
# by taking the 'key' of the dictionary within that list.
for student in sorted(students, key=get_name):
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
