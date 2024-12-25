from flask import Flask, render_template, jsonify, request
from openai import OpenAI
from create_user import create_user

OPEN_AI_API_KEY = "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"

client = OpenAI(api_key=OPEN_AI_API_KEY)

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/api/image')
def image():
    response = client.images.generate(
        model="dall-e-3",
        prompt="Big blue marlin in the ocean!",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})


@app.route('/api/user/create', methods=['POST'])
def create_user_route():
    data = request.json
    name = data['name']
    email = data['email']
    create_user(name, email)
    return jsonify({'message': 'User created successfully!'})