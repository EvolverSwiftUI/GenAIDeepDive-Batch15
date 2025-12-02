from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

response = llm.invoke("Tell me the key achivements of Virat Kohli in 4 bullet points.")  #10000

 
print(response.content)