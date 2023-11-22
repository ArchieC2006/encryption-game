import initialise, input, verify, streamlit as st, pandas as pd, numpy as np

plaintext = initialise.get_plaintext()
substitution_cipher = initialise.get_substitution_cipher()
ciphertext = initialise.encrypt(plaintext, substitution_cipher)
input.output_ciphertext(ciphertext)
user_input = input.user_input()
st.text(user_input[0])
new_substitution_cipher = verify.get_new_substitution_cipher(ciphertext, substitution_cipher)
verify.result(new_substitution_cipher, user_input)