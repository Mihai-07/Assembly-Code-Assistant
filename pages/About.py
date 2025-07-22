import streamlit as st

with open("README.md") as file:
    text = "\n".join([
        line.strip() for line in file.readlines()
    ])

st.markdown(text)
