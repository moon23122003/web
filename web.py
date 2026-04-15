#Add two no using streamlit 
import streamlit as st
st.title("welcome to my page")
name=st.text_input("Enter the name")
if name:
       st.write(f"hello,{name}!")
gender=st.text_input("Enter the gender",gender(female/male)
       if gender:
              st.selectbox("Enter gender",gender(female/male))
if st.button("login"):
      st.success()
