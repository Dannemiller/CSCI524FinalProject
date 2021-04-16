import datetime
import mysql.connector
from mysql.connector import errorcode
class SQLCustomClass:
    def __init__(self, user, password, hostIP, databaseName):
        self.user = user
        self.password = password
        # storing password in memory address might cause security concerns, how can this be accounted for
        self.hostIP = hostIP
        self.databaseName = databaseName

        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.hostIP,
                                                  database=self.databaseName)

        self.connection.close()

    def createConnection(self):
        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.hostIP, database=self.databaseName)

    def closeConnection(self):
        self.connection.close()

    def retreiveStationSchedule(self):
        cursor = self.connection.cursor()
        query = ("SELECT * FROM")


    query = ("SELECT * FROM Stops WHERE StopID LIKE RBG%")

    cursor.execute(query)

    cursor.close()
