import discord 
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_message(message):
   if ('fuck ' or 'fk ') in message.content.lower() and 'you ' in message.content.lower() and 'redbot' in message.content.lower():
        print('%s requesting %s' % (message.author.name, 'flip the bird'))
        await client.send_message(message.channel, 'http://b.1339.cf/ikphooc.gif')
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
