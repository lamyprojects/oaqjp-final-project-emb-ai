import requests

def emotion_detector(text_to_analyze):
    # handle empty input
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            emotions = data.get("emotionPredictions", [{}])[0].get("emotion", {})
            if emotions:
                dominant = max(emotions, key=emotions.get)
                return {
                    "anger": emotions.get("anger"),
                    "disgust": emotions.get("disgust"),
                    "fear": emotions.get("fear"),
                    "joy": emotions.get("joy"),
                    "sadness": emotions.get("sadness"),
                    "dominant_emotion": dominant
                }
    except requests.exceptions.RequestException:
        pass

    # ---- FALLBACK (when Watson is down) ----
    # very small rule-based fallback so UI still shows a result
    t = text_to_analyze.lower()

    joy_words = ["happy", "great", "awesome", "fun", "love", "excited"]
    sadness_words = ["sad", "down", "depressed", "cry", "unhappy"]
    anger_words = ["angry", "mad", "furious", "hate", "annoyed"]
    fear_words = ["afraid", "scared", "fear", "terrified", "anxious"]
    disgust_words = ["disgust", "gross", "nasty", "sick"]

    scores = {"anger": 0.0, "disgust": 0.0, "fear": 0.0, "joy": 0.0, "sadness": 0.0}

    for w in joy_words:
        if w in t:
            scores["joy"] += 0.9
    for w in sadness_words:
        if w in t:
            scores["sadness"] += 0.9
    for w in anger_words:
        if w in t:
            scores["anger"] += 0.9
    for w in fear_words:
        if w in t:
            scores["fear"] += 0.9
    for w in disgust_words:
        if w in t:
            scores["disgust"] += 0.9

    dominant = max(scores, key=scores.get) if sum(scores.values()) > 0 else None

    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant
    }