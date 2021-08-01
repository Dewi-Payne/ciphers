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
    id = 0
    for character in message.lower():
        if character.isalpha():
            # Similar to how the Caesar cipher works above, the difference being that we are adding an ASCII ordinal
            # value instead of a numerical key, so we need to remove a further 97 to translate the character's value to
            # a number from 0 to 25.
            final_message += chr((ord(character) + ord(key[id]) - (97 * 2)) % 26 + 97)
            id += 1
        else:
            final_message += character
    return final_message


def encrypt():
    input = inputbox.get("1.0", "end").rstrip()
    key = keybox.get("1.0", tk.END).rstrip()

    if i.get() == 1:
        output = caesar(input, key)

    if i.get() == 2:
        output = vigenere(input, key)

    outputbox.delete(1.0, "end")
    outputbox.insert(1.0, output)


if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()

    inputlabel = tk.Label(root, text="Input text: ")
    keylabel = tk.Label(root, text="Key: ")
    outputlabel = tk.Label(root, text="Output text: ")

    inputbox = tk.Text(root, width=30, height=2, wrap="char")
    keybox = tk.Text(root, width=30, height=1, wrap="char")
    outputbox = tk.Text(root, width=30, height=2, wrap="char")

    i = tk.IntVar()
    o1 = tk.Checkbutton(root, text="Caesar shift cipher", variable=i, onvalue=1)
    o2 = tk.Checkbutton(root, text="Vigenère cipher", variable=i, onvalue=2)
    b1 = tk.Button(root, text="Encrypt", command=lambda: encrypt())

    inputlabel.grid(row=0, column=0)
    keylabel.grid(row=1, column=0)
    outputlabel.grid(row=2, column=0)

    inputbox.grid(row=0, column=1)
    keybox.grid(row=1, column=1)
    outputbox.grid(row=2, column=1)

    o1.grid(row=3, column=0)
    o2.grid(row=3, column=1)
    b1.grid(row=4, column=0)

    root.mainloop()
