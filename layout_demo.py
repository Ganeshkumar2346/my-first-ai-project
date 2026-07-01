import streamlit as st

st.title("Layout Demo")

# Sidebar - appears on the left side
with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Choose model:", ["Llama", "Mixtral", "Gemma"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

st.write(f"Selected model: {model}")
st.write(f"Temperature: {temperature}")

# Columns - side by side layout
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the left side")

with col2:
    st.header("Column 2")
    st.write("This is the right side")