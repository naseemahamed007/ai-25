# Placeholder for voice emotion: integrate WebRTC + prosody analysis
# Approach: client records PCM → server extracts pitch/energy/speaking rate → classify (stress/excited/calm)
def analyze_voice_features(features):
    # features: {"pitch": float, "energy": float, "rate": float}
    if features["energy"] > 0.7 and features["rate"] > 0.6: return "excited"
    if features["pitch"] < 0.3 and features["energy"] < 0.3: return "sad"
    return "neutral"
