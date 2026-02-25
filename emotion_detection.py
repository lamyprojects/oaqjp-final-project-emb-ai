import requests

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/emotionDetection"

    payload = {"text": text_to_analyze}

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = response.json()

    emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

    anger = emotions.get("anger")
    disgust = emotions.get("disgust")
    fear = emotions.get("fear")
    joy = emotions.get("joy")
    sadness = emotions.get("sadness")

    dominant_emotion = max(emotions, key=emotions.get) if emotions else None

    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return result 
