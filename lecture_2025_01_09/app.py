from flask import Flask, request
from login import login

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def authenticate():
    username = request.args.get('username')
    password = request.args.get('password')
    if login(username, password):
        return 'You are authenticated!'
    return 'Invalid credentials'