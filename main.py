from flask import Flask, jsonify
import os
import requests
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.body)
    desc=data['desc']
    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer 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"}
    audio_bytes = {
        "inputs": desc
    }
    response = requests.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
    return jsonify({"res":"sucsess"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
