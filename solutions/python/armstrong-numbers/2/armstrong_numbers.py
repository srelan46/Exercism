"""Module for checking Armstrong numbers."""


def is_armstrong_number(number):
    """Return True if number is an Armstrong number, otherwise False."""
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number