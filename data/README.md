# Data Folder

This folder contains the processed and cleaned data for the RAG Chatbot project. The data includes text chunks, summaries, and metadata from the following books:

- **Atomic Habits** by James Clear
- **The 7 Habits of Highly Effective People** by Stephen Covey
- **Rich Dad Poor Dad** by Robert Kiyosaki

The data is used for building the **Retrieval-Augmented Generation (RAG)** chatbot. It is stored in JSON format and is ready for embedding and vector storage.

## Data Files

### `merged_book_chunks.json`
This is the combined file containing:
- **Text chunks** from the books.
- **Summaries** of each chunk.
- **Metadata** like `book`, `chapter`, `chunk_id` to allow for easy filtering and retrieval.

### How the Data Was Processed:
- The books were divided into **chunks of text** (typically per chapter or concept).
- A **summary** was generated for each chunk using the `mistral` model from **Ollama**.
- The data was **embedded** using the `all-MiniLM-L6-v2` sentence transformer to create vector representations for semantic search.

## How to Regenerate the Data
If you need to regenerate the data (or work with different books), follow these steps:

1. **Chunking**: Use the script in `embed_chunks.py` to split the books into text chunks.
2. **Summarization**: Use `mistral` via Ollama to summarize each chunk.
3. **Embeddings**: Embed the text chunks and summaries using **Sentence-Transformers** (`all-MiniLM-L6-v2`).

## Using the Data
The data can be loaded and queried directly using **ChromaDB** for retrieval tasks in the chatbot. Simply call the `get_collection` function to load the data from the local ChromaDB instance.


