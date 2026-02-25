from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    # Serves the UI page
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Gets the text from query string
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Call the emotion detector (Watson API wrapper)
    result = emotion_detector(text_to_analyze)

    # If blank input OR Watson failed -> required message
    if result is None or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Return a readable response for the UI
    return (
        f"For the given statement, the system response is {result}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    # IMPORTANT for Skills Network / Codespaces
    app.run(host="0.0.0.0", port=5000)