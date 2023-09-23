import discord
import random
import os
import requests
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

@bot.command()
async def mem(ctx):
    with open('M2L1\images\mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

    # with open('images/cat.jpg', 'rb') as f:
    #     picture = discord.File(f)

@bot.command()
async def randomMem(ctx):
    rastgele =random.choice(os.listdir('M2L1\images'))
    with open(f'M2L1\images\{rastgele}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def TatliKopek(ctx):
    rastgele2 =random.randint(1,50)
    if  rastgele2 > 30 :
        with open(f'M2L1\images\Tatli kopek 5.jpeg{rastgele2}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if  rastgele2 < 15 :
        with open(f'M2L1\images\Tatli kopek 4.jpeg{rastgele2}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if  25> rastgele2 >15 :
        with open(f'M2L1\images\Tatli kopek 3.jpeg{rastgele2}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if  30> rastgele2 >25 :
        with open(f'M2L1\images\Tatli kopek 2.jpeg{rastgele2}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    if  rastgele2 == 30 :
        with open(f'M2L1\images\Tatli kopek 1.jpeg{rastgele2}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("MTE0NDY1OTY2ODgyODk1MDU4OQ.GVk-K5.ZEjyGH2qlao73Yb6mxs3l7P5ZhNpM30BKUMels")