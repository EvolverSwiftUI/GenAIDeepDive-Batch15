import streamlit as st

st.title("Hello, Streamlit!")

st.header("This is a simple Streamlit app.")

st.write("Streamlit makes it easy to create web apps for data science and machine learning.")

name = st.text_input("Enter some text:", key="user_input")

if name:
    st.write(f"You entered: {name}")
    
col1,col2 =st.columns(2)

with col1:
    st.write("This is column 1") 
    st.button("Left Button", key="btn1") 
    
with col2:
    st.write("This is column 2") 
    st.button("Right Button", key="btn2")
    
    
if st.button("Send balloons!"):
    st.balloons()
    
      
