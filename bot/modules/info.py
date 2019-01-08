import discord, random

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
 if message.content.lower() == '.info':
    await client.send_message(message.channel, '''Server name: %s
Server owner: %s
Server region: %s'''  % (message.channel.server.name, message.channel.server.owner, message.channel.server.region))
    await client.send_message(message.channel, 'redbot built on old body of shellbot credit goes to shell')
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
