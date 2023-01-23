def convert(text) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input("Enter text here: ")
    text = convert(user_input)
    print(text)


main()
