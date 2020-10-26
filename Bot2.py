import discord
import config
from random import random
import Speak

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    #print(message.author.id)
    for popusk in config.pohuy_list:
        #print(popusk[0])
        #print(len(popusk[1]))
        if popusk[0] == str(message.author.id) and len(popusk[1]) >= config.pohuy_count:
            #if random() < 0.34:
            await message.add_reaction('🇵')
            await message.add_reaction('🇴')
            await message.add_reaction('🇭')
            await message.add_reaction('🇺')
            await message.add_reaction('🇾')
            #await message.add_reaction(bot.get_emoji(config.emoji_pohui))
    return

@bot.event
async def on_typing(channel, user, when):
    print('Пишет ' + str(user))
    return


print('Bot2 imported')
if __name__ == "__main__":
    bot.run(config.TOKEN)