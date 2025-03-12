import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter some Text")

if st.button("Show text"):
    st.write(f"You entered: {user_input}")