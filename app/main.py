from fastapi import FastAPI, UploadFile, File, Form
from app.pipelines.text_pipeline import text_pipeline
from app.pipelines.image_pipeline import image_pipeline
from app.pipelines.image_text_pipeline import image_text_pipeline
app = FastAPI(title="Multimodal Chatbot")
@app.post("/chat")
async def chat(
    prompt: str = Form(None),
    image: UploadFile = File(None)
):
    if prompt and image:
        image_bytes = await image.read()
        response = image_text_pipeline(prompt, image_bytes)
        return {"mode": "image+text", "response": response}

    elif image:
        image_bytes = await image.read()
        response = image_pipeline(image_bytes)
        return {"mode": "image_only", "response": response}

    elif prompt:
        response = text_pipeline(prompt)
        return {"mode": "text_only", "response": response}

    return {"error": "No input provided"}
