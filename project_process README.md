# RAG Chatbot for Books - Project Process

## Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that answers user queries by retrieving relevant chunks of text from three popular self-help books: *Atomic Habits*, *7 Habits of Highly Effective People*, and *Rich Dad Poor Dad*. It uses **ChromaDB** for embedding and retrieval, and **Ollama** (Mistral) for generation.

The main goal of this project is to showcase how RAG architecture can improve the accuracy and relevance of AI-generated responses in comparison to traditional LLM-based systems.

---

## Why Use RAG Instead of Traditional Models?

### Traditional Models:
Traditional models like **GPT-3** or **GPT-4** generate responses based on their **pre-trained knowledge**. They rely solely on the vast data used to train them, which can lead to:
- **Inaccurate or outdated information** if the model hasn't been updated
- **Hallucination of facts** where the model provides answers that sound plausible but are not grounded in real data
- **Limited specificity** when the model lacks specialized data on niche topics

### RAG Models:
**RAG (Retrieval-Augmented Generation)** improves traditional models by:
1. **Retrieving relevant information** in real-time from a database like ChromaDB.
2. **Generating answers** based on the most relevant content retrieved, rather than relying solely on pre-trained knowledge.

This means RAG models can:
- Provide **highly relevant, up-to-date, and accurate responses** based on the latest content.
- Ensure **contextual grounding**, making the answers more **factual** and **less likely to hallucinate**.
- Use **custom datasets** that are updated as new data (books, papers, etc.) is added.

---

## Development Process:

### Step 1: **Data Collection & Preprocessing**
The first step involved scraping and summarizing data from three books:
- *Atomic Habits* by James Clear
- *The 7 Habits of Highly Effective People* by Stephen Covey
- *Rich Dad Poor Dad* by Robert Kiyosaki

The **text was chunked into manageable parts**, each containing relevant content for easy retrieval.

### Step 2: **Embedding with Sentence-Transformers**
I used the **`all-MiniLM-L6-v2` model** from **HuggingFace** to embed the text chunks. This model is efficient for generating vector representations of text, allowing for **semantic search** later.

### Step 3: **Setting Up ChromaDB**
The embedded vectors were stored in **ChromaDB**, an efficient local vector database. I used Chroma for its:
- **Scalability** in terms of storage and retrieval
- **Speed** for semantic search tasks
- **Support for metadata filtering** (retrieving context based on books, chapters)

### Step 4: **Model Integration (Ollama / Mistral)**
I used **Ollama** (powered by the **Mistral** model) for natural language generation. Ollama provides:
- Fast inferences with local models
- Flexible integration with various sources (like ChromaDB) for context-based responses

### Step 5: **Building the Streamlit App**
I developed a **Streamlit-based frontend** to allow users to interact with the chatbot. Users can:
- Ask questions about the three books
- See the answers along with **the sources** used for the response
- Engage in **multi-turn conversation** where the chatbot remembers prior queries

---

## AWS Deployment

The app is **hosted on AWS EC2** (t3.large), where I deployed:
- **Streamlit** for the frontend
- The backend (ChromaDB and Ollama) is running on the same EC2 instance


---

## Conclusion
By using **RAG architecture**, this project demonstrates how combining **semantic search** with **LLM generation** provides accurate, grounded, and efficient responses. It's a great example of how modern AI systems can work with **retrieval** to enhance the **quality** of answers, especially in knowledge-intensive domains.

---

