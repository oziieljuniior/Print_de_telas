import mysql.connector

mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "14072849",
            database = "Aviator"
        )

mycursor = mydb.cursor()

sql = "INSERT INTO odds (id, odd, hora_criacao, apostadores) VALUES (%s,%s,%s,%s)"

values = 