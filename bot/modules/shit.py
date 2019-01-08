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
    if message.content.lower().endswith(' is shit'):
        print('%s requesting %s' % (message.author.name, 'is shit'))
        await client.send_message(message.channel, 'What %s meant to say is: **%s is the greatest thing ever!**' % (message.author.name, message.content.replace(' is shit'.lower(), '')))
    elif message.content.lower().endswith(' a shit'):
        print('%s requesting %s' % (message.author.name, 'is shit'))
        await client.send_message(message.channel, 'What %s meant to say is: **%s is the greatest thing ever!**' % (message.author.name, message.content.replace(' a shit'.lower(), '')))
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')

