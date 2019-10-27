# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program loops to get to the number entered and adds the numbers


def main():
    # variables
    answer = 0
    counter = 0

    # input
    number = int(input("Enter a number to loop it and add its results: "))

    # process & output
    while counter < number:
        answer = answer + counter
        counter = counter + 1
    print("The sum of all the numbers in {}".format(answer))


if __name__ == "__main__":
    main()
