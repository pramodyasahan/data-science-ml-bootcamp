import streamlit as st

st.title('Streamlit Widgets')

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello {name}")