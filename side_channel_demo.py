from flask import Flask, request, send_from_directory, abort
import time, os

app = Flask(__name__)

SECRET = "cat"
@app.route("/check", methods=["POST"])
def check():
    guess = request.form.get("guess", "")

    for i in range(min(len(guess), len(SECRET))):
        if guess[i] != SECRET[i]:
            return "Wrong"
        time.sleep(1)   

    if guess == SECRET:
        return "Correct!"
    return "Wrong"
        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
