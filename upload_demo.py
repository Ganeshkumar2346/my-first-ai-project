import streamlit as st

st.title("File Upload Demo")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    st.write("File size:", uploaded_file.size, "bytes")