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
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def KiminBotusun(ctx):
    await ctx.send(f'ben mehmet efenin botuyum ')
@bot.command()
async def emoji(ctx):
    await ctx.send("🤣")
@bot.event
async def on_message_delete(message):
    print(message.content)

@bot.event
async def on_typing(channel, user, when):
    await channel.send(f"{user.display_name} fazla vaktimi alma :(")
bot.run("MTE0NDY1OTY2ODgyODk1MDU4OQ.GVk-K5.ZEjyGH2qlao73Yb6mxs3l7P5ZhNpM30BKUMels")