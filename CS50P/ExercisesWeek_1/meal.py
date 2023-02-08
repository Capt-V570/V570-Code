def convert(time):
    x, y = time.split(":")
    # breakpoint()
    hours = int(x)
    minutes = int(y)
    return hours + minutes / 60


def main():
    time = (
        input("What time is it (HH:MM a.m./p.m.)? ")
        .lstrip("0")
        .rstrip("a.m.")
        .rstrip("p.m.")
    )
    hours = convert(time)
    # breakpoint()
    if 7 <= hours <= 8:
        meal = "breakfast"
    elif 12 <= hours <= 13:
        meal = "lunch"
    elif 18 <= hours <= 19:
        meal = "dinner"
    else:
        meal = None
    if meal:
        print(f"{meal} time")


if __name__ == "__main__":
    main()
