import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('.help'):
         await client.send_message(message.channel,'''Current commands:
    "ping" Test your ping to me.
    ".fortune" See what your 'fortune' for today is.
    ".roll 1d20" Roll some dice.
    "Shellbot, a or b" Tough decisions.
    ".8ball food" Useless 8ball.
    ".bug" Yell at Shell.
    ".info" Look at server info.
    And a few others ;)
    Note: Please do not spam the ShellBot''' )
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
