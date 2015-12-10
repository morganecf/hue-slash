'''
Useful heroku stuff: https://devcenter.heroku.com/articles/getting-started-with-python-o
'''


import os
from flask import Flask, render_template, request

app = Flask(__name__)

lights = ['s', 'm', 'd', 't', 's']
colors = ['red', 'blue', 'yellow', 'green']

all_lights = ', '.join(lights)
all_colors = ', '.join(colors)

@app.route('/')
def hello():
    data = open("data.csv").read().splitlines()
    return render_template('commands.html', {commands: data})

@app.route('/slash', methods=['POST'])
def slash():
	commands = request.form['text'].strip().lower().split()
	print commands 

	if len(commands) < 2:
		return 'Usage: /hue [light-name] [color]'
	else:
		light = commands[0]
		color = commands[1]

		print light, color

		if light == 'all':
			light = all_lights
		elif light not in lights:
			return 'light does not exist'
		if color == 'all':
			color = all_colors
		elif color not in colors:
			return 'color does not exist'

		cmd = 'Flashing ' + color + ' to ' + light

		fp = open('data.csv', 'a')
		fp.write(cmd + '\n')
		fp.close()

		return cmd
