# 100 Days AI Challenge

One small AI project a day for 100 days. Each project lives in its own folder with its own README and requirements.

## Projects

| Day | Project | Description |
| --- | ------- | ----------- |
| 01 | [AI Travel Guide Chatbot](Day-01-AI-Travel-Guide-Chatbot/) | Role-play travel-guide chatbot with conversation memory |

## Setup

All projects share one virtual environment and one `.env` file at the repo root.

```bash
git clone https://github.com/2003dinijay/100-Days-AI-Challenge.git
cd 100-Days-AI-Challenge
python3 -m venv venv
source venv/bin/activate
cp .env.example .env   # then add your API key
source .env
```

Then install a project's dependencies and run it, for example:

```bash
pip install -r Day-01-AI-Travel-Guide-Chatbot/requirements.txt
python3 Day-01-AI-Travel-Guide-Chatbot/chatbot.py
```

## Structure

```
100-Days-AI-Challenge/
├── README.md
├── .env.example          # template for API keys (copy to .env)
├── .gitignore
└── Day-01-AI-Travel-Guide-Chatbot/
    ├── README.md
    ├── chatbot.py
    └── requirements.txt
```
