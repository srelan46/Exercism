def classify(number:int)->str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    aliquot_sum = 1
    for index in range(2,number//2+1):
        if number%index == 0:
            aliquot_sum +=index
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
