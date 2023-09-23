import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
Puan = 0
@bot.command()
async def oyun(ctx):
    await ctx.send(f'Merhaba ben bir botum size sorular soracağım sizde doğru sıkları yazacaksınız 5 soru vardır soruları çağırmak için soru1 soru2 vs. kullanın')
    @bot.command()
    async def soru1(ctx):
        await ctx.send(f'karton hangi kutuya konur a/kağıt b/cam c/metal d/plastik')
        @bot.command()
        async def a(ctx):
            await ctx.send(f'aferin ')
        @bot.command()
        async def b(ctx):
            await ctx.send(f'üzgünüm yanlış cevap ')
        @bot.command()
        async def c(ctx):
            await ctx.send(f'üzgünüm yanlış cevap ')
        @bot.command()
        async def d(ctx):
            await ctx.send(f'üzgünüm yanlış cevap')
        
    @bot.command()
    async def soru2(ctx):
        await ctx.send(f'plastik şişe hangi kutuya konur a/kağıt b/cam c/metal d/plastik')
        @bot.command()
        async def a(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def b(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def c(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def d(ctx):
            await ctx.send(f'aferin')

    @bot.command()
    async def soru3(ctx):
        await ctx.send(f'gazoz şişesi hangi kutuya konur a/kağıt b/cam c/metal d/plastik')
        @bot.command()
        async def a(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def b(ctx):
            await ctx.send(f'aferin ')
        
        @bot.command()
        async def c(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def d(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')

    @bot.command()
    async def soru4(ctx):
        await ctx.send(f'dondurma kabı hangi kutuya konur a/kağıt b/cam c/metal d/plastik')
        @bot.command()
        async def a(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def b(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def c(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def d(ctx):
            await ctx.send(f'Aferin')

    @bot.command()
    async def soru5(ctx):
        await ctx.send(f'teneke kola hangi kutuya konur a/kağıt b/cam c/metal d/plastik')
        @bot.command()
        async def a(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def b(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')
        
        @bot.command()
        async def c(ctx):
            await ctx.send(f'Aferin')
        
        @bot.command()
        async def d(ctx):
            await ctx.send(f'Üzgünüm yanlış cevap')

bot.run("MTE0NDY1OTY2ODgyODk1MDU4OQ.GVrgDx.FDSdY8CZXngr4IqZ_Ro-EVulNVRov5JE-QboY0")