# RAG Chatbot for Books

## Overview
This project implements a **Retrieval-Augmented Generation (RAG)** chatbot, leveraging knowledge from three popular books:
- **Atomic Habits** by James Clear
- **The 7 Habits of Highly Effective People** by Stephen Covey
- **Rich Dad Poor Dad** by Robert Kiyosaki

The chatbot answers user queries by retrieving relevant context from these books and generating human-like responses using the **Mistral model** via Ollama.

### Key Features:
- **Book Knowledge**: Supports three books to answer a wide range of queries.
- **RAG Architecture**: Combines **retrieval-based search** (using ChromaDB) and **generation** (using Mistral).
- **Stateful Chat**: Maintain conversational history for better user experience.

## Tech Stack:
- **Streamlit**: For the chatbot interface.
- **ChromaDB**: For vector search and retrieval of relevant text chunks.
- **Ollama (Mistral)**: For generating context-based responses.
- **Sentence-Transformers**: For embedding text chunks and generating vectors.
