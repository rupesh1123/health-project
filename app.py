from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_logic import get_ai_response 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the AI Health & Fitness API!"
@app.route("/api/voice_command", methods=["POST"])
def voice_command():
    data = request.json
    command = data.get("command", "").lower()

    # Simple logic (expand this)
    if "water" in command:
        response = "Water logged. Stay hydrated!"
    elif "goal" in command:
        response = "Your goal is to lose 5 kg in 2 months."
    else:
        response = "Sorry, I didn't understand that."
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
