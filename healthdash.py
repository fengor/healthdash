from bottle import route, run, request
import sqlite3
import re
import pygal

@route('/hello')
def hello():
        return "Hello World!"

def load_all_weights():
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("SELECT date, weight, bodyfat, leanbodymass FROM bodyweight")
    result = c.fetchall()
    return result

def get_all_weights():
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("SELECT weight FROM bodyweight")
    result = c.fetchall()
    return result

def load_weight(datestring):
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("SELECT date, weight, bodyfat, leanbodymass FROM bodyweight WHERE date=?", (datestring,))
    result = c.fetchall()
    return result

def insert_weight_entry(date, weight, bodyfat, leanbodymass):
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO bodyweight (date, weight, bodyfat, leanbodymass) VALUES (?,?,?,?)", (date, weight, bodyfat, leanbodymass))
    conn.commit()

def delete_weight_entry(date, ):
    conn = sqlite3.connect('healthdash.db')
    c = conn.cursor()
    c.execute("DELETE FROM bodyweight WHERE date = ?", (date, ))
    conn.commit()

@route('/dash/weight')
def weight_graph():

    weight_entries = load_all_weights() 
    print(weight_entries)
    weight_chart = pygal.Line()
    weight_chart.title = "Bodyweight"
    weight_chart.x_labels = [i[0] for i in weight_entries]
    weight_chart.add('total bw', [i[1] for i in weight_entries])
    weight_chart.add('lean body mass', [i[3] for i in weight_entries])
    
    return weight_chart.render()
    #return "foobar"

@route('/weight', method='GET')
def weight():
    weightlist = load_all_weights()
    return str(weightlist)

@route('/weight', method='POST')
@route('/weight', method='PUT')
def add_weight():
    #TODO add parameter validation
    date = request.POST.get('date','').strip()
    weight = float(request.POST.get('weight',0))
    bodyfat = float(request.POST.get('bodyfat',0))
    leanbodymass = weight - (weight * bodyfat / 100)

    insert_weight_entry(date, weight, bodyfat, leanbodymass)

    return "entry added for %s with weight %f kg, bodyfat %f. Computed lean mass: %fkg\n" % (date,weight,bodyfat,leanbodymass)

#@route('/weight/:datestring#\d{4}-d{2}-\d{2}#', method='GET')
@route('/weight/:datestring', method='GET')
def show_weight_for_date(datestring):
    if re.match("\d{4}-\d{2}-\d{2}",datestring) is None:
        return "Please use the YYYY-MM-DD format"
    weightentry = load_weight(datestring)
    return str(weightentry)

@route('/weight/:date', method='PUT')
def show_weight_for_date(date):
    if re.match("\d{4}-\d{2}-\d{2}",date) is None:
        return "Please use the YYYY-MM-DD format"
    weight = float(request.POST.get('weight',0))
    bodyfat = float(request.POST.get('bodyfat',0))
    leanbodymass = weight - (weight * bodyfat / 100)

    insert_weight_entry(date, weight, bodyfat, leanbodymass)

    return "entry added for %s with weight %f kg, bodyfat %f. Computed lean mass: %fkg\n" % (date,weight,bodyfat,leanbodymass)

@route('/weight/:date', method='DELETE')
def show_weight_for_date(date):
    if re.match("\d{4}-\d{2}-\d{2}",date) is None:
        return "Please use the YYYY-MM-DD format"
    delete_weight_entry(date)
    return "entry deleted for date %s" % date

run(host='localhost', port=8000, debug=True, reloader=True)
