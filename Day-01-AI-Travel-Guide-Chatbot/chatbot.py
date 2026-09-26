import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")

SYSTEM_PROMPT = (
    "You are a friendly travel guide. Help the user plan trips by suggesting "
    "places to visit, activities, local food, and practical tips. "
    "Keep answers short, warm, and conversational."
)

GREETING = "Hi! I'm your travel guide. Where would you like to go?"


def chat():
    # The full history is sent each time, so the bot remembers the conversation
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": GREETING},
    ]
    print(f"Guide: {GREETING}")
    print("(type 'quit' to exit)\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGuide: Safe travels!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "bye"):
            print("Guide: Safe travels!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
        )
        answer = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": answer})
        print(f"\nGuide: {answer}\n")


if __name__ == "__main__":
    chat()