import streamlit as st

import initialise
import input
import verify

# todo: look at st.set_page_config to improve how the tab looks
# todo: add a st.title()
if "plaintext" not in st.session_state:
    st.session_state.plaintext = initialise.get_plaintext()
plaintext = st.session_state.plaintext
st.text(plaintext)  # todo: have this as a warning so you remember to remove it
if "substitution_cipher" not in st.session_state:
    st.session_state.substitution_cipher = initialise.random_alphabet()
substitution_cipher = st.session_state.substitution_cipher
ciphertext = initialise.encrypt(plaintext, substitution_cipher)

input.output_ciphertext(ciphertext)
user_input = input.user_input()
st.text(user_input)  # todo: have this as a warning so you remember to remove it

new_plaintext = verify.get_new_plaintext(ciphertext, user_input)
verify.result(new_plaintext, plaintext)
