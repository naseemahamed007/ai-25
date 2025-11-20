from pydantic import BaseModel
from typing import Dict, List, Optional

class TextInput(BaseModel):
    text: str

class EmotionResult(BaseModel):
    emotion: str
    scores: Dict[str, float]
    reply: str

class JournalEntryIn(BaseModel):
    text: str

class JournalEntryOut(BaseModel):
    id: int
    summary: str
    insights: List[str]
    createdAt: str

class MoodSnapshotIn(BaseModel):
    timeOfDay: str  # "morning" | "afternoon" | "night"
    emotion: str

class MoodSnapshotOut(BaseModel):
    saved: bool
    weekly: Dict[str, Dict[str, float]]
