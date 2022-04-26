from discord.ext import commands
import os

class Cog_Handling(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def load(self, ctx, extension):
		'''- Loads/updates a single cog.'''
		if ctx.author.top_role.id == int(os.environ.get("DEVID")):
			print(f"{ctx.author} ({ctx.author.id}) successfully called .load on {extension}.py")
			try: #Attempt to reload any given cog
				self.bot.unload_extension(f"cogs.{extension}")
				self.bot.load_extension(f"cogs.{extension}")
				print(f"{extension}.py successfully updated.")
				return await ctx.send(f"{extension}.py successfully updated.")
			except: #Attemps to load cog for the first time if it hasn't already been loaded
				print(f"{extension}.py has not been loaded before. Attemping first time load...")
				try: #Loads cog if it exists
					self.bot.load_extension(f"cogs.{extension}")
					print(f"{extension}.py successfully loaded.")
					return await ctx.send(f"{extension}.py successfully loaded.")
				except: #Lets user know it doesn't exist
					print(f"{extension}.py does not exist!")
					return await ctx.send(f"{extension}.py does not exist!")
		else: #Returns a warning if user doesn't have permission to load cogs
			print(f"WARNING! {ctx.author} ({ctx.author.id}) tried to call .load!")
			return await ctx.send("You\'re not a DEV!")

def setup(bot):
	bot.add_cog(Cog_Handling(bot))