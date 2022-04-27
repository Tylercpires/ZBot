from discord.ext import commands
from utils import config
from utils.timeutils import currentdatetime

class Add_Remove_Member(commands.Cog):
	'''Contains all actions the bot takes when a member joins or leaves the server.'''

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		'''Adds member to "Member" role when they join the server.'''
		print(f'{currentdatetime()}{member.name} just joined the server!')
		await self.bot.get_channel(config.welcomechannelid).send(f"{member.name} just joined the server!")
		await member.add_roles(self.bot.get_guild(config.serverid).get_role(config.memberid))
		print(f'{currentdatetime()}{member.name} was added to the "Member" role.')

def setup(bot):
	bot.add_cog(Add_Remove_Member(bot))