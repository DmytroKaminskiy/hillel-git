from flask import Flask, request

from utils import encrypt_message

import string
import random

app = Flask(__name__)


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters
    password = ''

    for i in range(length):
        password += random.choice(choices)

    return password


@app.route('/')
def hello_world():
    """
    ?name=Dima&age=28
    """
    length = int(request.args.get('length') or 10)
    name = request.args.get('name', 'DEFAULT')
    age = request.args.get('age', 'DEFAULT_AGE')
    return f'{name} {age}, here is your password {generate_password(length)}'


@app.route('/exp/')
def exp():
    return 'exp'


@app.route('/encrypt-message/')
def encrypt_message_router():
    message = request.args['message']
    return encrypt_message(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
