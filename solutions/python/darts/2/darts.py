"Calculate the points scored in a single toss of a Darts game."
def score(point_x:int, point_y:int)->int:
    "Calculates the points based on where the dart is thrown"
    distance = point_x**2 + point_y**2
    if distance > 100:
        return 0
    if 25 < distance <= 100:
        return 1
    if 1 < distance <= 25:
        return 5
    return 10