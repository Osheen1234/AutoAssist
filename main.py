import os
import google.generativeai as genai

def setup_autoassist():
    """Initializes the AutoAssist automotive troubleshooting agent."""
    # Ensure you have your GEMINI_API_KEY set in your environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please set it before running the agent.")
        return None
    
    genai.configure(api_key=api_key)
    # Using the standard model for quick, technical responses
    return genai.GenerativeModel('gemini-2.5-flash')

def get_diagnostic(model, issue_description):
    """Fetches diagnostic steps from the AI agent."""
    prompt = f"""
    You are AutoAssist, a highly experienced automotive mechanic and technical troubleshooting expert. 
    A user is experiencing the following vehicle issue: "{issue_description}"
    
    Please provide:
    1. Potential common causes.
    2. Step-by-step technical troubleshooting advice.
    3. Any safety warnings relevant to the repair.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while consulting AutoAssist: {e}"

if __name__ == "__main__":
    print("Welcome to AutoAssist - Your Virtual Mechanic")
    print("-" * 45)
    
    agent = setup_autoassist()
    
    if agent:
        issue = input("Describe the vehicle problem (e.g., 'rough idle when cold'): ")
        if issue.strip():
            print("\nConsulting AutoAssist...\n")
            diagnostic_report = get_diagnostic(agent, issue)
            print(diagnostic_report)
        else:
            print("No issue described. Shutting down AutoAssist.")
          
