# In a file called taqueria.py, implement a program that enables a user to place an order,
# prompting them for items, one per line, until the user inputs control-d
# (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far,
# prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

# NOTE Hints:
# Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
# try:
#     item = input()
# except EOFError:
#     ...
# You might want to print a new line so that the user’s cursor (and subsequent prompt)
# doesn’t remain on the same line as your program’s own prompt.

# Inputting control-d does not require inputting Enter as well, and so the user’s cursor
# (and subsequent prompt) might thus remain on the same line as your program’s own prompt.
# You can move the user’s cursor to a new line by printing \n yourself!
# Note that a dict comes with quite a few methods, per
# docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get,
# and supports operations like:
# d[key]
# and

# if key in d:
#     ...
# wherein d is a dict and key is a str.

# Be sure to avoid or catch any KeyError.


def restaurant_order():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    order = []
    total_cost = 0
    # print("Welcome to the taqueria! Here's our menu:")

    # for item, price in menu.items():
    #     print("- {}: ${:.2f}".format(item, price))
    while True:
        # print("\nWhat would you like to order?")
        try:
            item = input("Item: ").title()
            # while True:
            if item in menu:
                order.append(item)
                total_cost += menu[item]
                print("Total: ${:.2f}".format(total_cost))
            else:
                print("Sorry, we don't have that. Try again!")
                print("Total: ${:.2f}".format(total_cost))
        except EOFError:
            return
            # print("\nThank you for your order!")
            # print("Here's what you got:")
            # for item in order:
            #     #print("- {}".format(item))
            #     print("Total: ${:.2f}".format(total_cost))


# orders = input("Item: ")

# restaurant_order(orders)

if __name__ == "__main__":
    restaurant_order()
