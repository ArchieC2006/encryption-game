import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    with st.expander("instructions"):  # todo: capitalise
        st.text(
            "The aim of the game is to convert the ciphertext back into the plaintext by \nguessing the "
            "substitution cipher and inputting it into the chart")  # todo: improve this using st.markdown
    st.subheader(ciphertext)  # todo: probably worth just having st.write


# todo: move dataframe to variable before data editor
#  pass in an index parameter i.e. index = ["name"]
# todo: rename the index (df.index.names = ["name"])
def user_input():
    edited_chart = st.data_editor(pd.DataFrame(
        [{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input[0]

# todo: add frequency analysis graph
