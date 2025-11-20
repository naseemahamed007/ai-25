from transformers import pipeline

# Warm-up: multi-emotion model
_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

LABEL_MAP = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "stress",
    "surprise": "excited",
    "disgust": "angry",
    "neutral": "neutral"
}

def detect_emotion(text: str):
    scores = _classifier(text)[0]
    ranked = sorted(scores, key=lambda x: x["score"], reverse=True)
    top = ranked[0]["label"]
    normalized = {LABEL_MAP.get(s["label"], s["label"]): float(round(s["score"], 4)) for s in ranked}
    emotion = LABEL_MAP.get(top, top)
    return emotion, normalized
