"Calculates if sentence is a pangram"
def is_pangram(sentence):
    """
    Calculate if sentense is a pangram
    Input: sentence(string)
    Output: True if sentence is a pangram else False
    """
    unique_letters = set()
    for character in sentence.lower():
        if character.isalpha():
            unique_letters.add(character)  # Add the letter itself
    return len(unique_letters)==26