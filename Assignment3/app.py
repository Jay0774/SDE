from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('')
def hello():
   return "hello how are you",request.url

if __name__ == '__main__':
   app.run(debug=True)