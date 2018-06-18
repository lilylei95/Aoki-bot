import discord
import re
from discord.ext import commands


num_regex = re.compile('^[0-9]+$')

class Messages:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        pass_context = True,
        brief='Clear Messages from channel',
        description = 'Clear all previous sent messages unless a number is specify.')
    async def clear(self,ctx, number: str = None):
        bot = self.bot
        if number == None:
            await bot.say("Clearing all messages...")
            messages = []
            async for message in bot.logs_from(ctx.message.channel):
                messages.append(message)
            await bot.delete_messages(messages)
        else:
            if number_regex.match(number):
                limit = int(number)
                messages = []

                await bot.say("Clearing last {} messages....".format(limit))
                async for message in bot.logs_from(ctx.message.channel,limit):
                    messages.append(message)
                await bot.delete_messages(messages)
            else:
                await bot.say("Time to get some !help :wink:!")


def setup(bot):
    bot.add_cog(Messages(bot))
