from flask import Flask, render_template, request
from chatter import GenerateResponse  # Import your existing function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            response = GenerateResponse(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
