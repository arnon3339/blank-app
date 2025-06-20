import streamlit as st

st.title("Hello World")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Input box
name = st.text_input("Enter your name")

# Response
if name:
    st.write(f"Welcome, {name}!")