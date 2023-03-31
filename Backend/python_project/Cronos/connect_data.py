import mysql.connector 

class ConnectData:
    def conectar_data(self, table):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "14072849",
            database = table
        )
        print("its done!")

ConnectData().conectar_data(table = "Aviator")