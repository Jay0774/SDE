# MongoDB and Mysql
## To create the MongoDB database locally and Migrating to Mysql.
### 1. Install MongoDB and MySQL for windows Locally.
### 2. Create Database LibraryDB in MongoDB with Collection Books.
### 3. Insert Document into the  Books Collection using the commands.

->  use LibraryDB;

->  db.Books.insert({"ISBN" : "9780619216351","Accession No." : "040620180010","Title" : "Java programming : from problem analysis to program design","Author" : "D. S. Malik","Publisher" : "Boston : Course Technology/Thomson Learning","Edition" : 1,"Year of Publication" : 2003, "Category" : "java","Total Number of Pages" : 998,"Price" : 4897.53})

->  db.Books.insert({"ISBN" : "059600088X","Accession No." : "230820211652","Title" : "Java programming with Oracle JDBC","Author" : "Donald Bales","Publisher" : "Sebastopol, CA : O'Reilly","Edition" : 1,"Year of Publication" : 2002, "Category" : "java","Total Number of Pages" : 506,"Price" : 925})

->  db.Books.insert({"ISBN" : "9780538453028","Accession No." : "210320160010","Title" : "C# Programming ( Barbara Doyle)","Author" : "Barbara Doyle","Publisher" : "Course Techonology","Edition" : 3,"Year of Publication" : 2011, "Category" : "C","Total Number of Pages" : 1092,"Price" : 44413})

->  db.Books.insert({"ISBN" : "9780136631705","Accession No." : "170220210045","Title" : "Advanced C programming","Author" : " Oualline,Steve","Publisher" : "New York : Brady Pub.","Edition" : 2,"Year of Publication" : 1992, "Category" : "C","Total Number of Pages" : 442,"Price" : 5726})

->  db.Books.insert({"ISBN" : "9780321356567","Accession No." : "191220190102","Title" : "C++ programming","Author" : "  Ullman,Larry E.(Larry Edward)","Publisher" : "Berkeley, Calif. : Peachpit Press","Edition" : 1,"Year of Publication" : 2006, "Category" : "C","Total Number of Pages" : 532,"Price" : 600})

->  db.Books.insert({"ISBN" : "9781887902991","Accession No." : "310120120523","Title" : "Python programming","Author" : "John M. Zelle","Publisher" : "Franklin, Beedle","Edition" : 1,"Year of Publication" : 2004, "Category" : "python","Total Number of Pages" : 532,"Price" : 900})

->  db.Books.insert({"ISBN" : "9781435455009","Accession No." : "030120220023","Title" : "Python programming for the absolute beginner","Author" : "Dawson,Mike","Publisher" : "Boston, MA : Course Technology Cengage Learning","Edition" : 3,"Year of Publication" : 2010, "Category" : "python","Total Number of Pages" : 484,"Price" : 1000})

->  db.Books.insert({"ISBN" : "9781617292453","Accession No." : "010120220022","Title" : "Hello Raspberry Pi! : Python programming for kids and other beginners","Author" : "Heitz,Ryan","Publisher" : "Shelter Island, NY : Manning Publications Co.","Edition" : 1,"Year of Publication" : 2016, "Category" : "python","Total Number of Pages" : 322,"Price" : 400})

->  db.Books.insert({"ISBN" : "9780314933096","Accession No." : "260820102014","Title" : "Introduction to data structures and algorithm analysis","Author" : "Naps,Thomas L,Singh,Bhagat","Publisher" : " St. Paul, MN : West Pub. Co.","Edition" : 2,"Year of Publication" : 1992, "Category" : "python,c","Total Number of Pages" : 714,"Price" : 800})

->  db.Books.insert({"ISBN" : "9780911537048","Accession No." : "270520100056","Title" : "Reliable data structures in C","Author" : "Plum,Thomas","Publisher" : "Cardiff, N.J. : Plum Hall","Edition" : 1,"Year of Publication" : 1985, "Category" : "c","Total Number of Pages" : 276,"Price" : 250})

### 4. Now use script_db.py to create the database in MySQL Migrate the data to MySQL.
### 5. For entering new record use insert.py script.
### 6. For Manually inserting data into MongoDB use Script.py after inserting data into MongoDB. 
