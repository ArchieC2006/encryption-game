import numpy
import streamlit as st, pandas as pd,numpy as np


def output_ciphertext(ciphertext):
    st.text(f"ciphertext is: \"{ciphertext}\"")


def user_input():
    edited_chart = st.data_editor(pd.DataFrame([{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input
