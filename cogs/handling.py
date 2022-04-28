from discord.ext import commands
from utils import config
from utils.timeutils import currentdatetime

class Handling(commands.Cog):
	'''Contains all commands that handle cogs (and utils).'''
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def load(self, ctx, extension):
		'''Loads/updates a single cog.'''
		if ctx.author.top_role.id == config.devid:
			print(f"{currentdatetime()}{ctx.author} ({ctx.author.id}) successfully called .load on {extension}.py")
			try: #Attempt to reload any given cog
				self.bot.unload_extension(f"cogs.{extension}")
				self.bot.load_extension(f"cogs.{extension}")
				print(f"{currentdatetime()}{extension}.py has been updated.")
				return await ctx.send(f"{extension}.py has been updated.")
			except: #Attemps to load cog for the first time if it hasn't already been loaded
				print(f"{currentdatetime()}{extension}.py has not been loaded before, or is currently disabled. Attemping to load...")
				try: #Loads cog if it exists
					self.bot.load_extension(f"cogs.{extension}")
					print(f"{currentdatetime()}{extension}.py has been loaded.")
					return await ctx.send(f"{extension}.py has been loaded.")
				except: #Lets user know it doesn't exist
					print(f"{currentdatetime()}{extension}.py does not exist!")
					return await ctx.send(f"{extension}.py does not exist!")
		else: #Returns a warning if user doesn't have permission to load cogs
			print(f"{currentdatetime()}WARNING! {ctx.author} ({ctx.author.id}) tried to call .load on {extension}.py!")
			return await ctx.send("You\'re not a DEV!")

	@commands.command()
	async def unload(self, ctx, extension):
		'''Unloads a single cog.'''
		if ctx.author.top_role.id == config.devid:
			print(f"{currentdatetime()}{ctx.author} ({ctx.author.id}) successfully called .unload on {extension}.py")
			try:
				self.bot.unload_extension(f"cogs.{extension}")
				print(f"{currentdatetime()}{extension}.py has been unloaded.")
				return await ctx.send(f"{extension}.py has been disabled.")
			except:
				print(f"{currentdatetime()}{extension}.py does not exist, or is currently disabled.")
				return await ctx.send(f"{extension}.py does not exist, or is currently disabled.")
		else:
			print(f"{currentdatetime()}WARNING! {ctx.author} ({ctx.author.id}) tried to call .unload on {extension}.py!")
			return await ctx.send("You\'re not a DEV!")

def setup(bot):
	bot.add_cog(Handling(bot))