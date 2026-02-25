from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # If input is invalid or Watson fails
    if result is None or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Return HTML so it displays nicely in the UI
    return (
        f"Anger: {result.get('anger')}<br>"
        f"Disgust: {result.get('disgust')}<br>"
        f"Fear: {result.get('fear')}<br>"
        f"Joy: {result.get('joy')}<br>"
        f"Sadness: {result.get('sadness')}<br><br>"
        f"<b>Dominant Emotion: {result.get('dominant_emotion')}</b>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)