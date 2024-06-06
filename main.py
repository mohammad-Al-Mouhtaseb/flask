from flask import Flask, jsonify, request, redirect, send_file, Response
import os
import requests as req

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        print('start')
        desc=request.args.get('desc', '')
        print(desc)
        API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
        headers = {"Authorization": "Bearer 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"}
        audio_bytes = {
            "inputs": desc
        }
        print('1')
        response = req.post(API_URL, headers=headers, json=audio_bytes)
        print('2')
        if response.status_code != 200:
            return jsonify({"res":"Failed to get response from API"})
        print('3')
        return Response(response.content, mimetype='audio/flac')
    except Exception as e:
        print(e)
        return jsonify({"res":"An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
