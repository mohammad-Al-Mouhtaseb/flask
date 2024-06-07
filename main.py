from flask import Flask, jsonify, request, Response
import os
import requests as req

app = Flask(__name__)

@app.route('/')
def index():
    desc = request.args["desc"]
    key = request.args["key"]
    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer "+key}
    audio_bytes = {
        "inputs": desc,
    }
    res = req.post(API_URL, headers=headers, json=audio_bytes)
    return Response(res)#content

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
