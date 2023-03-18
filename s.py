import mysql.connector
#Alexis Password:dd020912#
#Kits Password: 911Apexpredator
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="911Apexpredator"
)

if mydb.is_connected():
    print("Connection Established")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MusicApp.users")
results = mycursor.fetchall()
print(results)
mycursor.execute('''INSERT INTO MusicApp.users (user_id, email, password) VALUES (%s, %s, %s)''', (4, "004@bu.edu", 1234))
mydb.commit()
