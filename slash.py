import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    #data = open("data.txt").read().splitlines()
    return 'list of commands sent'


@app.route('/slash')
def slash():
	return 'Hello'
