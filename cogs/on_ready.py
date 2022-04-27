from discord.ext import commands
from utils.timeutils import currentdatetime

class On_Ready(commands.Cog):
	'''Contains all actions the bot takes on startup.'''
	
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		'''Displays confirmation on successful startup.'''
		print(f"{currentdatetime()}Zenith Bot started successfully.")

def setup(bot):
	bot.add_cog(On_Ready(bot))