from typing import Dict

TONE_GUIDE: Dict[str, Dict[str, str]] = {
    "sad": {
        "voice": "gentle",
        "reply": "I hear that you're feeling low. It’s okay not to know the exact reason. Would a small step help—like a short walk, writing how the morning went, or messaging someone you trust? If you want, tell me one thing that felt heavy today."
    },
    "angry": {
        "voice": "calm",
        "reply": "Sounds frustrating. Your feelings are valid. Try a quick reset: 4 slow breaths, step away for 5 minutes, and note what triggered it. Want me to help label the trigger?"
    },
    "stress": {
        "voice": "grounded",
        "reply": "Stress can sneak up. Let’s make it lighter: list 3 tasks, pick one tiny action, and set a 20‑minute focus timer. I can help you break it down."
    },
    "happy": {
        "voice": "warm",
        "reply": "Love that energy. Want to capture this win? I can save a note or set a small goal to keep the momentum."
    },
    "excited": {
        "voice": "supportive",
        "reply": "You sound pumped! Want a quick plan to channel it—one action now, one later, one to share?"
    },
    "lonely": {
        "voice": "engaging",
        "reply": "Feeling alone is tough. You’re not invisible here. We can try a connection step: send a check‑in to a friend, join a small online group, or start a 5‑minute gratitude note together."
    },
    "confused": {
        "voice": "clarifying",
        "reply": "Let’s find clarity. Tell me the options you’re considering. I’ll help you compare them and choose one next step."
    },
    "neutral": {
        "voice": "balanced",
        "reply": "You seem steady. Want a tiny habit to keep the day smooth—like a 2‑minute reset or a quick note?"
    },
}

def craft_supportive_reply(emotion: str, text: str) -> str:
    base = TONE_GUIDE.get(emotion)
    if not base:
        return "Emotions can be layered. I’m here to listen and help you take one small, helpful step."
    return base["reply"]
