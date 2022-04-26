#Simple file that starts a Flask web server, through the bot on startup

#Inspiration for file taken from B. Carnes - "Code a Discord Bot with Python - Host for Free in the Cloud" - 2022/04/08

from flask import Flask
from threading import Thread

server = Flask('')

@server.route('/')
def online_message():
	return 'ZBot is currently online.'

def run():
	server.run(host='0.0.0.0', port=8080)

def stay_online():
	thread = Thread(target=run)
	thread.start()