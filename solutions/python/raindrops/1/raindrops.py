"Raindrops a complex version of FizzBuzz"
def convert(number):
    """
    Based on the instructions return the result string
    """
    result_string = ""
    if number%3==0:
        result_string+="Pling"
    if number%5==0:
        result_string+="Plang"
    if number%7==0:
        result_string+="Plong"
    if number%3!=0 and number%5!=0 and number%7!=0:
        result_string+=str(number)
    return result_string
