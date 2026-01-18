from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

# ✅ ABSOLUTE IMPORTS ONLY — NO DOTS
from model import get_emotion_scores, emotion_columns
from replies import generate_reply
from sortinghat import sorting_hat

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str


@app.post("/chat")
def chat(data: ChatInput):
    scores = get_emotion_scores(data.message)
    reply = generate_reply(scores, np.array(emotion_columns))
    return reply   # ⚠️ plain text only


@app.post("/sortinghat")
async def sortinghat_api(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    results = sorting_hat(text)

    output = ""
    for name, character in results.items():
        output += f"{name} → {character}\n"

    return output