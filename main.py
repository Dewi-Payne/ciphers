# Some basic ciphers as part of practicing python
# 2021, Dewi Payne

def caesar(message: str, key: int):
    # Caesar cipher - a basic cipher that shifts the message by a given number of letters.
    # Works both ways if you know the key, simply swap its sign (+/-) to decrypt.

    # TODO - deal with handling capital letters
    final_message = ""
    for character in message.lower():
        if character.isalpha():
            final_message += chr((ord(character) + key - 97) % 26 + 97)
        else:
            final_message += character
    return final_message


def vigenere(message: str, key: str):
    # Vigenère cipher - slightly more advanced cipher that uses caesar ciphers to shift a message by
    # a different number for each character based on the key.

    while len(key) < len(message):
        key += key

    key = key[:len(message)].lower()

    final_message = ""

    for i, character in enumerate(message.lower()):
        if character.isalpha():
            final_message += chr((ord(character) + ord(key[i]) - (97 * 2)) % 26 + 97)
        else:
            final_message += character
    return final_message

if __name__ == "__main__":
    test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    print(caesar(test_text, -2))
    print(vigenere(test_text, "king"))
