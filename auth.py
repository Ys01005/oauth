from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
users = {
    'joe': 'pass',
    'user': 'pass',
    'user1': 'pass'
}
refresh_token = None
access_token = None

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    print(f"Received login request for username: {username}, password: {password}")

    if username in users and users[username] == password:
        generate_tokens()
        return jsonify({'message': 'Login successful', 'refresh_token': refresh_token, 'access_token': access_token}), 200
    else:
        return 'Invalid credentials.', 401

@app.route('/refresh-token', methods=['POST'])
def refresh_token_route():
    global refresh_token, access_token
    if refresh_token == request.json['refresh_token']:
        generate_tokens()
        return jsonify({'message': 'Token refreshed', 'access_token': access_token}), 200
    else:
        return 'Invalid refresh token.', 401

def generate_tokens():
    global refresh_token, access_token
    refresh_token = jwt.encode({'exp': datetime.utcnow() + timedelta(minutes=30)}, 'refresh_secret', algorithm='HS256')
    access_token = jwt.encode({'exp': datetime.utcnow() + timedelta(minutes=15)}, 'access_secret', algorithm='HS256')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
