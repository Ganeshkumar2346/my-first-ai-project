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


## Project 2: Research Assistant Agent

A multi-tool, memory-enabled agent built with LangGraph that decides which tool to use — calculator or word lookup — and can chain multiple tool calls together to answer complex questions.

### How it works

1. User asks a question through the Streamlit UI
2. The agent (LLM + LangGraph) analyzes the question and decides whether a tool is needed
3. If needed, it calls the relevant tool (calculator or word definition lookup) and loops back to reassess
4. This repeats until the agent has enough information to give a final answer
5. The full reasoning trace (each step) is visible in an expandable section

### Tech Stack

- **LangGraph** — state machine / graph framework for building the agent
- **LangChain Tools** — `@tool` decorator for defining callable functions the LLM can use
- **Groq (Llama 3.3 70B)** — LLM powering the agent's decisions
- **Streamlit** — web UI

### Running Locally

1. Install dependencies: