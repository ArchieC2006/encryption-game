import numpy as np, streamlit as st


def get_new_substitution_cipher(ciphertext, substitution_cipher):
    for key, value in substitution_cipher.items():
        if value not in ciphertext:
            substitution_cipher[key] = "-"
    st.text(substitution_cipher)
    return substitution_cipher

def result(new_substitution_cipher, user_input):
    if new_substitution_cipher == user_input[0]:
        st.text("you are correct")
    else:
        st.text("input what you think the substitution cipher is")
