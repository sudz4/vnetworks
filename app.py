from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import requests    # pip install requests  

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# For the purposes of this example, we'll use a dictionary to represent a "database" of users.
users = {"sudz4": {"password": "pword4"}, "jimmy4": {"password": "pword4"}}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    if request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('welcome'))

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)
