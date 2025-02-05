# -*- coding: utf-8 -*-
"""Prueba-v0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e1m7ytJX3Gpcm7ht9iiszDAKxkxMs4w5
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

def concatenar(valor1, valor2):
  return valor1 + valor2

@app.route("/concatenar", methods=["POST"])
def procesar():
  datos = request.json
  resultado = concatenar(datos["valor1"], datos["valor2"])
  return jsonify({"resultado": resultado})

if __name__ == "__main__":
  app.run(debug=True)