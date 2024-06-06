from flask import Flask, jsonify, request, redirect, send_file
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
        print('end')
        response = req.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
        if response.status_code != 200:
            return jsonify({"res":"Failed to get response from API"}), 500
        with open('inputfile.flac', 'wb') as f:
            f.write(response.content)
        
        # Convert FLAC to MP3 using Audio Conversion API
        AUDIO_CONVERSION_API_URL = 'https://api.audioconversion.com/convert'
        files = {'file': open('inputfile.flac', 'rb')}
        data = {'outputformat': 'mp3'}
        conversion_response = req.post(AUDIO_CONVERSION_API_URL, files=files, data=data)
        if conversion_response.status_code != 200:
            return jsonify({"res":"Failed to convert audio file"}), 500
        with open('output.mp3', 'wb') as f:
            f.write(conversion_response.content)
        
        return send_file('output.mp3', mimetype='audio/mpeg')
    except Exception as e:
        print(e)
        return jsonify({"res":"An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
