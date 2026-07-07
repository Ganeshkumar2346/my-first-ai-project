# my-first-ai-project

A collection of AI/LLM projects built while learning to become an AI Engineer — starting from basic LLM API calls through a complete RAG (Retrieval-Augmented Generation) application.

## Project 1: Chat with your PDF

A RAG-based application that lets you upload a PDF and ask questions about its content in plain English.

### How it works

1. Upload a PDF through the browser
2. The app loads and splits the document into small chunks
3. Each chunk is converted into an embedding (a numerical representation of its meaning)
4. Chunks are stored in a FAISS vector database
5. When you ask a question, the app retrieves the most relevant chunks and passes them to an LLM (Llama 3.3 70B via Groq) to generate an accurate answer
6. If the answer isn't in the document, the app says so instead of guessing

### Tech Stack

- **LangChain** — orchestration framework
- **Groq (Llama 3.3 70B)** — LLM for generating answers
- **HuggingFace Embeddings** (`sentence-transformers/all-MiniLM-L6-v2`) — converts text to vectors
- **FAISS** — vector database for similarity search
- **Streamlit** — web UI
- **PyPDF** — PDF text extraction

### Running Locally

1. Clone this repo
2. Install dependencies: