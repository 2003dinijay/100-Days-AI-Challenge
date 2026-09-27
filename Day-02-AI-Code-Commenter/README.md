# AI Code Commenter

Reads a Python file, finds every function and method, and asks an LLM to write a one-line comment explaining each one. The result is saved as a new `*_commented.py` file; the original is left untouched.

## Example

Input ([examples/sample.py](examples/sample.py)):

```python
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

Output ([examples/sample_commented.py](examples/sample_commented.py)):

```python
# Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

## Features

- Uses Python's `ast` module to find functions, async functions, and class methods
- Places each comment above any decorators, matching the function's indentation
- Low temperature (0.2) for consistent, factual comments
- Works with OpenAI or Google Gemini (free tier) through the OpenAI-compatible API

## Setup

From the repo root (see the [main README](../README.md) for first-time setup):

```bash
source venv/bin/activate
source .env
pip install -r Day-02-AI-Code-Commenter/requirements.txt
```

## Usage

Comment a file:

```bash
python3 Day-02-AI-Code-Commenter/commenter.py Day-02-AI-Code-Commenter/examples/sample.py
```

Run with no arguments to comment a built-in demo snippet:

```bash
python3 Day-02-AI-Code-Commenter/commenter.py
```

## Tech

Python, `ast`, OpenAI Python SDK, Google Gemini
