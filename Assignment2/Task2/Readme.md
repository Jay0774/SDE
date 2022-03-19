# MonetDB Column store database
## 1. Download monetDB Run server and client.
## 2. create schema LibraryDB and Readers.
## 3. Create tables in both schemas using commands.

-> CREATE TABLE LibraryDB.ISBN( ISBN varchar(100),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Author( Author varchar(100),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Edition( Edition varchar(2),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Title( Title varchar(100),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Pages( Pages varchar(5),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Publication( Publication varchar(100),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Year( Year varchar(4),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Price( Price varchar(6),Accession_No varchar(12) Primary Key);

-> CREATE TABLE LibraryDB.Category( Category varchar(100),Accession_No varchar(12) Primary Key);
---------------------------------------------------------------------------------------------------------
-> CREATE TABLE Readers.Reader_Id( AccessionNo varchar(12), ReaderID int Primary Key);

-> CREATE TABLE Readers.Issue_Date( AccessionNo varchar(12), IssueDate varchar(10) );

-> CREATE TABLE Readers.Return_Date( AccessionNo varchar(12), ReturnDate varchar(10) );

## 4. Insert data into tables using commands.

-> insert into LibraryDB.ISBN values (9780911537048,270520100056);

-> insert into LibraryDB.ISBN values (9780314933096,260820102014);

-> insert into LibraryDB.ISBN values (9781617292453,100120220022);
----------------------------------------------------------------------------------------------------------
-> insert into Readers.Reader_Id values (270520100056,0001);

-> insert into Readers.Issue_date values (270520100056,'02/03/2021');

-> insert into Readers.Return_date values (270520100056,'21/03/2021');

-> insert into Readers.Reader_Id values (310120120523,0002);

-> insert into Readers.Issue_date values (310120120523,'03/03/2021');

-> insert into Readers.Return_date values (310120120523,'12/03/2021');

-> insert into Readers.Reader_Id values (260820102014,0003);

-> insert into Readers.Issue_date values (260820102014,'14/04/2021');

-> insert into Readers.Return_date values (260820102014,'16/04/2021');

## 5. Run script.py to check referential integrity and insert new record into Readers.
