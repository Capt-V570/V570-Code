def main():
    mass = int(input("Enter mass in kilograms: "))
    c = 300000000  # speed of light in meters per second
    energy = mass * pow(c, 2)
    print(energy)


main()
