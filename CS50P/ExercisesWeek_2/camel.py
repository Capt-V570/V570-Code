# replacing a camelCase input word to snake_case


def camel_to_snake(string):
    snake_case = ""
    for c in string:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c

    return snake_case


user_input = input("camelCase: ")

print("snake_case:", camel_to_snake(user_input))
