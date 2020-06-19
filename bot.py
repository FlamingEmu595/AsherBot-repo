from discord.ext import commands
import json
coglist = ["basic", "jishaku"]  # jishaku is a very helpful tool for d.py bots
settings = open("settings.json").read()  # read settings.json in
settings = json.loads(settings)  # make it a dictionary


class AsherBot(commands.AutoShardedBot):
    async def on_ready(self):
        print("Ready to go")

    async def on_message(self, message):
        if message.author.bot:  # ignore bots
            return

        await self.process_commands(message)  # finally, process commands

    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.CommandNotFound):
            return
        print(exception)


bot = AsherBot(  # create the bot
    command_prefix=settings["prefix"],
    case_insensitive=True
)

for extension in coglist:  # load each file in cogs/
    prefix = "cogs."
    if extension == "jishaku":  # jishaku isn't a cog, so no prefix if its found
        prefix = ""
    try:
        bot.load_extension(prefix + extension)  # load it
        print('Successfully loaded ' + extension)
    except Exception as e:  # unless something goes wrong
        exc = "{}: {}".format(type(e).__name__, e)
        print(f"Failed to load {extension}\nError: {exc}")

bot.run(settings["token"])
