import csv

# VERSION 11 - we create a program that ask for the user input of 'name' and 'family' data
# that will be append 'a' in the students_10.csv file, as row - using the csv.writer function.
name = input("What is your name? ")
family = input("What is your family name? ")

with open("students_10.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, family])
