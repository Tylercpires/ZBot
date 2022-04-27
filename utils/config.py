import discord
import os

#Bot token

token = os.environ.get("Token")

#Channel ids

welcomechannelid = int(os.environ.get("WelcomeChannelID"))

#Command options

intents = discord.Intents.all() #Permissions for the bot to perform certain actions
prefix = "." #Command prefix for the bot

#Role ids

devid = int(os.environ.get("DEVID"))
memberid = int(os.environ.get("MemberID"))

#Server id

serverid = int(os.environ.get("ServerID"))

#Time options

timeformat = "(%Y/%d/%m) %H:%M:%S: "
timezone = "Canada/Pacific"