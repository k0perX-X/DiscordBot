import discord
from discord.ext import commands
import config
from threading import Timer

bot = commands.Bot(command_prefix='%') #инициализируем бота с префиксом '%'
Tech = discord.Client()
Borshik5 = discord.Client()

def del_pohuy(author, id):
    for popusk in config.pohuy_list:
        if popusk[0] == id: #id
            for i in range(len(popusk[1])):
                if popusk[1][i] == author: #author
                    popusk[1].pop(i)
                    break
    print('Для ' + str(id) + ' удален ' + str(author))

@bot.command()
async def п(ctx, arg='!'):
    if arg == '!':
        config.obn_nam_pohui()
        await ctx.send(config.pohui, files = config.nam_pohui)
        #await ctx.send('<@!338638966574153728>' + config.pohui_teg, files=config.nam_pohui)
    else:
        config.obn_nam_pohui()
        await ctx.send(str(arg) + config.pohui_teg, files = config.nam_pohui)

@bot.command()
async def похуй(ctx, arg='!'):
    if arg == '!':
        config.obn_nam_pohui()
        await ctx.send(config.pohui, files = config.nam_pohui)
        #await ctx.send('<@!338638966574153728>' + config.pohui_teg, files=config.nam_pohui)
    else:
        config.obn_nam_pohui()
        await ctx.send(str(arg) + config.pohui_teg, files = config.nam_pohui)

@bot.command()
async def можешьнеписать(ctx, arg='!'):
    if arg == '!':
        config.obn_nam_pohui()
        await ctx.send(config.mnt, files=config.nam_pohui)
    else:
        for sting in str(arg).split(): #ищу попуск
            if sting.isdigit():
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting, [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[3:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
            elif sting[2:-1].isdigit(): #ищу попуск
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting[2:-1] == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting[2:-1], [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[2:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, <@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
            elif sting[3:-1].isdigit(): #ищу попуск
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting[3:-1] == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting[3:-1], [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[3:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')

@bot.command()
async def мнп(ctx, arg='!'):
    if arg == '!':
        config.obn_nam_pohui()
        await ctx.send(config.mnt, files=config.nam_pohui)
    else:
        for sting in str(arg).split(): #ищу попуск
            if sting.isdigit():
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting, [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[3:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
            elif sting[2:-1].isdigit(): #ищу попуск
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting[2:-1] == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting[2:-1], [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[2:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, <@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
            elif sting[3:-1].isdigit(): #ищу попуск
                popusk_nayden = False
                for id in config.pohuy_list:
                    if sting[3:-1] == id[0]:
                        popusk_nayden = True
                        author_nayden = False
                        for member in id[1]:
                            if ctx.message.author == member:
                                author_nayden = True
                                break
                        if not author_nayden:
                            id[1].append(ctx.message.author)
                            t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, id[0]])
                            t.start()
                            if str(len(id[1])) == 1:
                                print('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                                await ctx.send('<@!' + id[0] + '>, ' + '<@!'+ str(id[1].id) + '> похуй на то, что ты пишешь')
                            else:
                                print('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                                await ctx.send('<@!'+ id[0] + '>, ' + str(len(id[1])) + ' людям похуй на то, что ты пишешь')
                if not popusk_nayden:
                    config.pohuy_list.append([sting[3:-1], [ctx.message.author]])
                    t = Timer(config.pohuy_time, del_pohuy, args=[ctx.message.author, sting[3:-1]])
                    t.start()
                    print('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')
                    await ctx.send('<@!' + config.pohuy_list[-1][0] + '>, ' + '<@!' + str(config.pohuy_list[-1][1][0].id) + '> похуй на то, что ты пишешь')

@bot.command()
async def тухлый(ctx):
    borsh = True
    tech = True
    if str(Borshik5.get_channel(ctx.channel.id)) == 'None':
        borsh = False
        await ctx.send('Пожалуйста, добавьте бота\nhttps://discord.com/api/oauth2/authorize?client_id=768115787776524358&scope=bot&permissions=2147483639&guild_id=' + str(ctx.guild.id))
    if str(Tech.get_channel(ctx.channel.id)) == 'None':
        tech = False
        await ctx.send('Пожалуйста, добавьте бота\nhttps://discord.com/api/oauth2/authorize?client_id=768116854622781502&scope=bot&permissions=2147483639&guild_id=' + str(ctx.guild.id))
    if borsh and tech:
        config.obn_tech_privet()
        await Borshik5.get_channel(ctx.channel.id).send('Мистер Тухлый?')
        await Tech.get_channel(ctx.channel.id).send('Да')
        await Borshik5.get_channel(ctx.channel.id).send('Мистер Борщик передаёт вам привет',  files=config.tech_pivet)

@bot.command(pass_context=True)
async def инициализация(ctx, arg):
    print(arg)
    await ctx.send('Инициализация прошла успешно :heart:')

@bot.command()
async def хелп(ctx):
    await ctx.send('Я очень крутой бот и вот, что я умею:\n%п (%похуй) {тег/id}(не обязательно)\n\t - сказать похуй человеку\n%мнп (%можешьнеписать) {тег/id}(обязательно)\n\t - запросить реакции похуй под каждое сообщение человека на ' + str(config.pohuy_time / 60) + ' минут, для активации требуется, чтобы '+ str(config.pohuy_count) + ' человек применило эту команнду \n%мнпс (%можешьнеписатьстатус) {тег/id}(обязательно)\n\t - статус команды можешьнеписать по определенному человеку (в разработке)\n%тухлый\n\t - вызывает диалог с тухлым')

print('Bot1 imported')
if __name__== "__main__":
    print('Bot1 is working')
    bot.run(config.TOKEN)