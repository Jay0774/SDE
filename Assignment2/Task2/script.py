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
	flag ,x1 , x2 = status()
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

# defining the function that produces the records present in library schema only for isbn and accesion no.
def data_library():
	flag ,x1 , x2 = status()
	print("Records Present in the ISBN Table are:\n")
	cursor.execute("select isbn,accession_no from LibraryDB.ISBN;")
	l = cursor.fetchall()
	for i in range(len(l)):
		print("Record Number:",i+1,'\n')
		print("ISBN			:",l[i][0])
		print("Accession No. 		:",l[i][1])
		print("--------------------------------------------------------------\n")

# defining the function to insert a new record into readers database.
def insert_readers():
	flag ,x1 , x2 = status()
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

# defining the function to insert a new record into Library database.
def insert_library():
	flag ,x1 , x2 = status()
	t = input("Do you want to insert records in the table.... y/n\n")
	while t == 'y':
		print("--------------------------------------------------------------")
		print("Enter Record Details")	
		# taking record details
		isbn = input("Enter ISBN:\n")
		a = input("Enter Accession No.:\n")
		author = input("Enter Author:\n")
		publisher = input("Enter Publisher:\n")
		edition = input("Enter Edition:\n")
		title = input("Enter Title:\n")
		page = input("Enter NO. of Pages:\n")
		year = input("Enter Year of Publication\n")
		price = input("Enter Price:\n")
		category = input("Enter Category:\n")
		# if not present inserting data into table
		if a not in x1:
			print("Inserting Record in the Library database.")
			q = "insert into LibraryDB.ISBN values('"+isbn+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Author values('"+author+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Publication values('"+publisher+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Title values('"+title+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Edition values('"+edition+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Pages values('"+page+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Price values('"+price+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Year_of_publication values('"+year+"',"+a+")"
			cursor.execute(q)
			q = "insert into LibraryDB.Category values('"+category+"',"+a+")"
			cursor.execute(q)
			connection.commit()
		else:
			print("Record Already exists with same Acession No.")
		t = input("Do you want to insert more records...y/n\n")
	print("After inserting the records the status of database is:-")
	data_library()

# def the function for Updating the records of library tables
def update_library(): 
	flag ,x1 , x2 = status()
	t = input("Do you want to update records in the table.... y/n\n")
	while t == 'y':
		print("--------------------------------------------------------------")
		print("Enter Record Details")	
		# taking record details
		a = input("Enter Accession No.\n")
		# checking if accession number is already present or not in library or not
		if a  not in x1:
			print("Accession No. not exists in LibraryDB try again...")
		# checking if accession number is present in readers or not for referential integrity
		elif a in x2:
			print("Accession No. exists in Readers Need to update it also.")
			update_readers()
			print("--------------------------------------------------------------")
			print("Enter Record Details")	
			# taking record details
			isbn = input("Enter Updated ISBN:\n")
			author = input("Enter Updated Author:\n")
			publisher = input("Enter Updated Publisher:\n")
			edition = input("Enter Updated Edition:\n")
			title = input("Enter Updated Title:\n")
			page = input("Enter Updated NO. of Pages:\n")
			year = input("Enter Updated Year of Publication\n")
			price = input("Enter Updated Price:\n")
			category = input("Enter Updated Category:\n")
			# inserting updated data into readers
			print("Inserting Updated Record in the Library database.")
			q = "update LibraryDB.ISBN set isbn = '"+isbn+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Author set author = '"+author+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Publication set Publication = '"+publisher+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Title set title = '"+title+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Edition set edition = '"+edition+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Pages set pages = '"+page+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Price set price = '"+price+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Year_of_publication set year_p = '"+year+"' where accession_no = "+a
			cursor.execute(q)
			q = "update LibraryDB.Category set category = '"+category+" 'where accession_no = "+a
			cursor.execute(q)
			connection.commit()
		t = input("Do you want to update more records...y/n\n")
	print("After Updating the records the status of database is:-")
	data_library()

# def the function for Updating the records of readers database
def update_readers(): 
	flag ,x1 , x2 = status()
	t = input("Do you want to update records in the table.... y/n\n")
	while t == 'y':
		print("--------------------------------------------------------------")
		print("Enter Record Details")	
		# taking record details
		a = input("Enter Accession No.\n")
		# checking if accession number is present in readers or not
		if a not in x2:
			print("Accession No. not exists in Readers try again...")
		# checking if accession number is present in library or not for referential integrity
		elif a not in x1:
			print("Accession No. not exists in LibraryDB Database also try again...")
		else:
			# if present inserting updated data into readers
			print("Inserting Updated Record in the readers table.")
			# taking record details
			rid = input("Enter Updated Readers Id:\n")
			idate = input("Enter Updated Issue Date:\n")
			rdate = input("Enter Updated Return Date:\n")
			q = "update Readers.Reader_Id set readerid = "+rid+" where accessionno = "+a+";"
			cursor.execute(q)
			q = "update Readers.Issue_date set issuedate = '"+idate+"' where accessionno = "+a+";"
			cursor.execute(q)
			q = "update Readers.Return_Date set returndate = '"+rdate+"' where accessionno = "+a+";"
			cursor.execute(q)
			connection.commit()
		t = input("Do you want to update more records...y/n\n")
	print("After Updating the records the status of database is:-")
	data()

# defining the function for deleting the data from readers
def delete(a):
	flag ,x1 , x2 = status()
	if a in x2:
		print("Deleted record with Accession No.:",a)
		q = "delete from Readers.Reader_Id where accessionno ="+a
		cursor.execute(q)
		q = "delete from Readers.Issue_date where accessionno ="+a
		cursor.execute(q)
		q = "delete from Readers.Return_date where accessionno ="+a
		cursor.execute(q)
		# commitig the changes to monetdb.
		connection.commit()
	else:
		print("Record with Accession no. ",a," Not found.\n")
	print("Status of Database after deleting accesion no.",a,'\n')
	data()

# defining the function for deleting the data from library
def delete_Library():
	flag ,x1 , x2 = status()
	t = input("Do you want to delete records in the table.... y/n\n")
	while t == 'y':
		print("--------------------------------------------------------------")
		print("Enter Record Details")	
		# taking record details
		a = input("Enter Accession No.\n")
		# checking if accession number is already present in readers or not
		if a in x2:
			m = input("Accession No. exists in Readers table cannot delete from LibraryDB do you want to delete it from Readers...y/n\n")
			if m == 'y':
				# defleting from readers to maintain referential integrity
				delete(a)
				# deleting data from library
				print("Deleted Record in the Library database table.")
				q = "delete from LibraryDB.ISBN where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Author where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Publication where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Edition where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Price where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Pages where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Title where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Category where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.Year_of_publication where accession_no = "+a+";"
				cursor.execute(q)
				q = "delete from LibraryDB.ISBN where accession_no = "+a+";"
				cursor.execute(q)
				connection.commit()
			else: 
				print("Not deleting the record")
		# checking if accession number is present in books or not for referential integrity
		elif a not in x1:
			print("Accession No. not exists in LibraryDB try again...")
		else:
			print("Deleting Record in the Library database table.")
			q = "delete from LibraryDB.ISBN where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Author where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Publication where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Edition where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Price where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Pages where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Title where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Category where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.Year_of_publication where accession_no = "+a+";"
			cursor.execute(q)
			q = "delete from LibraryDB.ISBN where accession_no = "+a+";"
			cursor.execute(q)
			connection.commit()
		t = input("Do you want to delete more records...y/n\n")
	print("After deleting the records the status of database is:-")
	data_library()


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

# calling the insert and other defined functions function
choice = 'y'
while choice == 'y':
	print("Various Operations:")
	print("1. Insert into LibraryDB")
	print("2. Insert into Readers")
	print("3. Update LibraryDB")
	print("4. Update Readers")
	print("5. Delete from LibraryDB")
	print("6. Delete from Readers")
	n = int(input("Enter 1/2/3/4/5/6:\n"))
	if n == 1:
		insert_library()
	elif n == 2:
		insert_readers()
	elif n == 3:
		update_library()
	elif n == 4:
		update_readers()
	elif n == 5:
		delete_Library()
	elif n == 6:
		print("Deleting the Record in Readers Database:")
		a = input("Enter Accession No. for Deletion:\n")
		delete(a)
	else:
		print("Wrong choice..\n")
	choice = input("Do you want to go again..y/n\n")
	



