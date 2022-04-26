#T. Pires - Zenith Server Discord Bot - 2022/04/08
#Last updated 2022/04/25

import os
from utils.web_server import stay_online
from utils.bot import Bot

def main():
	bot = Bot() #Creates instance of "Bot" class
	stay_online() #Starts the flask webserver - used to keep the bot online 24/7
	bot.run(os.environ.get("Token")) #Starts the bot, using env. variable "Token"

if __name__ == "__main__":
	main()