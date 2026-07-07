import streamlit as st
import tempfile
import os as os_module  # only needed if you don't already have `os` imported
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Chat with your PDF")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    # TYPE THIS PART — the new concept: handle empty/unreadable PDFs
    if not documents or all(doc.page_content.strip() == "" for doc in documents):
        st.error("Couldn't extract any text from this PDF. It may be a scanned image without selectable text.")
    else:
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(chunks, embedding_model)

        st.success(f"Processed into {len(chunks)} chunks. Ready to answer questions!")

        query = st.text_input("Ask a question about your PDF:")

        if query:
            with st.spinner("Thinking..."):
                results = vector_store.similarity_search(query, k=3)
                context = "\n".join([doc.page_content for doc in results])

                prompt = f"""Answer the question using ONLY the context below. If the answer isn't in the context, say so clearly instead of guessing.

Context:
{context}

Question: {query}
"""
                response = llm.invoke(prompt)
                st.write("**Answer:**", response.content)

    # Clean up the temporary file now that we're done with it
    os.remove(tmp_path)