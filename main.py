import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot sudah online sebagai {bot.user}!")

async def main():
    async with bot:
        await bot.load_extension("music")
        await bot.load_extension("commands")
        await bot.start(TOKEN)

asyncio.run(main())
