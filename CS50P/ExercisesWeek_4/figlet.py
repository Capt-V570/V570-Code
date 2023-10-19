# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s
# for making large letters out of ordinary text, a form of ASCII art:

#  _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/
# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font,
# in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.

# NOTE Hints
# You can install pyfiglet with:
# pip install pyfiglet
# The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
# from pyfiglet import Figlet

# figlet = Figlet()
# You can then get a list of available fonts with code like this:

# figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:

# figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:

# print(figlet.renderText(s))
# Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.


# import sys
# import random
# from pyfiglet import Figlet


# def print_usage_and_exit():
#     print("Usage: python figlet.py [-f/--font <font_name>]")
#     sys.exit(1)


# def select_random_font():
#     figlet = Figlet()
#     fonts = figlet.getFonts()
#     return random.choice(fonts)


# def validate_font_argument(arg):
#     if arg == "-f" or arg == "--font":
#         return True

#     return False


# def get_font_name():
#     if len(sys.argv) != 3:
#         print_usage_and_exit()

#     arg1 = sys.argv[1]
#     arg2 = sys.argv[2]

#     if not validate_font_argument(arg1):
#         print("Invalid argument:", arg1)
#         print_usage_and_exit()

#     return arg2


# def prompt_user():
#     font_name = None

#     if len(sys.argv) == 3:
#         font_name = get_font_name()

#     figlet = Figlet(font=font_name) if font_name else Figlet(font=select_random_font())
#     user_input = input("Enter a string of text: ")
#     figlet_text = figlet.renderText(user_input)
#     print(figlet_text)


# prompt_user()

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]


def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font)
    elif (
        len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts()
    ):
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")


def figletize(prompt, f):
    txt = input(prompt)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(txt))


main()
