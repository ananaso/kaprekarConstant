#!/usr/bin/env python3
"""
Calculates and outputs the steps taken to reach Kaprekar's Constant given any
4-digit number. The only restrictions placed on the provided number is that it
contain at least two unique digits, otherwise a separate endstate is reached.

Author: Alden Davidson
Email: adavidson@pm.me
"""

KAPREKAR_CONSTANT = 6174

def get_starting_number():
    """
    Takes input from the user and ensures that it is valid.
    Valid means exactly 4 digits and no other characters.
    """
    starting_number = None
    while not starting_number:
        input_number = input("Enter a starting number: ")
        try:
            starting_number = int(input_number)
            if starting_number < 1000 or starting_number >= 10000:
                print("Please enter exactly 4 digits")
                starting_number = None
        except ValueError:
            if not input_number:
                print("You have to enter something...")
            else:
                print("Please enter only valid digits")
    return starting_number

def kaprekar_routine(input_num):
    """
    Completes a single iteration of the kaprekar routine.
    """
    original_num = str(input_num)
    small_first = int(''.join(sorted(original_num)))
    large_first = int(''.join(sorted(original_num, reverse=True)))
    iteration_output = large_first - small_first
    return iteration_output, large_first, small_first

if __name__ == "__main__":
    while True:
        STEP_COUNT = 0
        STARTING_NUMBER = get_starting_number()
        while True:
            STARTING_NUMBER, LARGE_SORT, SMALL_SORT = kaprekar_routine(
                STARTING_NUMBER)
            STEP_COUNT += 1
            # ensure small number is always printed with enough leading zeros
            print(LARGE_SORT, "-", f'{SMALL_SORT:04}', "=", STARTING_NUMBER)
            # Catch the normal endstate and break for another input
            if STARTING_NUMBER == KAPREKAR_CONSTANT:
                print("Iterations:", STEP_COUNT, "\n")
                break
            if STARTING_NUMBER == 0:
                print("Repdigits will always terminate at 0 after a single iteration\n")
                break
