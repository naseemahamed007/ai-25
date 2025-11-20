from collections import defaultdict
from typing import Dict

# In-memory aggregation (replace with DB)
_week = defaultdict(lambda: {"morning": {}, "afternoon": {}, "night": {}})

def save_mood_snapshot(user, timeOfDay: str, emotion: str):
    ukey = "anon" if not user else user.id
    day = "Fri"
    bucket = _week[ukey]
    bucket[timeOfDay][emotion] = bucket[timeOfDay].get(emotion, 0) + 1
    return True

def get_weekly_mood(user) -> Dict[str, Dict[str, float]]:
    ukey = "anon" if not user else user.id
    return _week[ukey]
