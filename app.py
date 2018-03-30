#Entry point root file
from flask import Flask

from mongoengine import *
connect('todoflaskdb')

app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Welcome to Wils TODO  !'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
