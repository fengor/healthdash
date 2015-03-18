import sqlite3

con = sqlite3.connect('healthdash.db') # Warning: This file is created in the current directory
con.execute("INSERT INTO bodyweight (date, weight, bodyfat, leanbodymass) VALUES ('2015-01-01', 80.5, 22.7, 62.23)")

con.commit()
