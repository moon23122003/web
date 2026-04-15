#Add two no using streamlit 
import streamlit as st
st.title("welcome to my page")
name=st.text_input("Enter the name")
if name:
       st.write(f"hello,{name}!")
       st.success()
