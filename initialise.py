import random
import json


def get_plaintext():
    with open("plaintext.json", "r") as pt:
        text = json.load(pt)
        plaintext = random.choice(text["plaintexts"])
        return plaintext.upper()


def random_alphabet():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    randomised = list(alphabet)
    # todo: both the above lines can be a single line comprehension
    random.shuffle(randomised)
    substitution_cipher = {key: value for key, value in zip(alphabet, "".join(randomised))}
    return substitution_cipher


def encrypt(plaintext, substitution_cipher):
    ciphertext = ""
    for letter in plaintext:
        if 65 <= ord(letter) <= 90:
            new_letter = substitution_cipher[letter]
            ciphertext += new_letter
        # todo: just alter letter
        else:
            ciphertext += letter
    return ciphertext
