import streamlit as st

import initialise
import input
import verify

# todo: Codecademy lesson 5: markdown, use this to add a readme.md doc
# todo: theming (https://docs.streamlit.io/library/advanced-features/theming)
# todo: use forms and add in a scoring system (https://docs.streamlit.io/library/advanced-features/forms)
# todo: add typehints
# todo: (ny) Get a perfect flake8, then pylint score

st.set_page_config("The Encryption Game", "🔎")
st.title("The Encryption Game")

# todo: treat st.session_state as dictionary
if "plaintext" not in st.session_state:
    st.session_state.plaintext = initialise.get_plaintext()
plaintext = st.session_state.plaintext
print(plaintext)
if "substitution_cipher" not in st.session_state:
    st.session_state.substitution_cipher = initialise.random_alphabet()
substitution_cipher = st.session_state.substitution_cipher
ciphertext = initialise.encrypt(plaintext, substitution_cipher)

input.plot_graph(ciphertext)
input.output_ciphertext(ciphertext)
user_input = input.user_input()
print(user_input)

new_plaintext = verify.get_new_plaintext(ciphertext, user_input)
verify.result(new_plaintext, plaintext)
