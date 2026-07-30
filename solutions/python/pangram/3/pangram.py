"Calculates if sentence is a pangram"
def is_pangram(sentence):
    """
    Calculate if sentense is a pangram
    Input: sentence(string)
    Output: True if sentence is a pangram else False
    """
    unique_letters = {character for character in sentence.lower() if character.isalpha()}
    return len(unique_letters) == 26