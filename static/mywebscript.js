function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;

  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState === 4) {
      document.getElementById("system_response").innerHTML = this.responseText;
    }
  };

  const url = "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze);
  xhttp.open("GET", url, true);
  xhttp.send();
}