# RAG Book Chatbot – Portfolio Overview

## Overview
The RAG (Retrieval-Augmented Generation) Book Chatbot is an interactive QA system that answers user queries based on the content of well-known self-help books:
- *Atomic Habits*
- *The 7 Habits of Highly Effective People*
- *Rich Dad Poor Dad*

The chatbot retrieves relevant information from book embeddings stored in ChromaDB and uses the Mistral model (via Ollama) to generate context-aware responses. It is deployed on AWS EC2 with a Streamlit interface and optional Docker support.

## Technologies Used
- **Streamlit**: Interactive UI
- **ChromaDB**: Vector database for text chunk retrieval
- **Ollama**: For running the Mistral language model
- **AWS EC2**: Cloud hosting
- **Docker**: Optional containerization
- **Python**, `sentence-transformers`, `chromadb`, `torch`, etc.

## Deployment Steps
1. Launch an Ubuntu EC2 instance and configure ports (SSH, Streamlit).
2. Clone the GitHub repo and install dependencies.
3. Populate ChromaDB using `embed_books.py`.
4. Run `streamlit run app.py` to launch the app.
5. (Optional) Use Docker to containerize and deploy.

## Folder Structure
```
rag-book-chatbot/
├── app.py
├── embed_books.py
├── chroma_db/
├── data/
├── book_data_cleaning.py
├── Dockerfile
└── requirements.txt
```

## Conclusion
This project showcases a real-world RAG system integrating document retrieval, embeddings, and generative LLM response generation—deployed via cloud infrastructure and made accessible through an intuitive Streamlit interface.
