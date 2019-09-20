#!/usr/bin/env python3

# How many tries will it take to get `1, 2, 3, 4, 5, 6` in a row?
# Maths says 6^6 (46,656) tries.

# TODO: Something is wrong with him I'm calculating the running average.  The average seems to be approaching zero.
# I'm doing something fundamentally wrong.

from math import ceil
from random import randint


def roll():
  die_roll = randint(1, 6)
  return die_roll


def main():
  running_average = 0
  success_counter = 0
  tries_counter = 0
  while True:
    tries_counter += 1
    if roll() == 1:
      if roll() == 2:
        if roll() == 3:
          if roll() == 4:
            if roll() == 5:
              if roll() == 6:
                success_counter += 1
                if running_average > 0:
                  print("({} + {}) / {}".format(running_average, tries_counter, success_counter))
                  running_average = ceil((running_average + tries_counter) / success_counter)
                  print("Running average is {}.".format(running_average))
                else:
                  print("({} + {}) / {}".format(running_average, tries_counter, success_counter))
                  running_average = ceil(tries_counter / success_counter)
                  print("Running average is {}.".format(running_average))
                tries_counter = 0
  exit()


if __name__ == '__main__':
  main()
