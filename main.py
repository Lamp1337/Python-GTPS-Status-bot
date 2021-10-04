#GTPS STATUS BOT
#reCoded by Lamp (CREDIT) KIPAS & NUMEX
import os
try:
    import discord, datetime, time, threading, json
    from discord.ext import commands
    from datetime import datetime
except:
    os.system('pip install discord')

with open('./config.json', 'r') as confjs:
    config = json.load(confjs)

client = commands.Bot(command_prefix="?", help_command=None)

player = open('onlines.txt').readlines()

@client.event
async def on_ready():
    print("Bot is online")
    await client.change_presence(activity=discord.Game(name=f"Join {player[0]} others online."))

@client.command()
async def serverup(ctx):
    if ctx.author.id == YOUR_ID:
        player = open('onlines.txt').readlines()
        listworldss = len(os.listdir('worlds'))
        listplayerss = len(os.listdir('players'))
        tm = datetime.now()
        tim = tm.strftime('%H:%M %p')
        await ctx.send("@everyone")
        embed = discord.Embed(color=0x00ff00, title='GTPS Status Bot',
        description=f"**Server Status : UP\nPlayer Online : {player[0]}\nTotal Players Create : {listplayerss}\nTotal Worlds Create : {listworldss}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/885876229083893813/894513371225944124/sssssssssssssssssssssssss.jpg")
        embed.set_footer(text='Last Update Today ' + tim + '')
        await client.change_presence(activity=discord.Game(name=f"Join {player[0]} others online."))
        text = await ctx.send(embed=embed)
        time.sleep(1)
        while True:
            players = open('onlines.txt').readlines()
            listworld = len(os.listdir('worlds'))
            listplayers = len(os.listdir('players'))
            newembed = discord.Embed(color=0x00ff00, title='GTPS Status Bot',
            description=f"**Server Status : UP\nPlayer Online : {players[0]}\nTotal Players Create : {listplayers}\nTotal Worlds Create : {listworld}**")
            newembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/885876229083893813/894513371225944124/sssssssssssssssssssssssss.jpg")
            newembed.set_footer(text='Last Update Today ' + tim + '')
            await client.change_presence(activity=discord.Game(name=f"Join {players[0]} others online."))
            edit = threading.Thread(target = await text.edit(embed=newembed))
            edit.start()
            time.sleep(1)
    else:
        await ctx.send('Oops! You dont have permission do that')

@client.command()
async def serverdown(ctx):
    if ctx.author.id == YOUR_ID:
        player = open('onlines.txt').readlines()
        listworldss = len(os.listdir('worlds'))
        listplayerss = len(os.listdir('players'))
        tm = datetime.now()
        tim = tm.strftime('%H:%M %p')
        await ctx.send("@everyone")
        embed = discord.Embed(color=0x00ff00, title='GTPS Status Bot',
        description=f"**Server Status : DOWN\nPlayer Online : {player[0]}\nTotal Players Create : {listplayerss}\nTotal Worlds Create : {listworldss}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/885876229083893813/894513371225944124/sssssssssssssssssssssssss.jpg")
        embed.set_footer(text='Last Update Today ' + tim + '')
        await client.change_presence(activity=discord.Game(name=f"Join {player[0]} others online."))
        text = await ctx.send(embed=embed)
        time.sleep(1)
        while True:
            players = open('onlines.txt').readlines()
            listworld = len(os.listdir('worlds'))
            listplayers = len(os.listdir('players'))
            newembed = discord.Embed(color=0x00ff00, title='GTPS Status Bot',
            description=f"**Server Status : DOWN\nPlayer Online : {players[0]}\nTotal Players Create : {listplayers}\nTotal Worlds Create : {listworld}**")
            newembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/885876229083893813/894513371225944124/sssssssssssssssssssssssss.jpg")
            newembed.set_footer(text='Last Update Today ' + tim + '')
            await client.change_presence(activity=discord.Game(name=f"Join {players[0]} others online."))
            edit = threading.Thread(target = await text.edit(embed=newembed))
            edit.start()
            time.sleep(1)
    else:
        await ctx.send('Oops! You dont have permission do that')

@client.command()
async def help(ctx):
    await ctx.reply("```\n?help (show this command)\n?serverup (for show the server is up)\n?serverdown (for show the server is down)```")

client.run(config["TOKEN"])
