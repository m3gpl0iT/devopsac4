import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def ac4():
   p = 1
   a = 0
   limite = 50
   contador = 0
   resposta = "0,"
   while (contador < limite):
       tmp = p
       p = p + a
       a = tmp
       contador=contador+1
       resposta+= str(p) + ","


   return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5777))
    app.run(host='0.0.0.0', port=port) 
