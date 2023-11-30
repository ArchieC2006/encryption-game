import random

import streamlit as st


def get_plaintext():
    with open("plaintext.txt", "r") as pt:
        n = random.randint(0, 12)
        for _ in range(1, n):
            pt.readline()
        return pt.readline().upper()


def random_alphabet():
    alphabet = [chr(i) for i in range(65, 91)]
    randomised = ""
    while alphabet:
        randomised += alphabet.pop(random.randint(0, len(alphabet) - 1))
    substitution_cipher = {key: value for key, value in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", randomised)}
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
