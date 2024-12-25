# THIS IS LINUX BASED TERMINAL :D 
# REMEMBER: TOUcH ON HOW THIS RELATES TO KUBERNETES

# http protocols 
# ESSENCE IS: SERVE PYTHON TO THE WEB (through your backend)

import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)

def get_website_visitors():
    # some code for getting the number of visitors from our database
    # or calling an api ... or machine learning 
    # Ellinor -> some machine learning algorithm -> 
    return {'total': 301}

@app.route('/visitors', methods=['GET'])
def visitors():
    return jsonify(get_website_visitors())

@app.route('/' )
def home():
    print('hello world')
    return render_template('index.html')


