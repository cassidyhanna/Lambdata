# my_lambdata/my_mod.py


def enlarge(n):
    """
    param n is a number

    Function will enlarge the number

    """
    return n * 100

# this code breaks the ability to import enlarge from other files
if __name__ == "__main__":
    print("Hello")
    y = int(input("Please choose a number: "))
    print(y, enlarge(y))
