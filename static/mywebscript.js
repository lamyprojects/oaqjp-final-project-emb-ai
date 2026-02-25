function RunSentimentAnalysis() {

    const textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then(response => response.text())
        .then(data => {
            document.getElementById("system_response").innerHTML = data;
        })
        .catch(error => {
            document.getElementById("system_response").innerHTML =
                "Error: " + error;
        });
}