# ===== STREAMLIT CHEATSHEET =====

# Text display
st.title("text")
st.write("text")

# Get input
name = st.text_input("label")
number = st.slider("label", 1, 10)

# Button
if st.button("label"):
    st.write("action")

# File upload
file = st.file_uploader("label")

# Sidebar
with st.sidebar:
    st.write("text")

# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("left")

# Memory
if "key" not in st.session_state:
    st.session_state.key = []