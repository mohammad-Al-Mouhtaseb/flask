from flask import Flask, jsonify
import os
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import requests, scipy, torch
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index(): data = json.loads(request.body)
    desc=data['desc']
    doctor=data['doctor']
    patient=data['patient']
    type=data['type']

    # music_path="sounds/music/"+type+"_"+desc+".flac"

    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    key=Music.objects.get(doctor="api@api.com").type
    print(key)  
    headers = {"Authorization": "Bearer "+key}
    audio_bytes = {
        "inputs": desc
    }
    response = requests.post(API_URL, headers=headers, json=audio_bytes, timeout=120)
    # music=Music.objects.create(doctor=doctor,patient=patient,music_path=music_path,type=type)
    # music.save()
    return jsonify({"res":"sucsess"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
