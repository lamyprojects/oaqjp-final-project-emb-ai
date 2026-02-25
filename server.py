from flask import Flask, jsonify, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the main UI page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    API endpoint used by mywebscript.js:
    /emotionDetector?textToAnalyze=<text>
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # Task 7: when dominant_emotion is None -> return required message
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # This string displays nicely in the provided UI (mywebscript.js injects responseText)
    return (
        f"For the given statement, the system response is {result}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)