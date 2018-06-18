import discord
import json
from discord.ext import commands

import sys, traceback

import sys, traceback

with open('settings/config.json') as f:
    data = json.load(f)

cogs_dir = ['cogs.members'
            ,'cogs.messages'
            ,'cogs.roles']

bot = commands.Bot(command_prefix = '!',pm_help=True)

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

bot.run(data["TOKEN"], bot=True, reconnect=True)
