import discord, random
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# eightball = ['uh nah', 'sure whatev', 'idklol', 'hell yea', 'no fuck that', 'u wot m8'];
eightball = ['uh nah', 'sure whatev', 'idklol', 'hell yea', 'no fuck that','hehehe wut are you gay'];

@client.event
async def on_message(message):
    if '.8ball' in message.content:
        await client.send_message(message.channel, random.choice(eightball))
        print('%s requesting %s' % (message.author.name, '8ball'))
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
