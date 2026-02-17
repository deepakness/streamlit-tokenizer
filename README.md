# Streamlit Token Counter

A lightweight Streamlit app for estimating token counts using OpenAI-compatible `tiktoken` encodings.

## Features

- Count tokens for pasted text in one click.
- Choose from common tokenizer encodings:
  - `cl100k_base`
  - `o200k_base`
  - `p50k_base`
  - `r50k_base`
- Quick text stats (character and word counts).
- Friendly empty-input validation.
- Graceful error handling with optional technical details.
- Offline/restricted fallback estimate (`~4 chars/token`) when encoder data cannot be loaded.

## Tech Stack

- [Streamlit](https://streamlit.io/) for the UI.
- [tiktoken](https://github.com/openai/tiktoken) for tokenization.

## Getting Started

### 1) Clone and enter the project

```bash
git clone <your-repo-url>
cd streamlit-tokenizer
```

### 2) Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit (typically `http://localhost:8501`).

## Usage

1. Paste text into the text area.
2. Select the tokenizer that matches your target model.
3. Click **Calculate tokens**.
4. Review token count and quick text stats.

## Troubleshooting

If token counting fails and you see a warning:

- Ensure outbound HTTPS access is allowed.
- Verify required proxy settings are configured in your environment.
- Expand **Show technical details** in the app for the exact underlying error.
- The app will provide an approximate count (`~4 chars/token`) so the workflow still remains usable.

## Notes

- Token counts can vary across model families due to tokenizer differences.
- Fallback estimates are intentionally rough and should not be used for precise billing decisions.

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```
