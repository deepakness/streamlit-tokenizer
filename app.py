import streamlit as st
import tiktoken

st.set_page_config(page_title='Token Counter', page_icon='📚', layout='wide')

enc = tiktoken.get_encoding("cl100k_base")

st.title("Token Counter")
st.markdown("---")

st.write("This tool counts the number of tokens in a given text. To use it, type or paste your text in the text box below and click the 'Calculate' button.")

text_input = st.text_area("Type or paste your text here...", height=200)
centered_button = st.button("Calculate", key="calculate")

if centered_button:
    tokens = len(enc.encode(text_input))
    st.success(f"Number of tokens: {tokens}")
