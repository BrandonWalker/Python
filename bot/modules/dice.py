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
  if len(message.content.split()) > 1 and message.content.startswith('.roll'):
    messagearray = message.content.split()
    try:
            print('%s requesting %s' % (message.author.name, 'roll'))
            if len(message.content) > 30:
                await client.send_message(message.channel, "O-onii chan~ That number is to big~")
            else:
                dicearray = message.content.replace('.roll ', ''); dicearray = dicearray.split('d')
                number, roll = int(dicearray[0]), 0
                for x in range(0, number):
                    roll += random.randint(1, int(dicearray[1]))
                await client.send_message(message.channel, roll)
    except ValueError:
        print('%s requesting %s' % (message.author.name, 'failed roll'))
        pass
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
