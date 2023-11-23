import random


# looks good
# todo: use .txt file(s) to have random plaintexts
# context manager, file mode: read
# string concatenation with filename and random number

def get_plaintext():
    plaintext = "aBc d".upper()
    return plaintext


# Quite bloated, consider using comprehension instead:
# substitution_cipher = {key: value for key, value in
#                        zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
#                            "XNFRDBQSALICHJVKTPGMEWYOZU")}
# todo: refactor this method to be neater
# todo: replace "XNFRDBQSALICHJVKTPGMEWYOZU" with random substitution

def random_alphabet():
    alphabet = [chr(i) for i in range(65, 91)]
    randomised = ""
    while alphabet:
        randomised += alphabet.pop(random.randint(0, len(alphabet) - 1))
    return randomised


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


# looks good, instead of a list and appends, consider just using a string and +
def encrypt(plaintext, substitution_cipher):
    ciphertext = []
    for letter in plaintext:
        if 65 <= ord(letter) <= 90:
            new_letter = substitution_cipher[letter]
            ciphertext.append(new_letter)
        else:
            ciphertext.append(letter)
    return "".join(ciphertext)
