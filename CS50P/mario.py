def main():
    height = int(input("Height: "))
    pyramid(height)


# creating the actual pyramid of # blocks:
def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
