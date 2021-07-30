# Some basic ciphers as part of practicing python
# 2021, Dewi Payne

def caesar(message: str, key: int):
    # Caesar cipher - a basic cipher that shifts the message by a given number of letters.
    # Can also be used to decipher text with a known key

    final_message = ""
    for character in message.lower():
        if character.isalpha():  # Checks to avoid attempting to encrypt punctuation
            # We convert our character to its ASCII value to be able to easily increment it by our key.
            # In ASCII the lowercase alphabet begins at 97, so to be able to loop around to the start we need to
            # subtract 97 from the ord value after adding our key, before performing modulo 26. then we add 97
            # back to the value to get to the desired ASCII value and translate that value back into a character.
            final_message += chr((ord(character) + key - 97) % 26 + 97)
        else:
            final_message += character
    return final_message


def vigenere(message: str, key: str):
    # Vigenère cipher - slightly more advanced cipher that shifts a message by
    # a different number for each character based on a key.

    # Here we stretch our key to the same length as our message.
    while len(key) < len(message):
        key += key
    key = key[:len(message)].lower()

    final_message = ""
    for i, character in enumerate(message.lower()):
        if character.isalpha():
            # Similar to how the Caesar cipher works above, the difference being that we are adding an ASCII ordinal
            # value instead of a numerical key, so we need to remove a further 97 to translate the character's value to
            # a number from 0 to 25.
            final_message += chr((ord(character) + ord(key[i]) - (97 * 2)) % 26 + 97)
        else:
            final_message += character
    return final_message

if __name__ == "__main__":
    test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    print(caesar(test_text, -2))
    print(vigenere(test_text, "king"))
    print(vigenere("ATTACKATDAWN", "LEMON"))
