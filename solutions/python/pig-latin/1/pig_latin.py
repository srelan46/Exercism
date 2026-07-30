vowels = {"a", "e", "i", "o", "u"}


def translate_word(word):
    # Rule 1: starts with a vowel sound
    if word.startswith(("xr", "yt")) or word[0] in vowels:
        return word + "ay"

    # Find the first vowel sound.
    for index, letter in enumerate(word):
        # Rule 3: treat "qu" as part of the consonant cluster.
        if word[index:index + 2] == "qu":
            split_index = index + 2
            return word[split_index:] + word[:split_index] + "ay"

        # Rule 4: "y" acts as a vowel after the first character.
        if letter == "y" and index > 0:
            return word[index:] + word[:index] + "ay"

        # Rule 2: move consonants before the first vowel.
        if letter in vowels:
            return word[index:] + word[:index] + "ay"

    return word + "ay"


def translate(text):
    return " ".join(translate_word(word) for word in text.split())