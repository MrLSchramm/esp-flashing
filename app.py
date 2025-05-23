from flask import Flask, request, jsonify

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
