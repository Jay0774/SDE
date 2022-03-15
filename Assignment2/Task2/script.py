# importing the library pymonetdb
import pymonetdb

# setting up connection, arguments below are the defaults
connection = pymonetdb.connect(username="monetdb", password="monetdb", hostname="localhost", database="demo")

# create a cursor object to run queries.
cursor = connection.cursor()

# creating a function that returns the status of values of accession numbers present in LibraryDB schema and REaders schema 
def status():
	print("Connecting to MonetDB...")
	print("--------------------------------------------------------------")
	# getting the values of Accession numbers present in LibraryDB
	cursor.execute("SELECT Accession_No FROM LibraryDB.ISBN")
	l = cursor.fetchall()
	# getting the values of Accession numbers present in Readers
	cursor.execute("SELECT AccessionNo FROM Readers.Reader_Id")
	l1 = cursor.fetchall()
	# stroing the values of accessio numbers in x1 and x2 
	x1 = []
	x2 = []
	# flag is used to cheack whether the values of accession numbers present in Readers are same as LibraryDB.
	flag = 0
	for i in range(len(l)):
		x1.append(l[i][0])
	for i in range(len(l1)):
		x2.append(l1[i][0])
		if l1[i][0] in x1:
			flag += 1
	print("Accession No. Present in Library are:\n")
	print(x1)
	print('\n')
	print("Accession No. Present in Readers are:\n")
	print(x2)
	print("--------------------------------------------------------------")
	# returning the values of flag, x1, and x2. 
	return flag,x1,x2

# defining the function that produces the records present in Readers schema
def data():
	print("Records Present in the Readers Table are:\n")
	cursor.execute("select Reader_id.readerid,reader_id.accessionno,Issue_date.issuedate,return_date.returndate from Readers.Return_Date,Readers.Reader_Id,Readers.Issue_date where Return_date.accessionno=reader_iD.Accessionno and Issue_date.accessionno = return_date.accessionno ;")
	l = cursor.fetchall()
	for i in range(len(l)):
		print("Record Number:",i+1,'\n')
		print("Reader Id 		:",l[i][0])
		print("Accession No. 		:",l[i][1])
		print("Issue Date 		:",l[i][2])
		print("Return Date 		:",l[i][3])
		print("--------------------------------------------------------------\n")

# defining the function to insert a new record into readers database.
def insert():
	t = input("Do you want to insert records in the table.... y/n\n")
	while t == 'y':
		print("--------------------------------------------------------------")
		print("Enter Record Details")	
		# taking record details
		rid = input("Enter Readers Id:\n")
		idate = input("Enter Issue Date:\n")
		rdate = input("Enter Return Date:\n")
		a = input("Enter Accession No.\n")
		# checking if accession number is already present in readers or not
		if a in x2:
			print("Accession No. already exists in Readers table try again...")
		# checking if accession number is present in books or not for referential integrity
		elif a in x1:
			# if present inserting data into readers
			print("Inserting Record in the Readers table.")
			q = "insert into Readers.Reader_Id values("+a+","+rid+")"
			cursor.execute(q)
			q = "insert into Readers.Issue_date values("+a+",'"+idate+"')"
			cursor.execute(q)
			q = "insert into Readers.Return_Date values("+a+",'"+rdate+"')"
			cursor.execute(q)
			connection.commit()
		else:
			print("Accession No. not in books Referential Integrity Not Maintained try again...")
		t = input("Do you want to insert more records...y/n\n")

	print("After inserting the records the status of database is:-")
	data()

flag ,x1 , x2 = status()
# if flag is same as all the records present in Readers then referential integrity is maintained
# since all Accession numbers of readers are also present in LibraryDB 
if flag == len(x2):
	print("Both Contains Same Accession Numbers Referential Integrity Maintained")
	print("Thanks")
	print("--------------------------------------------------------------")
	data()

# otherwise we need to maintain the referential integrity by deleting other records. 
# records need to be deleted from Reader_Id, Issue_Date, and Return_Date
else:
	print("Deleting the Record that are neglecting Referential Integrity\n")
	for i in range(len(x2)):
		if x2[i] not in x1:
			print("Deleting record with Accession No.:",x2[i])
			q = "delete from Readers.Reader_Id where accessionno ="+x2[i]
			cursor.execute(q)
			q = "delete from Readers.Issue_date where accessionno ="+x2[i]
			cursor.execute(q)
			q = "delete from Readers.Return_date where accessionno ="+x2[i]
			cursor.execute(q)
	# commitig the changes to monetdb.
	connection.commit()
	print("--------------------------------------------------------------")
	# again checking for referntial integrity in monetdb.
	print("After Deletion..")
	flag ,x1 , x2 = status()
	if flag == len(x2):
		print("Both Contains Same Accession Numbers Referential Integrity Maintained")
		print("Thanks")
		print("--------------------------------------------------------------")
		data()
# calling the insert function
insert()
	



