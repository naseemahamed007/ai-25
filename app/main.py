from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import TextInput, EmotionResult, JournalEntryIn, JournalEntryOut, MoodSnapshotIn, MoodSnapshotOut
from app.emotion import detect_emotion
from app.response_tone import craft_supportive_reply
from app.journaling import save_entry, summarize_entry
from app.mood import save_mood_snapshot, get_weekly_mood
from app.auth import get_current_user_optional

app = FastAPI(title="Emotional AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.post("/analyze", response_model=EmotionResult)
def analyze_text(payload: TextInput, user=Depends(get_current_user_optional)):
    emotion, scores = detect_emotion(payload.text)
    reply = craft_supportive_reply(emotion, payload.text)
    return {"emotion": emotion, "scores": scores, "reply": reply}

@app.post("/journal", response_model=JournalEntryOut)
def journal(payload: JournalEntryIn, user=Depends(get_current_user_optional)):
    entry = save_entry(user, payload.text)
    summary, insights = summarize_entry(payload.text)
    return {"id": entry.id, "summary": summary, "insights": insights, "createdAt": entry.created_at}

@app.post("/mood", response_model=MoodSnapshotOut)
def mood_snapshot(payload: MoodSnapshotIn, user=Depends(get_current_user_optional)):
    snap = save_mood_snapshot(user, payload.timeOfDay, payload.emotion)
    weekly = get_weekly_mood(user)
    return {"saved": True, "weekly": weekly}
