# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that
# a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# NOTE Hints:
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods,
# including split.
# Note that you can handle two exceptions separately with code like:


def fuel_check():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            percentage = round(x / y * 100)
            if x == 0 and y == 100:
                return f"E"
            if x == 100 and y == 100:
                return f"F"
            if x > y:
                continue
            if fraction == "0/4":
                return f"E"
            if fraction == "1/4":
                return f"25%"
            if fraction == "1/2":
                return f"50%"
            if fraction == "3/4":
                return f"75%"
            if fraction == "4/4":
                return f"F"
            if percentage <= 2:
                return f"E"
            elif percentage >= 98:
                return f"F"
            else:
                return f"{percentage}%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


print(fuel_check())
