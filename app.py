import streamlit as st
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from chromadb import PersistentClient
import ollama

# Define collection name
collection_name = "book_chunks"

# Streamlit page configuration
st.set_page_config(page_title="RAG Book Chatbot", layout="wide")

# Set paths and models
chroma_path = "chroma_db"
embed_model = "all-MiniLM-L6-V2"
llm_model = "mistral"
top_k = 3

# Setup function to retrieve or create collection
@st.cache_resource
def get_collection():
    embed_fn = SentenceTransformerEmbeddingFunction(model_name=embed_model)
    client = PersistentClient(path=chroma_path)

    # Check if collection exists, create it if not
    existing_collections = [col.name for col in client.list_collections()]
    if collection_name not in existing_collections:
        st.warning(f"Collection '{collection_name}' does not exist. Creating it now...")
        client.create_collection(name=collection_name, embedding_function=embed_fn)

    return client.get_collection(name=collection_name, embedding_function=embed_fn)

# Retrieve collection
collection = get_collection()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI setup for Streamlit
st.title("RAG Chatbot for Books")
st.markdown("""
Ask questions across the following books:

- *Atomic Habits*
- *The 7 Habits of Highly Effective People*
- *Rich Dad Poor Dad*
""")

# User input for query
user_query = st.text_input("Ask your Question:")

if user_query:
    # Query the ChromaDB collection
    result = collection.query(query_texts=[user_query], n_results=top_k)
    chunks = result['documents'][0]
    context = "\n\n".join(chunks)
    source_info = result["metadatas"][0]

    # Prepare the prompt for the LLM model
    prompt = f"""You must answer the question using the context provided below.

    Context:
    {context}

    Question:
    {user_query}

    Answer:"""

    # Create messages for the chatbot
    messages = [{"role": "system", "content": "You are a helpful assistant that uses the provided book context."}]

    # Include chat history for follow-up questions
    for q, a in st.session_state.chat_history:
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    messages.append({"role": "user", "content": prompt})

    # Get response from Ollama (Mistral model)
    with st.spinner("Thinking...."):
        response = ollama.chat(
            model=llm_model,
            messages=messages
        )
        answer = response["message"]["content"]

        # Store the query and answer in chat history
        st.session_state.chat_history.append((user_query, answer))

        # Display the generated answer
        st.success("Answer Generated!")
        st.write(answer)

        # Show sources used for the answer
        with st.expander("Sources Used"):
            for meta in source_info:
                st.markdown(f"- **{meta['book']}**, *{meta['chapter']}*")

# Display chat history
if st.session_state.chat_history:
    st.divider()
    st.subheader("Chat History")
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown("---")
