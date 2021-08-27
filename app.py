from transformers import pipeline
from typing import List
from flask import Flask, request, jsonify


# create the zero-shot classifier
classifier = pipeline(
    "zero-shot-classification", model="facebook/bart-large-mnli"
)


# classify function
def classify(sentence: str, labels: List[str], multi_label: int = 0):
    if (multi_label == 0):
        return classifier(sentence, labels, multi_label=False)
    else:
        return classifier(sentence, labels, multi_label=True)


# flask server
app = Flask(__name__)

# define flash routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json

        if data is None:
            return jsonify({"error": "Invalid JSON request"})
        elif not ("sentence" in data and "labels" in data):
            return jsonify(
                {
                    "error": "'sentence' and/or 'labels' field(s) not present in JSON request"
                }
            )
        elif not (
            isinstance(data["sentence"], str)
            and isinstance(data["labels"], list)
        ):
            return jsonify(
                {
                    "error": "'sentence' field is not a string and/or 'labels' field is not a list of strings"
                }
            )
        elif "multi_label" in data and not (isinstance(data["multi_label"], int)):
            return jsonify(
                {
                    "error": "'multi_label' field is not an integer"
                }
            )

        try:
            if ("multi_label" in data):
                result = classify(data["sentence"], data["labels"], data["multi_label"])
            else:
                result = classify(data["sentence"], data["labels"])
            return jsonify(result)
        except Exception as exception:
            return jsonify({"error": str(exception)})

    return """<h1>Flask Server Running</h1>
        <p>
            Send a JSON POST request in the format
            {
                "sentence": "...",
                "labels": ["...", "...", "..."]
                "multi_label": 0 / 1
            }
            to get predictions
        </p>"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)

