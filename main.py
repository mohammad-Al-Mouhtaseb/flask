from flask import Flask, jsonify, request, redirect, send_file
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
    with open('inputfile.flac', 'wb') as f:
        f.write(response.content)
    os.system('ffmpeg -i inputfile.flac output.mp3')
    return send_file('output.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
