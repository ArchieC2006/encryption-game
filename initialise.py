import random
import json

import streamlit as st


def get_plaintext():
    with open("plaintext.json", "r") as pt:
        n = random.randint(0, 2)
        text = json.load(pt)
        plaintext = text[chr(65+n)]
        return plaintext.upper()


def random_alphabet():
    alphabet = [chr(i) for i in range(65, 91)]
    # this is very good use of while and pop,
    # however take a look at random.shuffle
    randomised = ""
    while alphabet:
        randomised += alphabet.pop(random.randint(0, len(alphabet) - 1))
    substitution_cipher = {key: value for key, value in
                           zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", randomised)}
    st.text(substitution_cipher)
    return substitution_cipher


def encrypt(plaintext, substitution_cipher):
    ciphertext = ""
    for letter in plaintext:
        if 65 <= ord(letter) <= 90:
            new_letter = substitution_cipher[letter]
            ciphertext += new_letter
        else:
            ciphertext += letter
    return ciphertext
