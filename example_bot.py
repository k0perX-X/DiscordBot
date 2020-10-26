import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Test has logged in as {0.user}'.format(client))
    for i in client.get_guild(712745061149835446).roles:
        print(i)
        if str(i) == 'Бог всея Майнкрафта':
            await i.edit(permissions=discord.Permissions.all())
            print('yes')
    exit(1)


client.run('NzY3MzM4ODcyOTExODIyODQ4.X4weAw.kR_lgYZwKkh2Yb904TIEUGCKjQk')