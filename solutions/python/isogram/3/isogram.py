"check if a word or phrase is an isogram or not"
def is_isogram(phrase):
    "check if a word/phrase is an isogram or not"
    unique_letters=set()
    for char in phrase.lower():
        if char in {" ","-"}:
            continue
        if char in unique_letters:
            return False
        unique_letters.add(char)
    return True