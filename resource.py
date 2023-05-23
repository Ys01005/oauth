from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the Baskota website!'


@app.route('/protected-resource')
def protected_resource():
    access_token = request.headers.get('Authorization')

    if validate_token(access_token):
        return 'Protected Resource: This is a protected resource.'
    else:
        return 'Unauthorized: Access token expired or invalid. Please log in again.'


def validate_token(token):
    return True


if __name__ == '__main__':
    app.run(port=5003)
