# don't need redundant imports
# import statements should be separate for different modules,
# use commas in the case of:
# from module import class1, function1, function2, ...
# also remember the ordering:
# builtins e.g. datetime
# installs e.g. numpy
# custom e.g. my_module
# todo: fix imports (remove unused imports, separate lines, and ordering)
import initialise, input, verify, streamlit as st, pandas as pd, numpy as np

# looks good, however it would be neater to separate these into blocks, example:
#
# init_func1
# init_func2
# init_func3
#
# next_func1
# next_func2
#

# todo: separate into parts
plaintext = initialise.get_plaintext()
substitution_cipher = initialise.get_substitution_cipher()
ciphertext = initialise.encrypt(plaintext, substitution_cipher)

input.output_ciphertext(ciphertext)
user_input = input.user_input()
st.text(user_input[0])
new_substitution_cipher = verify.get_new_substitution_cipher(ciphertext, substitution_cipher)
verify.result(new_substitution_cipher, user_input)
