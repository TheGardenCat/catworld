import os
import requests
import datetime
import sys

def get_ai_tip(api_key):
    # FIXED: using a valid model name (gemini-2.0-flash-exp)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": "Write a one-sentence interesting fact or productivity tip for cat owners. Keep it fun, cute, original, and under 20 words."}]
        }]
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    else:
        print(f"API error {response.status_code}: {response.text}")
        return "AI was sleepy today – stay cat curious and keep cuddling!"

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
