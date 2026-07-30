def validTriangle(sides):
    if len(sides)>3:
        raise ValueError("sides must be less than equal to 3")
    if sides[0]+sides[1]+sides[2] <=0:
        return False
    if sides[0]+sides[1]<sides[2] or sides[1]+sides[2]<sides[0] or sides[0]+sides[2]<sides[1]:
        return False
    return True
        
def equilateral(sides):
    return validTriangle(sides) and sides[0]==sides[1]==sides[2]

def isosceles(sides):
    return validTriangle(sides) and (sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2])


def scalene(sides):
    return validTriangle(sides) and sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2]
