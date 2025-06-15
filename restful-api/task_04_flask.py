#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users storage (in memory only)
users = {}

# 1. Home page
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# 2. Get all usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# 3. Server status
@app.route('/status')
def status():
    return "OK"

# 4. Get user data by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# 5. Add new user (POST)
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if username is provided
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Store the new user
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run()
