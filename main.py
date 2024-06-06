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
        print('1')
        response = req.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
        print('2')
        if response.status_code != 200:
            return jsonify({"res":"Failed to get response from API"}), 500
        with open('inputfile.flac', 'wb') as f:
            f.write(response.content)
        
        print('3')
        # Convert FLAC to MP3 using Audio Conversion API
        AUDIO_CONVERSION_API_URL = 'https://api.audioconversion.com/convert'
        files = {'file': open('inputfile.flac', 'rb')}
        data = {'outputformat': 'mp3'}
        print('4')
        conversion_response = req.post(AUDIO_CONVERSION_API_URL, files=files, data=data)
        print('5')
        if conversion_response.status_code != 200:
            return jsonify({"res":"Failed to convert audio file"}), 500
        with open('output.mp3', 'wb') as f:
            f.write(conversion_response.content)
        
        print('end')
        return send_file('output.mp3', mimetype='audio/mpeg')
    except Exception as e:
        print(e)
        return jsonify({"res":"An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
