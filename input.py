import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    # warning probably isn't the best way to display this. Also we probably
    # don't need to have the "cipher text is"
    # todo: add in a st.expander with instructions and also use st.header(ciphertext)
    st.warning(f"ciphertext is: \"{ciphertext}\"")


# todo: move dataframe to variable before data editor
# todo: pass in an index parameter i.e. index = ["name"]
# todo: rename the index (df.index.names = ["name"])
def user_input():
    edited_chart = st.data_editor(pd.DataFrame(
        [{chr(a): "-" for a in range(65, 91)}]))
    users_input = edited_chart.to_dict("records")
    return users_input[0]

# todo: add frequency analysis graph, st.expander with title like hint
