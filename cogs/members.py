import discord
from discord.ext import commands

class Members:
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self,member):
        role = discord.utils.get(member.server.roles, id="458028398627913759")
        channel = discord.utils.get(member.server.channels, id = '458023579477344267')

        # welcome message on new member channel
        await self.bot.send_message(channel, "Hello {}! Welcome to {}!".format(member.name, member.server.name))
        # give joining user new member role
        await self.bot.add_roles(member, role)
        # send out rules to new member
        await self.bot.send_message(member, "Rules: Please type !rule accept your-display-name-with-number")


def setup(bot):
    bot.add_cog(Members(bot))
