import streamlit as st
from backend import get_available_models, find_achievements

# 1. Page configuration
st.set_page_config(page_title="Achivement Finder", page_icon="🤖", layout="centered")

# 2.Header and Discription
st.title("🤖 Achivement Finder")
st.markdown(" This AI tool helps you to find the key professional highlights of any individual")

# 3. Sidebar for Model Selection
with st.sidebar:
    st.header("Model Selection")
    model_name = st.selectbox("Choose a model:", get_available_models())
    st.info("Ensure Ollama is running locally with the selected model.")
    
# 4. User Input
# We need two inputs now to make it generic : Who is it ? and What is their role?
col1, col2 = st.columns(2)

with col1:
    person_name = st.text_input("Enter the person's name:", key="person_name")


with col2:
    person_role = st.text_input("Enter the person's role:", key="person_role")
    
# 5. Logic to generate Achivements
if st.button("Find Achievements",type="primary"):
    if person_name and person_role:
        with st.spinner("Searching internal knowledge base for {person_name}"):
            result = find_achievements(model_name, person_name, person_role)
            
            if result['success']:
                #Display output
                st.markdown("----")
                st.subheader(f" Result for {person_name} ")
                st.success(result['message'])
                st.markdown(result['content'])
            else:
                st.error(result['message'])
    else:
        st.warning("Please provide both the person's name and role to proceed.")
