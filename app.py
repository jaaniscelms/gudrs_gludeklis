import os
from flask import Flask, redirect, url_for,render_template,request

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/klase_tv")
def klase_tv():
    return render_template("klase_tv.html")

@app.route("/klases")
def klases():

    return render_template("klases.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        usr=request.form["user"]
        pasw=request.form["password"]
        if usr=="admin" and pasw=="admin":
             return redirect(url_for("skola"))
        else: 
            return redirect(url_for("login"))
    else: 
     return render_template("login.html")
headings=("Nr.","Priekšmets", "Pasniedzejs", "Laiks","Nenotiek","Darbības")
data=(
    (1,"Vēsture","Andris Bērziņš","9:15 - 9:55","unchecked"),
    (2, "Sports","Pēteris Skuja","10:15 - 10:55","checked"),
    (3,"Ekonomika","Anna Panna","11:20 - 12:05", "unchecked"),
    (4,"Matemātika","Valdis Liepa","12:35 - 13:05","checked"),
    (5,"Mājturība","Elita Bērziņa","12:20 - 14:00", "checked")
)
@app.route("/klase_edit")
def klase_edit():
    return render_template("klase_edit.html",headings=headings, data=data)

@app.route("/skola")
def skola():
    return render_template("skola.html")

if __name__=="__main__":
    app.run(debug=True)