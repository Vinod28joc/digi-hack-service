import streamlit as st

st.title('👽 Digi Hack Service')

st.info('This service is build to summarise the customer intraction.')

with col1:
    text_input = st.text_input(
        "Enter Customer id 👇",
        placeholder="eg:12345",
    )

with col2:
    text_input = st.text_input(
        "Enter Email address 👇",
        placeholder="eg:brian@gmail.com",
    )
