import discord
import asyncio
from discord.ext import commands
import crawl
import numpy as np
import pandas as pd

token = "ODgyMTYyNzQ5NTM3Mzk0NzE4.YS3YFQ.l_WeAxA6uHik6VbLwfOKswapr7M"
bot_activity = discord.Game(name='동현우 감시')
bot = commands.Bot(command_prefix='.',activity = bot_activity)




@bot.event
async def on_ready():
    print('등장!')

@bot.command()
async def 핑(ctx):
    await ctx.send('퐁')

@bot.event
async def on_message(message):
    message_content = message.content
    if message_content == '김기수':
        await message.channel.send('존잘')
        # await message.delete()
    elif message_content == '고윤재':
        await message.channel.send('존잘')
    elif message_content == '최민서':
        await message.channel.send('존잘')
    elif message_content == '배':
        await message.channel.send('수찬')
    elif message_content == '남필량':
        await message.channel.send(':nose:')
    elif message_content == '박태욱':
        await message.channel.send('겨털')
    elif message_content == '씨발':
        await message.channel.send('바르고 고운말을 사용합시다')
        await message.delete()


    await bot.process_commands(message)

@bot.command()
async def message1(ctx,context):
    await ctx.send(f"단일명령어내용 : {context}\n 현재채널ID : {ctx.channel.id}\n 현재채널이름 : {ctx.channel.name}")

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)

@bot.command()
async def 전적(ctx, *, text):
    await ctx.send(f"{text}님의 최근 전적 불러오는중")
    await ctx.send(crawl.gamelog(text))

@bot.command()
async def 티어(ctx, *, text):
    soltier,subtier = crawl.nowtier(text).replace(('Bronze','브론즈'),('Silver','실버'))
    await ctx.send(f"{text}님의 현재 티어\n솔로랭크 : {soltier}\n자유랭크 : {subtier}")
    print(soltier,subtier)

@bot.command()
async def 도움말(ctx):
    await ctx.send('.핑 : 동모니터가 퐁 으로 받아줍니다.')
    await ctx.send('.전적 [롤닉네임] : 해당 사용자의 최근 20판의 전적을 보여줍니다.')
    await ctx.send('.티어 [롤닉네임] : 해당 사용자의 현재 솔랭 티어를 보여줍니다')
    await ctx.send('.따라하기 [따라할말] : 입력한 말을 따라합니다.')


bot.run(token)








# import discord

# client = discord.Client()

# token = "ODgyMTYyNzQ5NTM3Mzk0NzE4.YS3YFQ.Qa1I76p2kzOBiezinAbnGqKth_Y"

# client.run(token)