# todo: fix imports
import numpy as np, streamlit as st


# This doesn't work as it is supposed to
# Issue 1:
# the substitution cipher should be reversed for the user (A:X will become X:A)
# Issue 2:
# Need to capitalise user letters
# Issue 3:
# Comparing the dictionaries will be tricky as sometimes a letter might not appear
#
# The best way to approach this will be to apply the users substitution to the
# ciphertext and then compare it to the plaintext. By doing this we can also
# display the decrypted ciphertext so the user can see what their current
# guess results in
# todo: add -
#  decrypting the ciphertext using the users guess,
#  show the result of decrypting with the users guess,
#  verify the decryption using the plaintext

def get_new_substitution_cipher(ciphertext, substitution_cipher):
    for key, value in substitution_cipher.items():
        if value not in ciphertext:
            substitution_cipher[key] = "-"
    st.text(substitution_cipher)
    return substitution_cipher


def result(new_substitution_cipher, user_input):
    if new_substitution_cipher == user_input[0]:
        st.text("you are correct")
        # todo: improve message, also add balloons
    else:
        st.text("input what you think the substitution cipher is")
