"Create an implementation of the rotational cipher, also sometimes called the Caesar cipher."
def rotate(text: str, key: int) -> str:
    """Rotate ASCII letters using a Caesar cipher."""

    result = []

    for character in text:
        if "a" <= character <= "z":
            rotated = chr(
                ord("a") + (ord(character) - ord("a") + key) % 26
            )
            result.append(rotated)

        elif "A" <= character <= "Z":
            rotated = chr(
                ord("A") + (ord(character) - ord("A") + key) % 26
            )
            result.append(rotated)

        else:
            result.append(character)

    return "".join(result)