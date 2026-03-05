from flask import Flask, request, render_template_string, jsonify
import hashlib, os

app = Flask(__name__)
OTP = "181996"

# HTML template for landing page
HTML = """
<!doctype html>
<html>
<head>
  <title>Side-Channel Lab</title>
</head>
<body>
  <h1>Welcome to Side-Channel Attack Lab</h1>
  <p>Enter your 6-digit OTP</p>

  <form action="/verify" method="POST">
    <input type="text" name="otp" maxlength="6" />
    <button type="submit">Verify</button>
  </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/verify", methods=["POST"])
def verify():
    guess = request.form.get("otp", "")
    
    if OTP.startswith(guess):
        for _ in range(100000):
            hashlib.sha256(b"x").digest()

    if guess == OTP:
        return "Correct OTP!"
    else:
        return "Incorrect OTP"
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
