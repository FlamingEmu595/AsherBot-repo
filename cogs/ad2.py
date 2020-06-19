import discord
import random
import json
from discord.ext import commands


class AD2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wisdom(self, ctx):
        """ Roll for wisdom.. """
        wisdoms = json.loads(open("insights.json").read())
        number = random.randint(1, 20)
        result = wisdoms[str(number)]
        result = random.choice(result)
        embed = discord.Embed(
            title="Wisdom Check",
            description=f"You rolled a **{number}**!",
            color=discord.Color.purple()
        )
        embed.add_field(name="The voice in your head says:", value=result)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AD2(bot))
