from flask import Flask, jsonify, request, redirect, send_file
from pydub import AudioSegment
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
        response = req.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
        print('2')
        if response.status_code != 200:
            return jsonify({"res":"Failed to get response from API"}), 500
        with open('inputfile.flac', 'wb') as f:
            f.write(response.content)
        
        print('3')
        song = AudioSegment.from_file("inputfile.flac", "flac")
        song.export("output.mp3", format="mp3")
        if not os.path.exists('output.mp3'):
            print('end')
            return jsonify({"res":"Failed to convert audio file"}), 500
        return send_file('output.mp3', mimetype='audio/mpeg')
    except Exception as e:
        print(e)
        return jsonify({"res":"An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
