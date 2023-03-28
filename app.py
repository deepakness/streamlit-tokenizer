import streamlit as st
import tiktoken

st.set_page_config(page_title='Token Counter', page_icon='📚', layout='wide')

enc = tiktoken.get_encoding("cl100k_base")

st.title("Token Counter")

text_input = st.text_area("Type or paste your text here...", height=200)

if st.button("Calculate"):
    tokens = len(enc.encode(text_input))
    st.success(f"Number of tokens: {tokens}")
