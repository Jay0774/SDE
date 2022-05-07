# importing required libraries
from flask import Flask,render_template, request
import os
from google.cloud import language_v1
import mysql.connector
from mysql.connector.constants import ClientFlag
import sqlalchemy
import pymysql

# connecting to mysql engine root is the user name and password 34.122.45.49 is public ip of mysql instance NLP is the database name
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@34.122.45.49/NLP')
print(engine)
# creating table if not exist
engine.execute("CREATE TABLE if not exists analysis ("
               "text MEDIUMTEXT,"
               "score decimal,"
               "magnitude decimal);")
print(engine)
# showing the tables
r = engine.execute("show tables;").fetchall()
print(r)

# setting up the environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "sde-a3-ed0f1cb3a84e.json"

# Instantiating a client
client = language_v1.LanguageServiceClient()

app = Flask(__name__)

# route home page of api
@app.route('/')
def no_api():
    print("Conducting new analysis")
    return render_template('api.html')

# route of taking data from user
@app.route('/data')
def form():
    return render_template('data.html')

# route for showing all data present in mysql
@app.route('/show')
def show_data(): 
    print("showing data of present records. ")
    # first we setup our query
    r = engine.execute("select * from analysis;").fetchall()
    t = ""
    s = 0
    m = 0
    f = open('templates/show.html', 'w')
    html_template = """
    <html>
    <head>
        <title>API Page</title>
    </head>
    <style>
        body {
            font-family: Tahoma, Verdana, Arial, sans-serif;
        }
        th, td {
            padding: 5px;
            border: 1px solid;
            text-align: left;
        }
        table{
            border: 1px solid;
            width: 100%;
        }
        
    </style>
    <body>
    <h1><center>AI Based API</center></h1>
    <h3><center>OUTPUT FOR PREVIOUS TEXTS</center></h3>
    <align="left">
    <br>"""
    for i in range(len(r)):
        t = r[i][0]
        s = r[i][1]
        m = r[i][2]
        html_template += """
        <table>
        <tr>
        <td><b>Record Number:</b></td>
        <td>"""+str(i+1)+"""</td>
        </tr>
        <tr>
        <td><b>Text</b></td>
        <td>"""+t+"""</td>
        </tr>
        <tr>
        <td><b>Score of Sentiment analysis:</b></td>
        <td>"""+str(s)+"""%</td>
        </tr>
        <tr>
        <td><b>Magnitude of SentimentAnanysis:<b></td>
        <td>"""+str(m)+"""%</td>
        </tr>
        </table><br><br>"""
    html_template+="""</body>
    </html>

    """
    f.write(html_template)
    f.close()
    return render_template('show.html')

# route for doing the analysis on user provided data
@app.route('/output',methods = ['GET', 'POST'])
def output():
    print("New Analysis")
    # getting user entered data 
    if request.method == 'POST':
        t = request.form['Name']
    text = ""
    for i in range(len(t)):
        if (t[i] >= 'a' and t[i] <= 'z') or (t[i] >= 'A' and t[i] <='Z') or t[i] == ' ':
            text+=t[i]
    # Instantiates a client
    client = language_v1.LanguageServiceClient()
    s1 = ""
    s2 = ""
    s3 = ""
    s = 0
    m = 0
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT , language = "en"
    )
    # Detect the sentiment
    response = client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    results1 = dict(
        Score=f"{sentiment.score:.1%}",
        Magnitude=f"{sentiment.magnitude:.1%}",
        )
    s = sentiment.score
    m = sentiment.magnitude
    for k, v in results1.items():
        s1 += f"{k:}: {v}"
        s1 += "<br>"
    # Detect the entities
    response = client.analyze_entities(document=document)
    i = 0
    for entity in response.entities:
        results2 = dict(
            Name=entity.name,
            Type=entity.type_.name,
            Salience=f"{entity.salience:.1%}",
            Wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            Mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results2.items():
            s2 += f"{k:15}: {v}"
            s2 += "<br>"
        if i != len(response.entities) - 1:
            s2+= "-" * 150 
            s2 += "<br>"
        i = i + 1
    # Detect the Classification
    i = 0
    response = client.classify_text(document=document)
    for category in response.categories:
        s3 += "<br>"
        s3 += f"Category  : {category.name}<br>"
        s3 += f"Confidence: {category.confidence:.0%}<br>" 
        if i != len(response.categories) - 1:
            s3+= "-" * 150 
            s3 += "<br>"
        i = i + 1
    print("Done with analysis")
    # writing data into output file  
    f = open('templates/output.html', 'w')
    html_template = """
    <html>
    <head>
        <title>API Page</title>
    </head>
    <style>
        body {
            font-family: Tahoma, Verdana, Arial, sans-serif;
        }
        th, td {
            padding: 5px;
            border: 1px solid;
            text-align: left;
        }
        table{
            border: 1px solid;
            width: 100%;
        }
        
    </style>
    <body>
    <h1><center>AI Based API</center></h1>
    <h3><center>OUTPUT FOR GIVEN TEXT</center></h3>
    <align="left">
    <br>
    <table>
    <tr>
    <td><b>Text</b></td>
    <td>"""+text+"""</td>
    </tr>
    <tr>
    <td><b>Sentiment analysis:</b></td>
    <td>"""+s1+"""</td>
    </tr>
    <tr>
    <td><b>Classification Ananysis:<b></td>
    <td>"""+s3+"""</td>
    </tr>
    <tr>
    <td><b>Entity Ananysis:<b></td>
    <td>"""+s2+"""</td>
    </tr>
    </table>
    </body>
    </html>

    """
    f.write(html_template)
    f.close()
    # print(t,s,m)
    # first we setup our query
    query = ('INSERT INTO analysis (text, score , magnitude) VALUES ("'+text+'",'+str(s)+','+str(m)+');')
    engine.execute(query)
    r = engine.execute("select * from analysis;").fetchall()
    print(r)
    return render_template('output.html')

if __name__ == '__main__':
   app.run(debug=True)
