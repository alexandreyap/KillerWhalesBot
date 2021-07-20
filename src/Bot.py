# bot.py
import os
from src.Commands.BotCommands import *
from dotenv import load_dotenv

from urllib import parse, request
import re

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    await ctx.send(randomDice(number_of_dice, number_of_sides))


# @bot.command(name='Reply')
# async def Reply(ctx):
#    channel = bot.get_channel(844284599130783769)
#    await channel.send(f'Hello there I am the bot')

@bot.command(name="yt", help="Search and returns first match on youtube")
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@bot.command(aliases=["tasks", "Todo"], help="List tasks in the todo list, aliases: Todo, tasks")
async def todo(ctx):
    StrList = getTask()
    Str = ""
    for i in range(len(StrList)):
        Str = Str + StrList[i] + '\n'
    await ctx.send(Str)


@bot.command(help="Same as todo")
async def todoList(ctx):
    StrList = getTask()
    Str = ""
    for i in range(len(StrList)):
        Str = Str + StrList[i] + '\n'
    await ctx.send(Str)


@bot.command(aliases=["taskAdd"], help="Add task to list, alias: taskAdd")
async def todoAdd(ctx, *args):
    if (len(args) == 0):
        await ctx.send("Expecting a task following the command.")
        return
    L = list(args)
    Str = " ".join(L)
    boolean = addTask(Str)
    if (boolean == False):
        await ctx.send("Adding task failed.")
    else:
        await ctx.send("Task added!")


@bot.command(help="Remove task at the given indexes")
async def todoRemove(ctx, *indexes: int):
    L = list(indexes)
    if (len(L) == 0):
        ctx.send("No indexes given.")
        return
    for i in range(len(L)):
        L[i] -= 1
    b = removeTask(L)
    if (b == False) :
        await ctx.send("Invalid index given, nothing is done.")
        return
    if (len(L) == 1):
        await ctx.send("Task removed.")
    else:
        await ctx.send("Tasks removed.")


@bot.command(aliases=["removeTask"], help="Same as todoRemove, aliases : removeTask")
async def TaskRemove(ctx, *indexes: int):
    L = list(indexes)
    if (len(L) == 0):
        ctx.send("No indexes given.")
        return
    for i in range(len(L)):
        L[i] -= 1
    b = removeTask(L)
    if (b == False) :
        await ctx.send("Invalid index given, nothing is done.")
        return
    if (len(L) == 1):
        await ctx.send("Task removed.")
    else:
        await ctx.send("Tasks removed.")


@bot.event
async def on_member_join(ctx, member):
    #    channel = bot.get_channel(844284599130783769)
    await ctx.send(f'Welcome {member.name} to KillerWhales!')


bot.run(TOKEN)
