
from app.pipelines.image_pipeline import image_pipeline
from app.pipelines.text_pipeline import text_pipeline

def image_text_pipeline(prompt: str, image_bytes: bytes) -> str:
    """
    Combines image understanding with user question.
    Guarantees image description presence.
    """

    image_description = image_pipeline(image_bytes)
    if not image_description or len(image_description) < 20:
        image_description = (
            "The image content could not be clearly identified. "
            "Answer cautiously using limited visual information."
        )

    final_prompt = f"""
You are given an image description and a user question.

IMAGE DESCRIPTION:
{image_description}

USER QUESTION:
{prompt}

Answer strictly based on the image description.
Do NOT add information not visible in the image.
"""

    return text_pipeline(final_prompt)
