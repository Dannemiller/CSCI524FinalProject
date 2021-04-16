import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ra BushMan\Downloads\RailwayDatabase.accdb;')
cursor = conn.cursor()
Roma = 'Roma'
cursor.execute('SELECT Train, Line, Destination, DepartureTime FROM TrainSchedule')

for row in cursor.fetchall():
    print(row)
