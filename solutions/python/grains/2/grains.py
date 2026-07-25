def square(number):
    """
    Takes in number as input and returns the number of grains on each squareboard of chessboard
    Input:
        Square number
    Output:
        Number of grains on each squareboard of chessboard
    """
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    """
    Returns the total number of grains on the chessboard
    """
    return 2**64-1
