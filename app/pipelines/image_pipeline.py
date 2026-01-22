from google import genai
import os
from app.utils.image_utils import load_image
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def image_pipeline(image_bytes: bytes) -> str:
    image = load_image(image_bytes)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            "Describe the main visible objects in this image. If unsure, describe what you can see without guessing.",
            image
        ]
    )
    return response.text
