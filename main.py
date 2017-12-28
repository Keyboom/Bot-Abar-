import discord
from discord.ext import commands
import psutil
import os
import asyncio
import requests
import datetime

pid = os.getpid()
pidPs = psutil.Process(pid)
usoMemoria = pidPs.memory_info()[0]
prefixo = '!'
bot = commands.Bot(command_prefix=prefixo, description='Teste')
@bot.event
async def on_ready():
    print('Bot logado como')
    print(bot.user.name)
    print(bot.user.id)
    print(''.join('Utilizando '+str(usoMemoria)+' de RAM'))
    

@bot.command()
async def kicknatan():
    servidor = bot.get_server(str(258014545715396608))
    await bot.kick(servidor.get_member_named('GoodMan215#5854'))
    await print('Natan foi kickado às '+datetime.datetime.now())

bot.run('MjczNDU4NTg1OTA2NzA4NDgw.DRcmRw.rmATh3kOl6V_k_rhtKHywWzrC8E')
