import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    st.warning(f"ciphertext is: \"{ciphertext}\"")


def user_input():
    edited_chart = st.data_editor(pd.DataFrame([{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input[0]

# todo: add frequency analysis graph
