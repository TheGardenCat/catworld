import os
import requests
import datetime
import sys

def get_ai_tip(api_key):
    # --- UPDATE THIS LINE with a model name from the find_model.py script ---
    # Try uncommenting one of these likely candidates:
    # MODEL_NAME = "gemini-2.0-flash-lite"
    MODEL_NAME = "gemini-1.5-flash"
    # MODEL_NAME = "gemini-2.5-flash-preview-09-2025"
    # --- --- ---

    # UPDATED: Using the stable v1beta endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    payload = {
        "contents": [{
            "parts": [{"text": "Write a one-sentence interesting fact or productivity tip for cat owners. Keep it fun, original, and under 20 words."}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}", file=sys.stderr)
        if response is not None:
            print(f"Status Code: {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
        return "AI cat was sleepy today – stay curious and keep cuddling!"

def main():
    api_key = os.environ.get("THEGARDENCAT")
    if not api_key:
        print("Missing THEGARDENCAT secret")
        sys.exit(1)

    tip = get_ai_tip(api_key)
    today = datetime.date.today().isoformat()

    with open("DIARY.md", "a") as f:
        f.write(f"\n## {today}\n{tip}\n")

    print(f"Added tip for {today}: {tip}")

if __name__ == "__main__":
    main()
