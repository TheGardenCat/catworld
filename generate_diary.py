import os
import datetime
from groq import Groq

def main():
    # Read your GitHub secret (still named THEGARDENCAT)
    api_key = os.environ.get("THEGARDENCAT")
    if not api_key:
        print("Missing THEGARDENCAT secret")
        return

    client = Groq(api_key=api_key)

    prompt = "Write a one‑sentence interesting fact or productivity tip for cat owners. Keep it fun, original, and under 20 words."

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",   # Fast, free, and good
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
