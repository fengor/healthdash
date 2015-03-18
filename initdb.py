import sqlite3

con = sqlite3.connect('healthdash.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE if not exists bodyweight (id INTEGER PRIMARY KEY, date date NOT NULL, weight numeric NOT NULL, bodyfat numeric, leanbodymass numeric)")

con.commit()
