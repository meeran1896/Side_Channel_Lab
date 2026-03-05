from flask import Flask, request
import random

app = Flask(__name__)
SECRET = "alamak"

@app.route("/check")
def check():
    guess = request.args.get("q", "")
    if SECRET.startswith(guess):
        padding = "A" * 1000
    else:
        padding = "A" * 500
    noise = "C" * random.randint(0, 100)
    return padding + noise

app.run(host="0.0.0.0", port=5003)
