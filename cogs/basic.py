import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ Ping """
        await ctx.send(f"Pong! **{round(self.bot.latency * 1000, 2)}ms**")

    @commands.command()
    async def embed_example(self, ctx, *, content=None):  # none by default makes it optional
        embed = discord.Embed(
            title="Embed title",
            color=discord.Color.green()
        )
        embed.add_field(name="This is a field", value="It sure is")
        embed.add_field(name="And so is this", value="ding ding ding")
        if content:
            embed.add_field(name="You told me that...", value=content, inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Basic(bot))
