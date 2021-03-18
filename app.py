import os
from flask import Flask, redirect, url_for,render_template,request, json, jsonify
import sqlite3

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

@app.route("/klase_edit")
def klase_edit():
    return render_template("klase_edit.html")

@app.route("/skola")
def skola():
    
    """ try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT  pasniedzejs.vards, pasniedzejs.uzvards, pasniedzejs.epasts, pasniedzejs.telefons, prieksmeti.prieksmets FROM pasniedzejs JOIN prieksmeti ON pasniedzejs.prieksmeta_id = prieksmeti.prieksmeta_id ")
        data = c.fetchall()
        jsonData = ''
        column_names = ['vards','uzvards','epasts','telefons','prieksmets']
        for row in data:          
            info = dict(zip(column_names, row))
            jsonData = jsonData + json.dumps(info) + ','
        jsonData = jsonData[:-1]
        jsonData = '[' + jsonData + ']'
        msg = "Ieraksti veiksmīgi saņemti un apstrādāti"
        print(msg)
    except:
      conn.rollback()
      msg = "Ir notikusi kļūda datu saņemšanā un apstrādāšanā"
      print(msg)
    finally:
      conn.commit()
      c.close()
      conn.close()    
      return jsonData

"""
    return render_template("skola.html")

if __name__=="__main__":
    app.run(debug=True)
