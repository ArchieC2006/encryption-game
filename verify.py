import streamlit as st


def get_new_plaintext(ciphertext, user_input):
    new_plaintext = ""
    for letter in ciphertext:
        if 65 <= ord(letter) <= 90:
            new_letter = user_input[letter]
            new_plaintext += new_letter.upper()
        else:
            new_plaintext += letter
    return new_plaintext


def result(new_plaintext, plaintext):
    if new_plaintext == plaintext:
        st.success("You are correct")
        st.balloons()
    st.warning(f"The new plaintext is {new_plaintext}") # todo: st.write
