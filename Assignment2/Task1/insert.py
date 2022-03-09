# importing pymongo for inserting into mongodb
import pymongo
import os
# providing the details of the client the database and the collecion.
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["LibraryDB"]
collection = db["Books"]
print("*************************************************************************************")   

# inserting the document using the insert command.
# getting the document details from user
doc = {	"ISBN" : "",
		"Accession No.":"",
		"Title":"",
		"Author":"",
		"Publisher":"",
		"Edition":"",
		"Year of Publication":"",
		"Category":"",
		"Total Number of Pages":"",
		"Price": ""}
print("Enter Document Details:\n")
doc["ISBN"]=(input("ISBN:\n"))
doc["Accession No."]=(input("Accession No.:\n"))
doc["Title"]=(input("Title:\n"))
doc["Author"]=(input("Author:\n"))
doc["Publisher"]=(input("Publisher:\n"))
doc["Edition"]=(int(input("Edition:\n")))
doc["Year of Publication"]=(int(input("Year of Publication:\n")))
doc["Category"]=(input("Category:\n"))
doc["Total Number of Pages"]=(int(input("Total Numner of Pages:\n")))
doc["Price"]=(float(input("Price:\n")))

# inserting the document details into mongodb
d = collection.insert_one(doc)
print(d.inserted_id , "Inserted Document Sucessfully")
print("*************************************************************************************")  
# checking mysql database for updates
print("Checking the Mysql Database for updates...")
os.system('python script.py')



