from bottle import route, run
import sqlite3
import re

@route('/hello')
def hello():
        return "Hello World!"

def load_all_weights():
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("SELECT date, weight, bodyfat, leanbodymass FROM bodyweight")
    result = c.fetchall()
    return result

def load_weight(datestring):
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("SELECT date, weight, bodyfat, leanbodymass FROM bodyweight WHERE date=?", (datestring,))
    result = c.fetchall()
    return result

@route('/weight')
def weight():
    weightlist = load_all_weights()
    return str(weightlist)

@route('/weight/:datestring#\d{4]-\d{2}-\d{2}#', method='GET')
def show_weight_for_date(datestring):
    weightentry = load_weight(datestring)
    return str(weightentry)


run(host='localhost', port=8000, debug=True, reloader=True)
