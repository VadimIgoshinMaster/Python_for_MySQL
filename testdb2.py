import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerty123",
    database="testdb"

)

mycursor = mydb.cursor()

sql1 = "SELECT * FROM students WHERE name LIKE '%an%'"

sql2 = "UPDATE students SET age = 17 WHERE name = 'Anna'"

mycursor.execute(sql1)
mycursor.execute(sql2)

myresult= mycursor.fetchall()

myresult1= mycursor.fetchone()

for row in myresult:
    print(row)

for onerow in myresult1:
    print(onerow)

mydb.commit()  