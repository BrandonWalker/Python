import discord
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def joined(member : discord.Member):
    await client.send_message(message.channel, "hello  onii chan  (●´ω｀●). please use .help to see what I can do   ")
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
