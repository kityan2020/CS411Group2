import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dd020912#"
)

if mydb.is_connected():
    print("Connection Established")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MusicApp.users")
results = mycursor.fetchall()
print(results)
mycursor.execute('''INSERT INTO MusicApp.users (user_id, email, password) VALUES (%s, %s, %s)''', (3, "003@bu.edu", 1234))
mydb.commit()
