from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


model =ChatOllama(model="llama3.2:3b")

prompt = PromptTemplate.from_template("Tell me the key achivements of {name} in 4 bullet points as Technical Trainer at Zensar Technologies.")


chain = prompt | model  #LCEL

response = chain.invoke({"name": "Sharad Rajore"})

print(response.content)