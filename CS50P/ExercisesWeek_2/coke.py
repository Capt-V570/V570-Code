# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts
# coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


# Define the cost of a bottle of Coke in cents
COST = 50


def coke_distributor(coin):
    global COST
    # Define the accepted coins in cents
    COINS = [25, 10, 5]
    # Initialize the total amount inserted to 0
    total_inserted = 0
    # Prompt the user to insert coins until the cost of a bottle of Coke is reached
    while total_inserted < COST:
        # Prompt the user to insert a coin & keep track of the change insert from the user
        coin = int(input(f"Amount Due: {COST - total_inserted}\nInsert coin: "))
        # Check if the money is an accepted coin, add it to the total amount inserted
        if coin in COINS:
            # keep record of the coins inserted
            total_inserted += coin
            # Inform user in case the coin is not accepted:
        if coin != COINS:
            print("Change not accepted")
            # Output the final change owed to the user
        if total_inserted == COST:
            print("Change Owed: 0")
            break


user_money = 0

coke_distributor(user_money)


# tot_amount = 50

# def amount_due(amount):
#     global tot_amount
#     accepted_amounts = [25, 10, 5]
#     amount = int(input("Insert Coin: "))
#     while tot_amount > 0:
#         for amount in accepted_amounts:
#             tot_amount -= amount
#             print(int(input(f"Amount Due: {amount}\nInsert Coin: ")))
#             if tot_amount == 0:
#                 print("Amount Owed:", 0)
#                 break
#             elif amount != accepted_amounts:
#                 print("Change not accepted")


# user_input = int(input(f"Amount Due: {tot_amount}\nInsert Coin: "))

# amount_due(user_input)
