from flask import Flask, render_template

#Create a Flack Instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
    return "<h1>Hello World number 3!</h1>"

#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

