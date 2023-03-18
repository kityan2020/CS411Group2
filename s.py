import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="911Apexpredator"
)

if mydb.is_connected():
    print("Connection Established")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM musicapp.users")
results = mycursor.fetchall()
print(results)
mycursor.execute("insert into users (user_id,email,password) values (2,002@bu.edu,123)")