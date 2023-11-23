# todo: fix imports
import numpy
import streamlit as st, pandas as pd, numpy as np


# This is fine, however st.text is possibly not the best option for this
# todo: look at the "API reference - Text elements" in the streamlit docs and
#       see if any of those are better suited
def output_ciphertext(ciphertext):
    st.text(f"ciphertext is: \"{ciphertext}\"")


# Very good, however it might be more convenient to return just the dictionary
# instead of the dictionary being contained in a list
# todo: improve return
def user_input():
    edited_chart = st.data_editor(
        pd.DataFrame([{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input

# todo: add frequency analysis graph
