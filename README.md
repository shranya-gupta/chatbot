#  Multimodal AI Chatbot (Text + Image) using Gemini API

An AI-powered **multimodal chatbot system** built using **FastAPI** and **Gemini API**.

This application supports:

-  Text-based conversations
-  Image understanding
-  Multimodal reasoning (Image + Text together)

The system is modular, scalable, and production-ready with separated pipelines for clean architecture.

---

#  Features

- ✅ Text generation using Gemini
- ✅ Image analysis using Gemini
- ✅ Image + text combined reasoning
- ✅ Modular pipeline architecture
- ✅ Clean separation of concerns
- ✅ FastAPI backend

---

#  System Architecture

The project follows a **pipeline-based architecture**:

- `text_pipeline` → Handles text prompts
- `image_pipeline` → Handles image-only inputs
- `image_text_pipeline` → Handles multimodal inputs
- `image_utils` → Image preprocessing utilities

---

#  Project Structure

```
project-root/
│
├── pipelines/
│   ├── __init__.py
│   ├── text_pipeline.py
│   ├── image_pipeline.py
│   └── image_text_pipeline.py
│
├── utils/
│   ├── __init__.py
│   └── image_utils.py
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

#  Pipeline Responsibilities

## 🔹 text_pipeline.py
Handles:
- Text prompts
- Chat-style interactions
- Gemini text model calls

---

## 🔹 image_pipeline.py
Handles:
- Image-only analysis
- Image preprocessing
- Gemini model calls

---

## 🔹 image_text_pipeline.py
Handles:
- Image + accompanying text prompt
- Multimodal reasoning
- Advanced contextual responses

---

#  Tech Stack

- Python
- FastAPI
- Gemini API
- Uvicorn

---

#  Setup & Installation

## 1️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️. Set Gemini API Key

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Windows (PowerShell)

```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

---

## 3️. Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

#  What This System Handles

- ✔️ Pure text AI conversations
- ✔️ Image understanding
- ✔️ Multimodal reasoning
- ✔️ Structured JSON responses
- ✔️ Modular architecture for scaling
- ✔️ Error handling

---

# 💡 Future Enhancements

- 🔹 Conversation memory
- 🔹 Streaming responses
- 🔹 Authentication & rate limiting
- 🔹 Logging & monitoring
- 🔹 Docker support
- 🔹 Cloud deployment (AWS / GCP / Azure)
- 🔹 Frontend integration (React / Next.js)

---
