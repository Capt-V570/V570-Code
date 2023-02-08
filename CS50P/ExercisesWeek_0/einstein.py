"""
Einstein

Even if you haven't studied physics (recently or ever!), you might have heard that
, wherein:
E = represents energy (measured in Joules),
m = represents mass (measured in kilograms), and
c*2 = represents the speed of light (measured approximately as 300000000 meters per second),
per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

NOTE:
Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
Recall that int can convert a str to an int, per docs.python.org/3/library/functions.html#int.
Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.

"""


def main():
    mass = int(input("Enter mass in kilograms: "))
    c = 300000000  # speed of light in meters per second
    energy = mass * pow(c, 2)
    print(energy)


main()
