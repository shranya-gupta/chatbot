import os
import google.genai as genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def text_pipeline(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text


