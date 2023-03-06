# In a file called nutrition.py, implement a program that prompts
# users to input a fruit (case-insensitively) and then outputs the number
# of calories in one portion of that fruit, per the FDA’s poster for fruits,
# which is also available as text. Capitalization aside, assume that users
# will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
# Ignore any input that isn’t a fruit.

# NOTE Hints:
# Rather than use a conditional with 20 Boolean expressions, one for each fruit,
# better to use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# if k in d:
#     ...
# Take care to output the fruit’s calories, not calories from fat!


fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


def check_calories():
    string = input("Item: ").lower()
    if string in fruits:
        return f"Calories: {fruits[string]}"
    else:
        return f""


print(check_calories())
