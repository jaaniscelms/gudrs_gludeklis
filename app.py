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
 return render_template("skola.html")
#================================= skolas tabulas dati ========================================
@app.route('/skola/dati', methods=['GET'])
def datiskolas():
    try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT  pasniedzejs.vards,pasniedzejs.uzvards, pasniedzejs.epasts, pasniedzejs.telefons, prieksmeti.prieksmets FROM pasniedzejs JOIN prieksmeti ON pasniedzejs.prieksmeta_id = prieksmeti.prieksmeta_id ")
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
#==========================================================

#================================= audzinatajs tabulas dati ========================================
@app.route('/klasesdati/dati', methods=['GET'])
def datiklases():
    try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT  klases.klase, pasniedzejs.vards, pasniedzejs.uzvards FROM audzinatajs JOIN klases ON audzinatajs.klases_id = klases.klases_id JOIN pasniedzejs ON audzinatajs.pasniedzeja_id = pasniedzejs.pasniedzeja_id ")
        data = c.fetchall()
        jsonData = ''
        column_names = ['klase','vards','uzvards']
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
#==========================================================


#================================= audzinatajs tabulas dati ========================================
@app.route('/klasesstundas/dati', methods=['GET'])
def datiklasesstundas():
    try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT  klases.klase, pasniedzejs.vards, pasniedzejs.uzvards FROM audzinatajs JOIN klases ON audzinatajs.klases_id = klases.klases_id JOIN pasniedzejs ON audzinatajs.pasniedzeja_id = pasniedzejs.pasniedzeja_id ")
        data = c.fetchall()
        jsonData = ''
        column_names = ['klase','vards','uzvards']
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
#=========================klase_edit dati=================================
@app.route('/stundas/dati', methods=['GET'])
def stundas():
    try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT  dienas.diena,laiks.laiks_id,klases.klase,prieksmeti.prieksmets, pasniedzejs.vards, pasniedzejs.uzvards, laiks.laiki, stundas.notiek FROM stundas JOIN dienas ON stundas.dienas_id = dienas.dienas_id JOIN laiks ON stundas.laiks_id = laiks.laiks_id JOIN prieksmeti ON stundas.prieksmeta_id = prieksmeti.prieksmeta_id JOIN pasniedzejs ON stundas.pasniedzeja_id = pasniedzejs.pasniedzeja_id JOIN klases ON stundas.klases_id = klases.klases_id WHERE  klases.klase LIKE '1.c'")
        data = c.fetchall()
        jsonData = ''
        column_names = ['diena','laiks','klase','prieksmeti','vards', 'uzvards', 'laiki', 'notiek']
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

#=========================klase_tv dati=================================
@app.route('/stundas_tv/dati', methods=['GET'])
def stundas_tv():
    try:
       with sqlite3.connect("Dati.db") as conn:
        conn=sqlite3.connect('Dati.db')
        c = conn.cursor()
        c.execute("SELECT stundas.stundas_id, klases.klase,prieksmeti.prieksmets,laiks.laiki,stundas.dienas_id FROM stundas JOIN dienas ON stundas.dienas_id = dienas.dienas_id JOIN laiks ON stundas.laiks_id = laiks.laiks_id JOIN prieksmeti ON stundas.prieksmeta_id = prieksmeti.prieksmeta_id  JOIN klases ON stundas.klases_id = klases.klases_id  WHERE  (klases.klase LIKE '1.c'  AND stundas.dienas_id LIKE '1')")
        data = c.fetchall()
        jsonData = ''
        column_names = ['stundasid','klase','prieksmeti', 'laiks','diena']
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




















if __name__=="__main__":
    app.run(debug=True)
