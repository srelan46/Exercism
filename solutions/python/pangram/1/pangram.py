"Calculates if sentence is a pangram"
def is_pangram(sentence):
    """
    Calculate if sentense is a pangram
    Input: sentence(string)
    Output: True if sentence is a pangram else False
    """
    ch = set()
    for character in sentence.lower():
        if character.isalpha():
            ch.add(character)  # Add the letter itself
    return len(ch)==26