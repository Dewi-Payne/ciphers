def caesar(message: str, key: int):
    final_message = ""
    for character in message:
        final_message += chr((ord(character) + key - 97) % 26 + 97)
    return final_message


def vigenere(message: str, key: int):
    pass


if __name__ == "__main__":
    print(caesar("message", 2))
