import os
import datetime
import random
from groq import Groq

def main():
    api_key = os.environ.get("THEGARDENCAT")
    if not api_key:
        print("Missing THEGARDENCAT secret")
        return

    client = Groq(api_key=api_key)

    # All prompts are now purely about cats
    prompts = [
        "Write a one‑sentence fun fact about cats.",
        "Share an interesting observation about cat behavior.",
        "Give a short tip for making a cat happier.",
        "Tell me something surprising about cats that most people don't know.",
        "Write a cute one‑sentence story about a cat's daily adventure.",
        "What's a unique habit of cats that makes them special?",
        "Describe a cat's purr in a creative, one‑sentence way."
    ]
    prompt = random.choice(prompts)

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.8,
            max_tokens=40,
        )
        tip = chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Groq API error: {e}")
        tip = "AI cat was sleepy today – stay curious and keep cuddling!"

    today = datetime.date.today().isoformat()
    with open("DIARY.md", "a") as f:
        f.write(f"\n## {today}\n{tip}\n")

    print(f"Added tip for {today}: {tip}")

if __name__ == "__main__":
    main()
