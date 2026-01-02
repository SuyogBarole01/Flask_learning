from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to flask app'

@app.route('/home')
def home():
    return 'Home page in Flask'

from controller import product_controller, user_controller