from typing import List, Tuple
import re

def save_entry(user, text: str):
    # Stub: replace with DB write
    class Entry: pass
    e = Entry()
    e.id = 1
    e.created_at = "2025-11-21T02:27:00Z"
    return e

def summarize_entry(text: str) -> Tuple[str, List[str]]:
    sentences = [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
    summary = sentences[0] if sentences else "A short reflective note."
    insights = []
    if "morning" in text.lower(): insights.append("Morning mood signal")
    if any(k in text.lower() for k in ["tired","sleep","rest"]): insights.append("Energy/rest pattern")
    if any(k in text.lower() for k in ["alone","lonely","isolated"]): insights.append("Connection need")
    return summary, insights or ["Not enough data—try adding what felt hard or helpful."]
