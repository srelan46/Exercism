"Calculate the points scored in a single toss of a Darts game."
def score(x:int, y:int)->int:
    "Calculates the points based on where the dart is thrown"
    distance = x**2 + y**2
    if distance > 100:
        return 0
    elif 25 < distance <= 100:
        return 1
    elif 1 < distance <= 25:
        return 5
    return 10