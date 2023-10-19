# When texting or tweeting, it’s not uncommon to shorten words
# to save time or space, as by omitting vowels, much like Twitter was originally called twttr.

# In a file called twttr.py, implement a program that prompts the user
# for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# text = input("Enter text here: ")
# vowels = ["a", "e", "i", "o", "u"]
# output = print("Output: ", end="")

# for c in text:
#     if c.casefold() not in vowels:
#         print(c, end="")

# print()

def twitter_shortener(text):
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([char for char in text if char not in vowels])


user_input = input("Enter text here: ")


print(twitter_shortener(user_input))
