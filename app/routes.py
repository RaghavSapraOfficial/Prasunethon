from flask import render_template, request, jsonify
from app import app
from app.ml_model import get_response

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.json['user_input']
    response = get_response(user_input)
    return jsonify({'bot_response': response})
