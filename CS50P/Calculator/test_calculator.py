from calculator import square


def main():
    test_square()


# version 1:
# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")

# version 2 with 'assert' statement plus Exeptions:
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# version 3 - using UnitTest:


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0


if __name__ == "__main__":
    main()
