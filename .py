import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def name(ctx):
    await ctx.send('İsmin nedir?')

@bot.command()
async def repeat(ctx, times: int, content='A.'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, left: int, right: int, left1: int, right1:int):
    await ctx.send(left + right + left1 + right1)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("Token")
