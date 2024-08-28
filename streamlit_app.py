import datetime
import requests
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
date = st.date_input("Please select date 👇", value=None)

# st.button("Generate Summary") 
# st.button("Send email") 
# st.button("Reset", type="primary")

with st.form("my_form1"):
    submitted = st.form_submit_button("Generate Summary")
    if submitted:
        st.write("Generating the sumamry for Customer ID", text_input1)
        url = "https://api.freeapi.app/api/v1/public/randomuser/user/random"
        st.write("URL", url)
        response = requests.get(url)   
        st.write("Got the response.....")
        st.write("Response here", response.json())
        st.write("status", response)
        
with st.form("my_form2"):
    submitted = st.form_submit_button("Send email")
    if submitted:
        st.write("Email has been sent to Customer ID", text_input1)

with st.form("my_form3"):
    submitted = st.form_submit_button("Reset", type="primary")
    if submitted:
        text_input1 = None
        text_input2 = None
        date = None
        st.write("filed has been Reseted")








