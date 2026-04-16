#Add two no using streamlit 
import streamlit as st

# Sidebar menu
page = st.sidebar.selectbox("Choose page", ["Home", "Loading", "Wait"])

# Home Page
if page == "Home":
    st.title("Welcome to my page")
    name = st.text_input("Enter your name")
    if name:
        st.write(f"hello, {name}!")

# Loading Page
elif page == "Loading":
    st.title("Loading Page")
    st.write("Loading... please wait")

# Wait Page
elif page == "Wait":
    st.title("Wait Page")
    st.write("Processing... hold on")
