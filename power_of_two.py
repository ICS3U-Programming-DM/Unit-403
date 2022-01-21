# Created by Dylan Melo
# Created on Jan 2022
# Calculates the square of any numbers
# starting from 0 up until user number.

import math
user_input = input("Enter a whole number here:")


def main():

    try:
        user_number = int((user_input))

        for x in range(user_number):
            print("{} = {}".format(x, x**2))
    except Exception:
        print("Invalid entry :(")


if __name__ == "__main__":
    main()
