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
    if message.content.startswith('redbot, ') or message.content.startswith('redbot ') and (' or ') in message.content.lower():
        print('%s requesting %s' % (message.author.name, 'yes or no'))
        decisions = message.content.lower().replace('redbot', ''); decisions = decisions.replace(',', ''); decisions = decisions.split(' or ')
        choice = random.choice(decisions)
        await client.send_message(message.channel, '%s, %s' % (message.author.name, random.choice(decisions)))
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
