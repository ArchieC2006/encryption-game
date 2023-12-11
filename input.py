import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    with st.expander("instructions"):
        st.text("The aim of the game is to convert the ciphertext back into the plaintext by \nguessing the "
                "substitution cipher and inputting it into the chart")
    st.subheader(ciphertext)


# todo: move dataframe to variable before data editor
# todo: pass in an index parameter i.e. index = ["name"]
# todo: rename the index (df.index.names = ["name"])
def user_input():
    edited_chart = st.data_editor(pd.DataFrame(
        [{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input[0]

# todo: add frequency analysis graph, st.expander with title like hint
