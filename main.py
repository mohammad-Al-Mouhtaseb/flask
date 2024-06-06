from flask import Flask, jsonify, request, Response
import os
import requests as req

app = Flask(__name__)

@app.route('/')
def index():
    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer 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"}
    audio_bytes = {
        "inputs": "paly",
    }
    return Response(response.content)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
