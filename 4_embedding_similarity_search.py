from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)  # 3072



documents=[
    "Virat kohli is a great cricketer.",
    "Sachin Tendulkar is a legendary batsman.",
    "Messi is a world-renowned footballer.",
]

query= "tell me about Sachin Tendulkar"

doc_embedding = embeddings.embed_documents(documents)

query_embedding = embeddings.embed_query(query)

similarity_score = cosine_similarity([query_embedding],doc_embedding)

print("Query:",query)
print("Similarity Score:",similarity_score)
print("Most Similar Document:",documents[similarity_score.argmax()])
print("Most Similar Document Score:",similarity_score.max())


#-----------------------------------------------
print("--------------------------------------------------")
from sklearn.metrics.pairwise import euclidean_distances

similarity_score = euclidean_distances([query_embedding], doc_embedding)
# Note: Lower values = more similar (opposite of cosine)
print("Most Similar Document:", documents[similarity_score.argmin()])