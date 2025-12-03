import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# 1. Page configuration
st.set_page_config(page_title="Achivement Finder", page_icon="🤖", layout="centered")

# 2.Header and Discription
st.title("🤖 Achivement Finder")
st.markdown(" This AI tool helps you to find the key professional highlights of any individual")

# 3. Sidebar for Model Selection
with st.sidebar:
    st.header("Model Selection")
    model_name = st.selectbox("Choose a model:", ["phi3:3.8b", "llama3.2:3b"])
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
            try:
                #---------langchain login ---------
                llm= ChatOllama(model=model_name)
                
                # Dynamic Prompt Template : we pass BOTH variables into the template
                template ="""
                    Your are a helpful research assistant.
                    Please list the top 5 key achievements of {name} specifically in their role as {role}.
                    
                    Format the output as:
                    - A brief 1-sentance summery intro
                    - Bullet point list of achievements
                    - keep the tone professional
                
                """
                
                prompt = PromptTemplate.from_template(template)
                
                # Create the chain
                
                chain = prompt | llm  # LCEL
                
                # Invoke the chain with dictionary containing both variables
                
                response = chain.invoke({
                    'name': person_name,
                    'role': person_role
                })
                
                #Display output
                st.markdown("----")
                st.subheader(f" Result for {person_name} ")
                st.success("Data Retrieved Successfully!")
                st.markdown(response.content)
                
            except Exception as e:
                st.error(f" Error: Could not connect to Ollama.{e}")
    else:
        st.warning("Please provide both the person's name and role to proceed.")
                
                
                
                
            
            
        
        