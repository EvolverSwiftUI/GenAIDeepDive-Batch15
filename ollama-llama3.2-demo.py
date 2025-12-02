from langchain_ollama import ChatOllama

#from dotenv import load_dotenv

#load_dotenv()

#llm = ChatOllama(model="llama3.2:3b")

llm = ChatOllama(model="phi3:3.8b")

response = llm.invoke(" What is the capital of India?")

print(response.content)