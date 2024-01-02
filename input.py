import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    with st.expander("Instructions"):
        st.markdown(
            '''The aim of the game is to convert the ciphertext back into the plaintext, you can do this by guessing
            the substitution cipher and inputting it into the chart''')
    st.write(ciphertext)


def user_input():
    chart = pd.DataFrame([{chr(a): "-" for a in range(65, 91)}],
                         ["Substitution Cipher"])
    chart.index.names = ["Alphabet"]
    edited_chart = st.data_editor(chart)
    users_input = edited_chart.to_dict("records")
    return users_input[0]


def plot_graph(ciphertext):
    alphabet = zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    frequency = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3,
                 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]
    frequency_data = pd.DataFrame(frequency, alphabet)
    st.bar_chart(frequency_data)
    counter = {chr(i): ciphertext.count(chr(i)) for i in range(65, 91)}
    counter_data = pd.DataFrame(list(counter[chr(i)] for i in range(65, 91)),
                                [chr(i) for i in range(65, 91)])
    st.bar_chart(counter_data)
