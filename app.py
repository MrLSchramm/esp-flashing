from flask import Flask, request, jsonify
import os

app = Flask(__name__)

current_command = {"command": "off"}

@app.route("/command", methods=["GET"])
def get_command():
    return jsonify(current_command)

@app.route("/command", methods=["POST"])
def set_command():
    data = request.get_json()
    if "command" in data:
        current_command["command"] = data["command"]
        return jsonify({"status": "ok", "command": current_command["command"]})
    return jsonify({"status": "error", "message": "Missing 'command'"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
