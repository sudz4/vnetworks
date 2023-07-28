from flask import Flask
test_flask = Flask(__name__)

@test_flask.route("/") 
def index():
    return "You don't know me son!"

# this actually runs the app
if __name__ == "__main__":
    test_flask.run(debug=True)
    # test_flask.run(debug=True, port=5001) # can try other ports if other processes are running on 5000
