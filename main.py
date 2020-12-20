from flask import Flask

import string
import random


app = Flask(__name__)


def generate_password():
    choices = string.ascii_letters
    password = ''

    for i in range(10):
        password += random.choice(choices)

    return password


@app.route('/')
def hello_world():
    return generate_password()


@app.route('/exp/')
def exp():
    return 'exp'


if __name__ == '__main__':
    app.run()
