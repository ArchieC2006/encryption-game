import streamlit as st
import pandas as pd


def output_ciphertext(ciphertext):
    with st.expander("Instructions"):
        st.markdown(
            '''The aim of the game is to convert the ciphertext back into the plaintext, you can do this by guessing
            the substitution cipher and inputting it into the chart''')
    st.write(ciphertext)


def user_input():
    chart = pd.DataFrame([{chr(a): "-" for a in range(65, 91)}], ["Substitution Cipher"])
    chart.index.names = ["Alphabet"]
    edited_chart = st.data_editor(chart)
    users_input = edited_chart.to_dict("records")
    return users_input[0]


def plot_graph(ciphertext):
    counter = {chr(i): 0 for i in range(65, 91)}
    for i in ciphertext:
        if i in counter:
            counter[i] += 1
    data = pd.DataFrame(list(counter[chr(i)] for i in range(65, 91)), [chr(i) for i in range(65, 91)])
    st.bar_chart(data)
