import datetime
import streamlit as st

st.title('👽 Digi Hack Service')

st.info('This service is build to summarise the customer intraction.')

col1, col2, col3 = st.columns(3)

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

with col3:
d = st.date_input("When's your birthday", , value=None)

