import streamlit as st


# This doesn't work as it is supposed to
# Issue 1:
# Need to capitalise user letters


def get_new_plaintext(ciphertext, user_input):
    new_plaintext = ""
    for letter in ciphertext:
        if 65 <= ord(letter) <= 90:
            new_letter = user_input[letter]
            new_plaintext += new_letter
        else:
            new_plaintext += letter
    return new_plaintext


def result(new_plaintext, plaintext):
    # todo: .upper()?
    # todo: capitalise messages (as in "You are correct")
    # todo: probably don't need the else, easier to just have the new
    #       plaintext always shown
    if new_plaintext == plaintext:
        st.success("you are correct")
        st.success(f"the plaintext was \"{new_plaintext}\"")
        st.balloons()
    else:
        st.warning("input what you think the substitution cipher is")
        st.warning(f"the new plaintext is {new_plaintext}")
