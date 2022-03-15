# Adding the Required Libraries
import json
import mysql.connector
import os

# getting the json file by running the below command (using the local mongodb server)
os.system('mongoexport --uri="mongodb://localhost:27017/LibraryDB"  --collection=Books  --out=data.json')
f = open("data.json",'r')
s = f.readlines()
print("*************************************************************************************")
# converting the json string to a dictionary
s = json.loads(s[0])
# getting the key of the dictionary
l = list(s.keys())
l[0] = "ID"
# creating the table query for mysql
q = "create table if not exists books("
q1 = "create table if not exists bookauthor( "+l[0]+" varchar(100)  , Author_name varchar(100) , foreign key ("+l[0]+") references books ("+l[0]+") on delete cascade);"
q2 = "create table if not exists category( "+l[0]+" varchar(100)  , Category varchar(100) , foreign key ("+l[0]+") references books ("+l[0]+") on delete cascade);"
for i in range(len(l)):
	if l[i] == "Author":
		continue 
	elif l[i] == "Category":
		continue
	else:
		q += l[i].split(" ")[0]
		q += " varchar(100) "
		if i == 0:
			q+= " Primary key , "
		elif i == len(l)-1:
			q+= " ); "
		else: 
		 	q+= " , "

# connecting to the Local mysql server. 
mysql_db = mysql.connector.connect(
  host="localhost",
  username="root",
  password="root"
)
cursor = mysql_db.cursor()
# creating and changing the databse to LibraryDB
cursor.execute("create database if not exists LibraryDB;")
cursor.execute("use LibraryDB;")
# executing the queries. 
cursor.execute(q)
result = cursor.fetchall()
print("Table created Sucessfully.")
print("*************************************************************************************")
cursor.execute(q1)
result = cursor.fetchall()
print("Table created Sucessfully.")
print("*************************************************************************************")
cursor.execute(q2)
result = cursor.fetchall()
print("Table created Sucessfully.")
print("*************************************************************************************")
# checking mysql database for updates
print("Checking the Mysql Database for updates...")
os.system('python script.py')