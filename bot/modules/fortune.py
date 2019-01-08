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
  if message.content.lower().startswith('.fortune'):
    random.seed(a=None, version=1)
    print('%s requesting %s' % (message.author.name, 'fortune'))
    lines = open('fortune.txt', encoding='utf8').read().splitlines()
    fortune = random.choice(lines)
    if len(message.content) <= 9:
        await client.send_message(message.channel, '%s\u0027s fortune for today is: %s' % (message.author.name, fortune))
    else:
        name = message.content.split('.fortune ')
        await client.send_message(message.channel, '%s\u0027s fortune for today is: %s' % (name[1], fortune))

client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
