import config
import Bot1
import Bot2
import asyncio

loop = asyncio.get_event_loop()
loop.create_task(Bot2.bot.start(config.TOKEN))
loop.create_task(Bot1.bot.start(config.TOKEN))
loop.create_task(Bot1.Tech.start(config.TOKEN_Tech))
loop.create_task(Bot1.Borshik5.start(config.TOKEN_Borshik5))
loop.run_forever()
