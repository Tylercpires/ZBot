from discord.ext import commands

class On_Ready(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		'''Displays confirmation on successful startup.'''
		print("Zenith Bot started successfully.")

def setup(bot):
	bot.add_cog(On_Ready(bot))