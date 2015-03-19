import sqlite3
import random
from datetime import datetime, timedelta

startdate = datetime.strptime("2015-01-01","%Y-%m-%d")
entries = []

for x in range(0, 10):
    entries.append((startdate+timedelta(days=x), 80+(random.randint(-40,40)/10), 23+random.randint(-5,5)))


con = sqlite3.connect('healthdash.db') # Warning: This file is created in the current directory

c = con.cursor()
c.executemany("INSERT OR REPLACE INTO bodyweight (date, weight, bodyfat) VALUES (?, ?, ?)", entries)
c.execute("UPDATE bodyweight SET leanbodymass=(weight-(weight*bodyfat/100))")

con.commit()
