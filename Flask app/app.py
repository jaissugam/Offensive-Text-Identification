from flask import Flask, redirect, render_template, request, session,url_for
import newIdentifier
app = Flask(__name__)
app.secret_key = "random"


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        session.pop("messages", None)
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/textInput", methods=['GET', 'POST'])
def home():
    session.pop("messages", None)
    return render_template("index.html")


@app.route("/fileInput", methods=['GET', 'POST'])
def home2():
    session.pop("messages", None)
    return render_template("newindex.html")


@app.route("/resultText", methods=['GET', 'POST'])
def res():
    session.pop("messages", None)
    if request.method == "GET":
        return redirect(url_for('index'))

    elif request.method == "POST":
        result = request.form.get('userInput')
        resultList = [result]
        mes, out = newIdentifier.checkMessage(resultList)
        for i in range(len(mes)):
            resultNew = str(out[i])
            if resultNew == "[0]":
                resultNew = "NOT OFFENSIVE"
            else:
                resultNew = "OFFENSIVE"
            message = mes[i].strip() + ": " + resultNew
            if "messages" in session:
                session["messages"].extend([message])
            else:
                session["messages"] = [message]

    return render_template("resultDisplay.html")


@app.route("/resultFile", methods=['GET', 'POST'])
def reslt():
    session.pop("messages", None)
    if request.method == "GET":
        return redirect(url_for('index'))

    else:
        document = request.files["doc"]
        document.save(document.filename)
        mes, out = newIdentifier.checkDocument(document.filename)
        for i in range(len(mes)):
            resultNew = str(out[i])
            if resultNew == "0":
                resultNew = "NOT OFFENSIVE"
            else:
                resultNew = "OFFENSIVE"
            message = mes[i].strip() + ": " + resultNew
            if "messages" in session:
                session["messages"].extend([message])
            else:
                session["messages"] = [message]
        return render_template("resultDisplay.html")


if __name__ == "__main__":
    app.run(debug=False)
