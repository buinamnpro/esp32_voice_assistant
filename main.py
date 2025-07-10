from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "🚀 Server Flask dang chay tren Render!"

@app.route("/voice", methods=["POST"])
def handle_voice():
    return jsonify({"message": "Dang xu ly giong noi..."})
