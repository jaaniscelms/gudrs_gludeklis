from flask import Flask, redirect, url_for,render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/klase_tv")
def klase_tv():
    return render_template("klase_tv.html")

@app.route("/klase_edit")
def klase_edit():
    return render_template("klase_edit.html")

@app.route("/klases")
def klases():
    return render_template("klases.html")

@app.route("/skola")
def skola():
    return render_template("skola.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        return redirect(url_for("skola"))
    else:
        return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)