import streamlit as st
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from chromadb import PersistentClient
import ollama

st.set_page_config(page_title="RAG Book Chatbot", layout = "wide")

chroma_path = "chroma_db"
collection = "book_chunks"
embed_model = "all-MiniLM-L6-V2"
llm_model = "mistral"
top_k = 3


#Setup
@st.cache_resource
def get_collection():
    embed_fn = SentenceTransformerEmbeddingFunction(model_name=embed_model)
    client = PersistentClient(path = chroma_path)

    # Check if the collection exists
    existing_collections = [col.name for col in client.list_collections()]
    if collection not in existing_collections:
        st.warning(f"Collection '{collection}' does not exist. Creating it now...")
        client.create_collection(name=collection, embedding_function=embed_fn)

    return client.get_collection(name=collection, embedding_function=embed_fn)


collection = get_collection()


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#UI
st.title("RAG Chatbot for books")
st.markdown("""
Ask questions across the following books:

- *Atomic Habits*
- *The 7 Habits of Highly Effective People*
- *Rich Dad Poor Dad*
""")

user_query = st.text_input("Ask your Question:")

if user_query:
    result = collection.query(query_texts=[user_query],n_results=top_k)
    chunks = result['documents'][0]
    context = "\n\n".join(chunks)
    source_info = result["metadatas"][0]

    prompt = f"""You must answer the question using the context provided below."

    Context:
    {context}

    Question:
    {user_query}

    Answer:"""

    messages = [{"role": "system", "content": "You are a helpful assistant that  uses the provided book context."}]

    for q, a in st.session_state.chat_history:
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    messages.append({"role": "user", "content":prompt})
                        
    with st.spinner("Thinking...."):
        response = ollama.chat(
            model=llm_model,
            messages = messages
        )
        answer = response["message"]["content"]

        st.session_state.chat_history.append((user_query, answer))        

        st.success("Answer Generated!")
        st.write(answer)


        with st.expander("Souces Used"):
            for meta in source_info:
                st.markdown(f"- **{meta['book']}**, *{meta['chapter']}*")


if st.session_state.chat_history:
    st.divider()
    st.subheader("Chat History")
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown("---")
