from flask import Flask, jsonify, request, Response
import os
from experta import *

app = Flask(__name__)

@app.route('/')
def index():
    a1=int(request.args['a1'])#Stress
    a2=int(request.args['a2'])#Anxiety
    a3=int(request.args['a3'])#Depression
    a4=int(request.args['a4'])#Stress
    a5=int(request.args['a5'])#Depression
    a6=int(request.args['a6'])#Anxiety
    a7=int(request.args['a7'])#Depression
    a8=int(request.args['a8'])#Anxiety
    class Robot(KnowledgeEngine):
        @Rule(NOT(Fact(Depression=W())))
        def Depression(self):
            self.declare(Fact(Depression=bool((a3+a5+a7)>=4)))

        @Rule((Fact(Depression=W())) and (NOT(Fact(Anxiety=W()))))
        def Anxiety(self):
            self.declare(Fact(Anxiety=bool((a2+a6+a8)>=4)))

        @Rule((Fact(Anxiety=W())) and (NOT(Fact(Stress=W()))))
        def Stress(self):
            self.declare(Fact(Stress=bool((a1+a4)>=3)))
            
    engine = Robot()
    engine.reset()
    engine.run()
    facts=list(engine.facts.items())
    d=str(facts[1])
    a=str(facts[2])
    s=str(facts[3])
    d=d[9:len(d)-2]
    a=a[9:len(a)-2]
    s=s[9:len(s)-2]
    d=d.split('=')
    a=a.split('=')
    s=s.split('=')
    if(d[1]=="True"):
        a[1]="False"
        s[1]="False"
        iris.das_d=True
    elif(a[1]=="True"):
        s[1]="False"
        iris.das_a=True
    elif(s[1]=="True"):
        iris.das_s=True

    return Response({d[0]:d[1],a[0]:a[1],s[0]:s[1]})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
