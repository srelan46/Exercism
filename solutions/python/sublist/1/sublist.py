"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    "Return is list one is sublist, superlist , equal or unequal to list two"
    if list_one==list_two:
        return EQUAL
    if is_sublist(list_two,list_one):
        return SUPERLIST
    if is_sublist(list_one,list_two):
        return SUBLIST
    return UNEQUAL

def is_sublist(small,large):
    "return is small is a sublist of large"
    length = len(small)
    for index in range(len(large)-length+1):
        if large[index:index+length]==small:
            return True
    return False
                
