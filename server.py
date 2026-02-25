from flask import Flask, request, render_template
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    return (
        f"Anger: {result['anger']}<br>"
        f"Disgust: {result['disgust']}<br>"
        f"Fear: {result['fear']}<br>"
        f"Joy: {result['joy']}<br>"
        f"Sadness: {result['sadness']}<br><br>"
        f"<b>Dominant Emotion: {result['dominant_emotion']}</b>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)