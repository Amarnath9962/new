import sqlite3
connection= sqlite3.connect('basic.db')
cursor=connection.cursor()
#cursor.execute("create table Baby(number text, month text)")
#cursor.execute("insert into Baby values(123,'march')")
cursor.execute("insert into baby values(1234,'feb')")
connection.commit()
connection.close()
