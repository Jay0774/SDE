# importing required libraries
import sqlalchemy
import pymysql

# ceating the engine object root is the user and password 34.122.45.49 is public ip of mysql instance NLP is database
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@34.122.45.49/NLP')
print(engine)
'''
# executing command
engine.execute("drop table analysis;")

engine.execute("CREATE TABLE if not exists analysis ("
               "text MEDIUMTEXT,"
               "score decimal,"
               "magnitude decimal);")

print(engine.execute("describe analysis;").fetchall())
'''
# printing the tables present
r = engine.execute("show tables;").fetchall()
print(r)

# creating a demo function to see data present in database
def show_data(): 
    # first we setup our query
    r = engine.execute("select * from analysis;").fetchall()
    t = ""
    s = 0
    m = 0

    for i in r:
        t = i[0]
        s = i[i]
        m = i[2]

show_data()

