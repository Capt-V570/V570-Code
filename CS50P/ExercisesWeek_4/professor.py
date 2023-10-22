### LITTLE PROFESSOR GAME ###

# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# - Prompts the user for a level, 'n'. If the user does not input 1, 2, or 3, the program should prompt again.
# - Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
#  digits. No need to support operations other than addition (+).
# - Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# - If the user has still not answered correctly after three tries, the program should output the correct answer.
# - The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user
# for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with 'level' digits
# or raises a ValueError if level is not 1, 2, or 3:

# import random


# def main():
#     ...


# def get_level():
#     ...


# def generate_integer(level):
#     ...


# if __name__ == "__main__":
#     main()

# Hints
# NOTE: you can raise an exception like ValueError with code like:
# raise ValueError
# NOTE: the random module comes with quite a few functions, per docs.python.org/3/library/random.html.


import random


def main():
    equation = 10
    score = 0
    chances = 3
    level = get_level()
    while equation != 0:
        if chances == 3:  # User have 3 chances to answer each equation
            # Only generate_integer for new equation if chances == 3
            x, y = generate_integer(level)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                equation = equation - 1
                score = score + 1
                chances = 3  # Reset chances to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3  # Reset chances to generate new equation
            equation = equation - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
