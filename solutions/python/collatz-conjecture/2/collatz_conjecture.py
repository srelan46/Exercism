"""Exercise solutions for Collatz Conjecture."""


def steps(number):
    """Return the number of Collatz steps needed to reach 1."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1

    return count