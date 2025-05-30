from flask import Flask, request

app = Flask(__name__)
message = "Waiting..."

@app.route('/')
def home():
    return message

@app.route('/set', methods=['GET'])
def set_message():
    global message
    new_message = request.args.get('message')
    if new_message:
        message = new_message
        return f"Message set to: {message}"
    return "No message provided", 400
