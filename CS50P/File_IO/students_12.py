import csv

# VERSION 12 - we create a program that ask for the user input of 'name' and 'family' data
# this time, it will be appended ['a'] in the students_10.csv file, as dictionary - using the csv.DictWriter function.
name = input("What is your name? ")
family = input("What is your family name? ")

# we now gonna use DictWriter, which actually will let us write a dictionary into a file:
with open("students_10.csv", "a") as file:
    # NOTE: with DictWriter we need to specify the 'fieldnames' (columns) that are going to be filled (this case: 'name', 'family')
    writer = csv.DictWriter(file, fieldnames=["name", "family"])
    writer.writerow({"name": name, "family": family})
