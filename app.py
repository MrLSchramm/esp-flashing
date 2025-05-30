from flask import Flask, request

app = Flask(__name__)
current_message = "Hello World!"

@app.route('/')
def get_message():
    return current_message

@app.route('/set')
def set_message():
    global current_message
    msg = request.args.get('message')
    if msg:
        current_message = msg
        return f"Message updated to: {current_message}"
    return "No message provided."
