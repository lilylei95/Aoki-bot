@bot.command(pass_context=True)
async def greet(ctx):
    await bot.say('Hello {}!'.format(ctx.message.author.mention))
    await bot.say('By the way, {} you are a nerd.'.format(ctx.message.author.mention))

@bot.command(pass_context=True)
async def help(ctx):
    await bot.send_message(ctx.message.author, ALL_COMMANDS)

@bot.command(pass_context=True)
async def rules(ctx, arg1, arg2):
    if arg1 == 'accept':
        if arg2 == ctx.message.author:
            await delete_role(ctx.message.server, "new-member");
    else:
        await bot.send_message(ctx.message.author, "Invalid command. Type !rules to see the rules again.")

@bot.event
async def on_member_update(before,after):
    print('a')
    # await bot.send_message("general", "before")
    # await bot.say(before)
    # await bot.say("after {}".format(after))
