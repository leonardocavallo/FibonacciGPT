from flask import Flask, jsonify, render_template, request
from modules import FibonacciGPT
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ai-response', methods=['POST'])
def ai_response():
    data = request.json
    headers = request.headers

    if not data or "prompt" not in data:
        return {"response": "Errore Nella Richiesta"}, 400

    if "chiavesupersegreta" not in headers:
        return {"response": "Errore Nella Richiesta"}, 400

    if headers["chiavesupersegreta"] == "malig":
        prompt = data["prompt"]
        response = {"response": FibonacciGPT.generate(prompt)}
        return response
    else:
        return {"response": "Richiesta Non Autorizzata"}, 401

if __name__ == '__main__':
    app.run(debug=True)