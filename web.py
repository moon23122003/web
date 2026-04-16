#Add two no using streamlit 
import streamlit as st

# Sidebar menu
page = st.sidebar.selectbox("Choose page", ["Home", "Loading", "Wait"])

# Home Page
import streamlit as st
st.title("welcome to my page")
name=st.text_input("Enter the name")
if name:
       st.write(f"hello,{name}!")

# Loading Page
import streamlit as st
import time#core python

with st.spinner("Loding...."):
       time.sleep(5)
with st.sidebar:
       st.write("Show the above options")
       
       
st.title("health care prediction project")

# Wait Page
import streamlit as st
import time#core python
with st.spinner("Loding...."):
       time.sleep(5)
st.title("SMART DIAGNOSIS SYSTEM")
