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