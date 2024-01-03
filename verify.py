import streamlit as st


def get_new_plaintext(ciphertext, user_input):
    new_plaintext = ""
    for letter in ciphertext:
        if 65 <= ord(letter) <= 90:
            new_letter = user_input[letter]
            new_plaintext += new_letter.upper()
        # todo: just alter letter
        else:
            new_plaintext += letter
    return new_plaintext


def result(new_plaintext, plaintext):
    if new_plaintext == plaintext:
        st.success("You are correct")
        st.balloons()
    # todo: either get rid of "The new plaintext is" or have it on a separate
    #  line above the decryption
    #  alternative way of saying it that would be more correct is "result of decryption"
    st.write(f"The new plaintext is {new_plaintext}")
