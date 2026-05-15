import os
import datetime
import google.generativeai as genai

def main():
    # The library reads GEMINI_API_KEY by default
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY secret")
        return

    genai.configure(api_key=api_key)

    # Use the latest stable model name as a string – the library will map it
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = "Write a one‑sentence interesting fact or productivity tip for cat owners. Keep it fun, original, and under 20 words."

    try:
        response = model.generate_content(prompt)
        tip = response.text.strip()
    except Exception as e:
        print(f"API error: {e}")
        tip = "AI cat was sleepy today – stay curious and keep cuddling!"

    today = datetime.date.today().isoformat()
    with open("DIARY.md", "a") as f:
        f.write(f"\n## {today}\n{tip}\n")

    print(f"Added tip for {today}: {tip}")

if __name__ == "__main__":
    main()
