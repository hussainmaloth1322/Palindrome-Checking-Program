"""Flask palindrome API deployed by Kubernetes."""
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_palindrome(value):
    normalized = value.strip().lower()
    return normalized == normalized[::-1]

@app.get("/")
def home():
    return "Palindrome Checker Application"

@app.get("/check")
def check():
    word = request.args.get("word")
    if word is None or word.strip() == "":
        return jsonify({"error": "Please provide a word using ?word=VALUE"}), 400
    return jsonify({"word": word, "palindrome": is_palindrome(word)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
