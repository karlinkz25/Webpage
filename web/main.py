from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/home/<ime_podjetja>")
def home(ime_podjetja):
    return render_template("main.html", ime_podjetja=ime_podjetja)

@app.route("/test/")
def test():
    return render_template("form_test.html")

@app.route("/prijava-submit/")
def handle_form():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("password")
    print(uporabnisko_ime, geslo)
    select_usr = 'select * from contacts where first_name = "'+uporabnisko_ime+'" and last_name="'+geslo+'";'
    print(select_usr)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(select_usr)
    ls = cursor.fetchall()
    if len(ls) > 0 :
        return "prijava uspela"
    else:
        return "ne dela"
    
    
    
@app.route('/view_db/')
def view_db():
    conn =sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from Contacts;")
    return (cursor.fetchall())


@app.route('/registracija/')
def registracija():
    return render_template("registracija.html")

@app.route('/registracija-submit/')
def registracija_submit():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("password")
    print(uporabnisko_ime, geslo)
 

app.run(debug=True)