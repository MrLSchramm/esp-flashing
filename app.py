from flask import Flask, request

app = Flask(__name__)

current_message = "Waiting for message..."

@app.route("/")
def home():
    return current_message

@app.route("/set", methods=["GET"])
def set_message():
    global current_message
    message = request.args.get("message")
    if message:
        current_message = message
        return f"Message updated to: {message}"
    return "No message provided"
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host='0.0.0.0', port=port)
