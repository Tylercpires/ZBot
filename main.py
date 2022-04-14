#T. Pires - 2022/04/08

import discord
from discord.ext import commands
import os

intents = discord.Intents().all()
client = commands.Bot(command_prefix = '.', intents = intents)

#Commands

voiceclient = None

@client.command()
async def join(ctx):
	'''Makes the bot join the users current voice channel'''
	currentguild = client.get_guild(int(os.environ['ServerID'])) #Current server instance
	clientmember = currentguild.get_member(int(os.environ['ClientID'])) #Bot instance
	voiceclient = None #Initialization for bot's voiceclient; needed for cleanup()
	currentchannel = ctx.channel #Text channel the command was sent in
	if isinstance(ctx.author.voice, discord.VoiceState):
		voicechannel = ctx.author.voice.channel
		if clientmember.voice == None:
			voiceclient = await voicechannel.connect()
			voiceclient.cleanup()
		elif clientmember.voice.channel != voicechannel:
			voiceclient = await clientmember.move_to(voicechannel)
			voiceclient.cleanup()
		else: 
			await currentchannel.send('I\'m already here!')
	else:
		await currentchannel.send('You aren\'t in a voice channel!')
		return

@client.command()
async def leave(ctx):
	'''Makes the bot leave the channel it's in'''
	currentguild = client.get_guild(int(os.environ['ServerID'])) #Current server instance
	clientmember = currentguild.get_member(int(os.environ['ClientID'])) #Bot instance
	#voiceclient = None #Initialization for bot's voiceclient; needed for cleanup()
	currentchannel = ctx.channel #Text channel the command was sent in
	if isinstance(clientmember.voice, discord.VoiceState):
		server = ctx.message.guild.voice_client
		await server.disconnect()
	else:
		await currentchannel.send('I am not currently in a channel.')
	
#Events

@client.event
async def on_ready():
	'''Sends message to terminal on successful startup'''
	print('ZBot started successfully!')

@client.event
async def on_member_join(member):
	'''Sends message to terminal and welcome channel, and adds user to "Member" role on user joining the server'''
	print(f'{member.name} just joined the server!') #Message to terminal
	currentguild = client.get_guild(int(os.environ['ServerID'])) 
	welcomechannel = currentguild.get_channel(int(os.environ['WelcomeChannelID']))
	await welcomechannel.send(f'A wild {member.name} just appeared!') #Message to welcome channel
	memberrole = currentguild.get_role(int(os.environ['MemberRoleID']))
	await member.add_roles(memberrole) #Adds "Member" role to user

@client.event
async def on_member_remove(member):
	'''Sends message to terminal and welcome channel, on user leaving the server'''
	print(f'{member.name} just left the server!') #Message to terminal
	currentguild = client.get_guild(int(os.environ['ServerID'])) 
	welcomechannel = currentguild.get_channel(int(os.environ['WelcomeChannelID']))
	await welcomechannel.send(f'Say goodbye to {member.name}. They just left the server!') #Message to welcome channel
	
client.run(os.environ['Token'])