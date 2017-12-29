import discord
from discord.ext import commands
import psutil
import os
import asyncio
import requests
import datetime
import scrape as Scrape

pid = os.getpid()
pidPs = psutil.Process(pid)
usoMemoria = pidPs.memory_info()[0]
prefixo = '!'
bot = commands.Bot(command_prefix=prefixo, description='Teste')
servidor = None
natan = None

@bot.event
async def on_ready():
    print('Bot logado como')
    print(bot.user.name)
    print(bot.user.id)
    print(''.join('Utilizando '+str(usoMemoria)+' de RAM'))
    servidor = bot.get_server(str(258014545715396608))
    natan = servidor.get_member_named('GoodMan215#5854')

@bot.event
async def on_member_join(natan):
    natan = servidor.get_member_named('GoodMan215#5854')
    await bot.add_roles(natan,discord.utils.get(server.roles, name='Deveria Estar Banido'))

@bot.command()
async def kicknatan():
    servidor = bot.get_server(str(258014545715396608))
    await bot.kick(natan)
    await print('Natan foi kickado às '+datetime.datetime.now())

@bot.command()
async def imagem(word):
    await bot.say(Scrape.get_image_src(word))

bot.run('MjczNDU4NTg1OTA2NzA4NDgw.DRcmRw.rmATh3kOl6V_k_rhtKHywWzrC8E')
