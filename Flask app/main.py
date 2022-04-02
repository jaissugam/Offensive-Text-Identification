from flask import Flask, redirect, url_for, render_template, request
import newIdentifier
app = Flask(__name__)


@app.route("/")
def home():
    if request.method == "POST":
        inp = request.form["userInput"]
        return redirect(url_for("res", message=inp))
    else:
        return render_template("index.html")


@app.route("/result")
def res(message):
    out = newIdentifier.checkMessage(message)
    if out == 0:
        return f"<h1>NOT OFFENSIVE</h1>"
    else:
        return f"<h1>OFFENSIVE</h1>"


if __name__ == "__main__":
    app.run(debug=True)