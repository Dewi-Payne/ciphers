# Some basic ciphers as part of practicing python
# 2021, Dewi Payne

def caesar(message: str, key: int):
    # Caesar cipher - a basic cipher that shifts the message by a given number of letters.
    # Works both ways if you know the key, simply swap its sign (+/-) to decrypt.

    # TODO - deal with handling capital letters
    final_message = ""
    for character in message:
        final_message += chr((ord(character) + key - 97) % 26 + 97)
    return final_message


def vigenere(message: str, key: int):
    # Vigenère cipher - slightly more advanced cipher that uses caesar ciphers to shift a message by
    # a different number for each character.
    # TODO
    pass


if __name__ == "__main__":
    print(caesar("oguucig", -2))
    print(vigenere("message", 2))
