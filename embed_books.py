import os, json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
from chromadb.config import Settings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


data_path = Path(r"C:\Users\neeha\Downloads\RAG_chatbot\data\merged_book_chunks.json")
chroma_path = "chroma_db"
collection_name = "book_chunks"
model = "all-MiniLM-L6-V2"



with open(data_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)


client = PersistentClient(path=chroma_path)


embed_fn = SentenceTransformerEmbeddingFunction(model_name=model)

existing_collections = [col.name for col in client.list_collections()]
if collection_name in existing_collections:
    client.delete_collection(name=collection_name)
collection = client.create_collection(name=collection_name, embedding_function=embed_fn)



documents = []
metadata = []
ids = []


for chunk in chunks:
    content = chunk.get("summary") or chunk.get("text")[:300]
    chunk_id = f"{chunk['book'].replace(' ', '_')}_{chunk['chunk_id']}"
    documents.append(content)
    ids.append(chunk_id)
    metadata.append({
        "book" : chunk["book"],
        "chapter" : chunk["chapter"],
        "chunk_id" : chunk["chunk_id"]
    })


print(f"Adding {len(documents)} documents to ChromaDB.. ")
collection.add(documents=documents,metadatas=metadata,ids=ids)

#client.persist()
print(f"Embeddings saved to `{chroma_path}` and ready for retrieval!")

