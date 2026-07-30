"Create an implementation of the rotational cipher, also sometimes called the Caesar cipher."
def create_char_map(char_map: dict) -> dict:
    "create a dictionary for the mappings"
    for i in range(0,26):
        char_map[chr(ord('a')+i)] = i
    return char_map
def rotate(text: str, key: int)->str:
    "Rotates the string according to Caesar cipher."
    char_map = {}
    create_char_map(char_map)
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                ch=ch.lower()
                result+=chr(ord('a')+((char_map[ch]+key)%26)).upper()
            else:
                result+=chr(ord('a')+((char_map[ch]+key)%26))
        else:
            result+=ch
    return result