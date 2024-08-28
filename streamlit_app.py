import datetime
import streamlit as st

st.title('👽 Digi Hack Service')

st.info('This service is build to summarise the customer intraction.')

col1, col2 = st.columns(2)

with col1:
    text_input1 = st.text_input(
        "Enter Customer id 👇",
        placeholder="eg:12345",
    )

with col2:
    text_input2 = st.text_input(
        "Enter Email address 👇",
        placeholder="eg:brian@gmail.com",
    )
d = st.date_input("When's your birthday", value=None)

# st.button("Generate Summary") 
# st.button("Send email") 
# st.button("Reset", type="primary")

with st.form("my_form1"):
    submitted = st.form_submit_button("Generate Summary")
    if submitted:
        st.write("Generating the sumamry for Customer ID", text_input1, "\n\n Email body here")

with st.form("my_form2"):
    submitted = st.form_submit_button("Send email")
    if submitted:
        st.write("Email has been sent to Customer ID", text_input1)

with st.form("my_form3"):
    submitted = st.form_submit_button("Reset", type="primary"")
    if submitted:
        st.write("filed has been Reseted")








