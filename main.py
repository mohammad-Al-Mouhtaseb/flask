from flask import Flask, jsonify, request, redirect
import os
import requests as req
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print('start')
    desc=request.args['desc']
    print(desc)
    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer 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"}
    audio_bytes = {
        "inputs": desc
    }
    print('end')
    response = req.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
    return jsonify({"res":"sucsess"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
