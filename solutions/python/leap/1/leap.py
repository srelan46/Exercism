"Check if a year is a leap year or not"
def leap_year(year):
    """
    Check if a year is leap or not
    Input: year(int)
    Output: True if leap year else False
    """
    if year%4==0:
        if year%100==0:
            return year%400==0
        return True
    return False