from flask import Flask, request, render_template_string
import time, os

app = Flask(__name__)

USERS = {
    "admin": "m33r@n1896@!"
}

LOGIN_HTML = """
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit">
</form>
<p style="color:red;">{{ error }}</p>
"""

SUCCESS_HTML = """
<h2>Welcome {{ user }}</h2>
<p>Login successful!</p>
"""

def insecure_password_check(user_input, real_password):
    for i in range(min(len(user_input), len(real_password))):
        if user_input[i] != real_password[i]:
            return False
        time.sleep(0.05)
    return len(user_input) == len(real_password)

@app.route("/", methods=["GET", "POST"])
def login():
    error = "Invalid credentials"
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user in USERS:
            if insecure_password_check(pwd, USERS[user]):
                return render_template_string(SUCCESS_HTML, user=user)

    return render_template_string(LOGIN_HTML, error=error)
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=5001)

    

