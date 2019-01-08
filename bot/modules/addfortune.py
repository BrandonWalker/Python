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
  if message.content.lower().startswith('.addfortune'):
    print('%s requesting %s' % (message.author.name, 'addfortune'))
    if message.content == '.addfortune' or message.content == '.addfortune ':
        await client.send_message(message.channel, "Nothing to add.")
    else:
        with open('fortune.txt', 'a') as fortunes:
            content = message.content.replace('.addfortune ', '')
            fortunes.write('\n%s' % content)
            await client.send_message(message.channel, 'Added to the list of fortunes!')

client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
