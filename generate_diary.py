import os
import requests
import datetime
import sys

def get_ai_tip(api_key):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    
    prompt = "Write a one‑sentence interesting fact or productivity tip for cat owners. Keep it fun, original, and under 20 words."
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, headers=headers, params=params, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    else:
        print(f"API error: {response.text}")
        return "AI was sleepy today – stay curious and keep cuddling!"

def main():
    api_key = os.environ.get("THEGARDENCAT")   # <-- your secret name
    if not api_key:
        print("Missing THEGARDENCAT secret")
        sys.exit(1)
    
    tip = get_ai_tip(api_key)
    today = datetime.date.today().isoformat()
    
    with open("DIARY.md", "a") as f:
        f.write(f"\n## {today}\n{tip}\n")
    
    print(f"✅ Added tip for {today}: {tip}")

if __name__ == "__main__":
    main()
