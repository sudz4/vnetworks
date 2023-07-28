from flask import Flask
app = Flask(__name__) # crea's the an instance of the Flask class

@app.route("/") # maps the url route to the following function
def index():
    return "You don't know me son!"