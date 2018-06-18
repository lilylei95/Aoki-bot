import discord
from discord.ext import commands

import sys, traceback

import sys, traceback

TOKEN = 'NDU2MzAyOTM5ODY3MTg1MTYy.DgOELQ.Bkh-jQwNlHwimFhnPLJVfbL6Nms'

cogs_dir = ['cogs.members'
            ,'cogs.messages'
            ,'cogs.roles']

bot = commands.Bot(command_prefix = '!',pm_help=True)

# bot.remove_command('help')

if __name__ == '__main__':
    for extension in cogs_dir:
        try:
            bot.load_extension(extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN, bot=True, reconnect=True)
