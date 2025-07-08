from discord.ext import commands
import random

quotes = [
    "Jangan menyerah sebelum mencoba.",
    "Kesuksesan dimulai dari mimpi.",
    "Belajar dari kegagalan adalah kunci.",
    "Kerja keras mengalahkan bakat ketika bakat tidak bekerja keras.",
]

class TextCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Halo {ctx.author.name}, saya bot kamu!")

    @commands.command()
    async def roll(self, ctx):
        angka = random.randint(1, 6)
        await ctx.send(f"{ctx.author.mention} melempar dadu dan mendapatkan angka **{angka}** 🎲")

    @commands.command()
    async def quote(self, ctx):
        q = random.choice(quotes)
        await ctx.send(q)

async def setup(bot):
    await bot.add_cog(TextCommands(bot))
