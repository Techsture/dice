#!/usr/bin/env python3

# How many tries will it take to get `1, 2, 3, 4, 5, 6` in a row?
# Maths says 6^6 (46,656) tries.

# TODO: Set this up so it continues to execute, and calculate the running average.

from random import randint


def roll():
    die_roll = randint(1, 6)
    print(die_roll)
    return die_roll


def main():
    success = False
    counter = 0
    while success is False:
        counter += 1
        print("\n")
        if roll() == 1:
            if roll() == 2:
                if roll() == 3:
                    if roll() == 4:
                        if roll() == 5:
                            if roll() == 6:
                                success = True
    print("Success!  It took {0} tries.".format(counter))
    exit()


if __name__ == '__main__':
    main()
