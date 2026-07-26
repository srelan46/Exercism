"""Functions for validating and classifying triangles."""

def valid_triangle(sides):
    """Return True if the three sides form a valid triangle."""
    if len(sides)>3:
        raise ValueError("sides must be less than equal to 3")
    if sides[0]+sides[1]+sides[2] <=0:
        return False
    if sides[0]+sides[1]<sides[2] or sides[1]+sides[2]<sides[0] or sides[0]+sides[2]<sides[1]:
        return False
    return True
        
def equilateral(sides):
    """Return True if the triangle is equilateral."""
    return valid_triangle(sides) and sides[0]==sides[1]==sides[2]

def isosceles(sides):
    """Return True if the triangle is isosceles."""
    return valid_triangle(sides) and (sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2])


def scalene(sides):
    """Return True if the triangle is scalene."""
    return valid_triangle(sides) and sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2]
