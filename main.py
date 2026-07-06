import requests
import os

# Get API key from environment variable
API_KEY = os.environ.get("GEMINI_API_KEY")


def get_diagnostic(issue_description):
    # Endpoint for Gemini 2.0 Flash
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                          "text": f"You are a professional mechanic. Vehicle issue: {issue_description}. Provide potential causes, troubleshooting steps, and safety warnings."}]
        }]
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        # Check if 'candidates' exists and contains content before accessing it
        if 'candidates' in data and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            if 'content' in candidate and 'parts' in candidate['content']:
                return candidate['content']['parts'][0]['text']
            else:
                return f"Error: Candidate found but no content. Full response: {data}"
        else:
            # This captures safety blocks or empty API responses
            return f"Error: No candidates returned. This often means the request was blocked by safety filters. Full response: {data}"

    except Exception as e:
        return f"An exception occurred: {e}"


if __name__ == "__main__":
    print("Welcome to AutoAssist (REST API Version)")
    issue = input("Describe the vehicle problem: ")
    if issue.strip():
        print("\nConsulting AutoAssist...\n")
        print(get_diagnostic(issue))
        
