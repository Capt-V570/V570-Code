import sys

# checks for error
if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hi, my name is", sys.argv[1])
