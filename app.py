import math

import streamlit as st
import tiktoken

st.set_page_config(page_title="Token Counter", page_icon="📚", layout="wide")

MODEL_TO_ENCODING = {
    "GPT-4o / GPT-4.1 / GPT-3.5 (cl100k_base)": "cl100k_base",
    "GPT-4o-mini (o200k_base)": "o200k_base",
    "Codex / code models (p50k_base)": "p50k_base",
    "Legacy GPT-3 (r50k_base)": "r50k_base",
}


@st.cache_resource(show_spinner=False)
def get_encoder(encoding_name: str) -> tiktoken.Encoding:
    """Load and cache a tokenizer encoder by name."""
    return tiktoken.get_encoding(encoding_name)


def count_tokens(text: str, encoding_name: str) -> int:
    """Return token count for text using the selected tokenizer encoding."""
    encoder = get_encoder(encoding_name)
    return len(encoder.encode(text))


def estimate_tokens_fallback(text: str) -> int:
    """Best-effort token estimate for offline/restricted environments."""
    normalized = text.strip()
    if not normalized:
        return 0
    return max(1, math.ceil(len(normalized) / 4))


st.title("📚 Token Counter")
st.caption("Quickly estimate token usage for OpenAI-compatible encodings.")

col1, col2 = st.columns([2, 1])
with col1:
    text_input = st.text_area(
        "Type or paste your text",
        height=260,
        placeholder="Paste prompt, document, or code here…",
    )
with col2:
    selected_label = st.selectbox("Tokenizer", options=list(MODEL_TO_ENCODING.keys()))
    encoding_name = MODEL_TO_ENCODING[selected_label]

    st.markdown("### Quick stats")
    st.metric("Characters", len(text_input))
    st.metric("Words", len(text_input.split()) if text_input.strip() else 0)

calculate = st.button("Calculate tokens", type="primary")

if calculate:
    if not text_input.strip():
        st.warning("Please enter text before calculating tokens.")
    else:
        try:
            token_count = count_tokens(text_input, encoding_name)
            st.success(f"Number of tokens: {token_count}")
            st.info(f"Using encoding: `{encoding_name}`")
        except Exception as exc:
            estimated = estimate_tokens_fallback(text_input)
            st.warning(
                "Tokenizer data could not be loaded in this environment. "
                "Showing an approximate count instead."
            )
            st.success(f"Estimated tokens: ~{estimated}")
            st.caption("Approximation uses ~4 characters per token and may differ from model-accurate counts.")
            with st.expander("Show technical details"):
                st.code(str(exc), language="text")

st.markdown("---")
st.markdown(
    "**Tip:** Different models use different tokenizers. "
    "If you're budgeting costs, choose the encoding that best matches your target model."
)
