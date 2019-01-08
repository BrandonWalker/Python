import discord, threading, logging
import asyncio
from modules import help 
from modules import a_or_b
from modules import addfortune
from modules import dice
from modules import fortune
from modules import info
from modules import shit
from modules import stuff
from modules import eightball

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
async def on_message(message):
    if message.content.startswith('.purge'):
        ans = message.content.replace('.purge','')
        deleted = await client.purge_from(channel1, limit=100,check=None, before=None, after=None)
        await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))
    elif message.content.startswith('redbot, ') or message.content.startswith('redbot ') and (' or ') in message.content.lower():
        a_or_b.a_or_b(message) # :^)
        return
client.run('MjAwMjE3NTQyMDI1OTM2ODk3.Cl6Cng.rRwIu4IM5YihAvdTzat4PSoijaA')
