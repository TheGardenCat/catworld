import os
import requests
import sys

def main():
    api_key = os.environ.get("THEGARDENCAT")
    if not api_key:
        print("Error: THEGARDENCAT environment variable not set.", file=sys.stderr)
        sys.exit(1)

    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        models_data = response.json()

        print("Available models that support 'generateContent':")
        for model in models_data.get("models", []):
            if "generateContent" in model.get("supportedGenerationMethods", []):
                # The name is in the format "models/gemini-xxx", we want the part after "models/"
                model_name = model["name"].replace("models/", "")
                print(f"  - {model_name}")

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}", file=sys.stderr)
        if response is not None:
            print(f"Status Code: {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
