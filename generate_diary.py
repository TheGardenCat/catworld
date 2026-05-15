import os
import datetime
import google.generativeai as genai

def main():
    # Read the secret directly (matches your GitHub secret name)
    api_key = os.environ.get("THEGARDENCAT")
    if not api_key:
        print("Missing THEGARDENCAT secret")
        return

    genai.configure(api_key=api_key)

    # Try multiple model names (Google changes them often)
    model_names = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp"]
    tip = None

    for model_name in model_names:
        try:
            print(f"Trying model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(
                "Write a one‑sentence interesting fact or productivity tip for cat owners. Keep it fun, original, and under 20 words."
            )
            tip = response.text.strip()
            print(f"Success with {model_name}")
            break
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue

    if not tip:
        tip = "AI cat was sleepy today – stay curious and keep cuddling!"

    today = datetime.date.today().isoformat()
    with open("DIARY.md", "a") as f:
        f.write(f"\n## {today}\n{tip}\n")

    print(f"Added tip for {today}: {tip}")

if __name__ == "__main__":
    main()
