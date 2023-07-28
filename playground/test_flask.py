from flask import Flask
app = Flask(__name__) # creaet's the an instance of the Flask class

@app.route("/") # this sets the route to this page
def index():
    return "You don't know me son!"