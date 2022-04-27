from discord.ext import commands
import os
from utils import config
from utils.timeutils import currentdatetime

class Bot(commands.Bot):

	print(f"{currentdatetime()}Attempting to start Zenith Bot...")

	def __init__(self):
		super().__init__(
			command_prefix = config.prefix, #Sets the bot's command prefix
			intents = config.intents #Gives the bot permission to perform certain actions
		)

		for file in os.listdir("./cogs"): #Loops through "cogs" folder
			if file.endswith(".py"):
				self.load_extension(f"cogs.{file[:-3]}") #Loads any files that end with .py
				print(f"{currentdatetime()}Loaded {file}.")