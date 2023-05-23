from flask import Flask, render_template, request
import requests

AUTH_SERVER_URL = 'http://localhost:5001'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders the index.html template

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = requests.post(f"{AUTH_SERVER_URL}/login", data={'username': username, 'password': password})
    print(response.status_code)  # Prints the status code of the response from the authentication server
    print(response.text)  # Prints the response text received from the authentication server
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return render_template('success.html', access_token=access_token)  # Renders the success.html template with the access token
    else:
        return render_template('failure.html', message='Invalid credentials.')  # Renders the failure.html template with an error message

@app.route('/refresh-token', methods=['POST'])
def refresh_token():
    refresh_token = request.form['refresh_token']
    response = requests.post(f"{AUTH_SERVER_URL}/refresh-token", data={'refresh_token': refresh_token})
    print(response.status_code)  # Prints the status code of the response from the authentication server
    print(response.text)  # Prints the response text received from the authentication server
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return render_template('success.html', access_token=access_token)  # Renders the success.html template with the new access token
    else:
        return render_template('failure.html', message='Token refresh failed.')  # Renders the failure.html template with an error message

@app.route('/protected-resource', methods=['POST'])
def protected_resource():
    access_token = request.form['access_token']
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('http://localhost:5002/protected', headers=headers)
    print(response.status_code)  # Prints the status code of the response from the protected resource server
    print(response.text)  # Prints the response text received from the protected resource server
    if response.status_code == 200:
        return response.text  # Returns the protected resource content
    else:
        return 'Failed to access protected resource.'  # Returns an error message

if __name__ == '__main__':
    app.run(port=5000)
