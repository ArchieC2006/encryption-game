def get_plaintext():
    plaintext = "aBc d".upper()
    return plaintext


def get_substitution_cipher():
    substitution_cipher = {"A": "X",
                           "B": "N",
                           "C": "F",
                           "D": "R",
                           "E": "D",
                           "F": "B",
                           "G": "Q",
                           "H": "S",
                           "I": "A",
                           "J": "L",
                           "K": "I",
                           "L": "C",
                           "M": "H",
                           "N": "J",
                           "O": "V",
                           "P": "K",
                           "Q": "T",
                           "R": "P",
                           "S": "G",
                           "T": "M",
                           "U": "E",
                           "V": "W",
                           "W": "Y",
                           "X": "O",
                           "Y": "Z",
                           "Z": "U"
                           }
    return substitution_cipher


def encrypt(plaintext, substitution_cipher):
    ciphertext = []
    for letter in plaintext:
        if 65 <= ord(letter) <= 90:
            new_letter = substitution_cipher[letter]
            ciphertext.append(new_letter)
        else:
            ciphertext.append(letter)
    return "".join(ciphertext)
