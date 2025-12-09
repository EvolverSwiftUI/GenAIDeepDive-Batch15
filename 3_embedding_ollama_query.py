from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OllamaEmbeddings(model="granite-embedding:latest")  # 3072

result = embeddings.embed_query("Delhi is the capital of India")

print(str(result))