from flask import Flask, jsonify, request, Response
import os
import requests as req

app = Flask(__name__)

@app.route('/music')
def music():
    desc = request.args["desc"]
    key = request.args["key"]
    API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
    headers = {"Authorization": "Bearer "+key}
    audio_bytes = {
        "inputs": desc,
    }
    res = req.post(API_URL, headers=headers, json=audio_bytes)
    return Response(res.content)

@app.route('/expert')
def expert():
    a1=int(request.args['a1'])#Stress
    a2=int(request.args['a2'])#Anxiety
    a3=int(request.args['a3'])#Depression
    a4=int(request.args['a4'])#Stress
    a5=int(request.args['a5'])#Depression
    a6=int(request.args['a6'])#Anxiety
    a7=int(request.args['a7'])#Depression
    a8=int(request.args['a8'])#Anxiety

    depression = (a3+a5+a7)*3
    anxiety = (a2+a6+a8)*3
    stress = (a1+a4)*4

    if depression>=anxiety and depression>=stress:
        depression=True
        anxiety=False
        stress=False
    elif anxiety>=stress:
        depression=False
        anxiety=True
        stress=False
    else:
        depression=False
        anxiety=False
        stress=True
        
    return jsonify({'Depression': depression, 'Anxiety': anxiety, 'Stress': stress})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
