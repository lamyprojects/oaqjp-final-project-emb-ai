from flask import Flask, request, render_template
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")

    # samo prazan input je invalid
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # PRIKAŽI rezultat uvijek (fallback daje brojeve)
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