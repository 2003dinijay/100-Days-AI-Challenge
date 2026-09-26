# AI Travel Guide Chatbot

An interactive, role-play travel-guide chatbot that remembers the conversation, so you can ask follow-up questions naturally.

## Example

```
Guide: Hi! I'm your travel guide. Where would you like to go?
You: Colombo
Guide: Great choice! Colombo mixes colonial history, markets, and seaside views...
You: what food should I try there?
Guide: Don't miss kottu roti, hoppers, and fresh seafood at Galle Face...
```

## Features

- Role-play persona set with a system prompt
- Conversation memory: the full chat history is sent with each request
- Works with OpenAI or Google Gemini (free tier) through the OpenAI-compatible API

## Setup

From the repo root (see the [main README](../README.md) for first-time setup):

```bash
source venv/bin/activate
source .env
pip install -r Day-01-AI-Travel-Guide-Chatbot/requirements.txt
```

## Usage

```bash
python3 Day-01-AI-Travel-Guide-Chatbot/chatbot.py
```

Type `quit` to exit.

## Tech

Python, OpenAI Python SDK, Google Gemini
