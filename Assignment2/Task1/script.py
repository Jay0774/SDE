# Adding the Required Libraries
import json
import mysql.connector
import os

# defing the function to print the information of complete document
def print_info(x):
    print("ID                       : ",x[0])
    print("ISBN                     : ",x[1])
    print("Accession No.            : ",x[2])
    print("Title                    : ",x[3])
    print("Author                   : ",x[4])
    print("Publisher                : ",x[5])
    print("Edition                  : ",x[6])
    print("Year of Publication      : ",x[7])
    print("Category                 : ",x[8])   
    print("Total Number of Pages    : ",x[9])
    print("Price                    : ",x[10])
    print('\n')

# defining the function to print the complete details of mysql records.
def print_record(x):
    print("ISBN                     : ",x[0])
    print("Accession No.            : ",x[1])
    print("Title                    : ",x[2])
    print("Author                   : ",x[3])
    print("Publisher                : ",x[4])
    print("Edition                  : ",x[5])
    print("Year of Publication      : ",x[6])
    print("Category                 : ",x[7])   
    print("Total Number of Pages    : ",x[8])
    print("Price                    : ",x[9])
    print('\n')

id1 = []
id2 = []
# getting the json file by running the below command (using the local mongodb server)
os.system('mongoexport --uri="mongodb://localhost:27017/LibraryDB"  --collection=Books  --out=data.json')
f = open("data.json",'r')
s = f.readlines()
m = []
for i in s:
    l = []
    d = json.loads(i)
    x=list(d.keys())
    l.append(d['_id']['$oid'])
    id1.append(d['_id']['$oid'])
    if 'ISBN' in x:
        l.append(d['ISBN'])
    else: 
        l.append("")
    if 'Accession No.' in x:    
        l.append(d['Accession No.'])
    else:
        l.append("")
    if 'Title' in x:
        l.append(d['Title'])
    else:
        l.append("")
    if 'Author' in x:
        l.append(d['Author'].split(','))
    else:
        l.append("")
    if 'Publisher' in  x:
        l.append(d['Publisher'])
    else:
        l.append("")
    if 'Edition' in x:    
        l.append(d['Edition'])
    else:
        l.append("")
    if 'Year of Publication' in x:
        l.append(d['Year of Publication'])
    else:
        l.append("")
    if 'Category' in x:
        l.append(d['Category'].split(','))
    else:
        l.append("")
    if 'Total Number of Pages' in x:
        l.append(d['Total Number of Pages'])
    else:
        l.append("")
    if 'Price' in x:
        l.append(d['Price'])
    else:
        l.append("")
    m.append(l)
print("************************************************************************************")
# printing the number of documents in Books collection
print("Number of records present in MongoDB:",len(s),'\n')

# connecting to the Local mysql server. 
mysql_db = mysql.connector.connect(
  host="localhost",
  username="root",
  password="root"
)
cursor = mysql_db.cursor()
# changing the databse to LibraryDB
cursor.execute("use LibraryDB;")
# getting the currently present ids in table 
cursor.execute("select ID from books;")
result = cursor.fetchall()
for i in range(len(result)):
    id2.append(result[i][0])
print("Number of records present in Mysql:",len(id2),'\n')
print("*************************************************************************************")
# if both id's are same the data is same no changes
if id1==id2:
    print("Both contain same number of records\n")
# otherwise data should be entered or deleted. 
else:
    if len(id1)>len(id2):
        print("Records need to be entered in Mysql\n")
        for i in range(len(m)):
            l = m[i]
            if l[0] in id2:
                continue;
            print("Entering the record:\n")
            print_info(l)
            query = """INSERT INTO books (ID,ISBN,Accession,Title,Publisher,Edition,Year,Total,Price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record = (l[0],l[1],l[2],l[3],l[5],l[6],l[7],l[9],l[10])
            cursor.execute(query,record)
            for j in range(len(l[4])):
                q = """INSERT INTO bookauthor (ID,Author_name) VALUES (%s,%s)""" 
                cursor.execute(q,(l[0],l[4][j]))
            for j in range(len(l[8])):
                q = """INSERT INTO category (ID,Category) VALUES (%s,%s)""" 
                cursor.execute(q,(l[0],l[8][j]))    
            mysql_db.commit()
            print(cursor.rowcount,"Record Inserted sucessfully.")
            print("*************************************************************************************")
    elif len(id1)<len(id2):
        print("Records need to be deleted from Mysql\n")
        for i in range(len(id2)):
            l = id2[i]
            if l in id1:
                continue;
            print("Deleting the Record having ID as : ",l,'\n')
            query = "delete from books where ID = %s"
            record = (l,)
            cursor.execute(query,record)
            mysql_db.commit()
            print(cursor.rowcount,"Record Deleted sucessfully.")
            print("*************************************************************************************")   

x = input("Do you want the complete status of all records....y/n\n")
# getting the status of the records inserted.    
if x=='y':
    print("Status of Mysql database (only complete records are shown):\n")
    cursor.execute("select ISBN,Accession,Title,Author_name,Publisher,Edition,Year,Category,Total,Price from books,category,bookauthor where books.Id=bookauthor.ID and books.Id=category.ID;")
    result = cursor.fetchall()
    for i in range(len(result)):
        print_record(result[i])
    print("*************************************************************************************")
    print("Thank you..\n")
else:
    print("Thank you..\n")
