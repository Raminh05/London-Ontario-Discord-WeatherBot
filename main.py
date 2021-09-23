import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = 'w/', description="") # Defines the command prefix to be "w/"

# Gets API key
with open(".env", encoding="utf-8") as f:
    api_key = f.read()
    f.close()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Kelcogg's ")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# Iterates through all filenames in the cogs directory to load all cogs.
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(api_key)


# Uncomment and re-implement to def temp if need be.
 # if condition == "Mostly Cloudy":
        #await ctx.send("The temperature is " + temp + " in London, Ontario. Condition: " + condition + " with a chance of meatballs") # Just for movie fun!
    #else:
        #await ctx.send("The temperature is " + temp + " in London, Ontario. Condition: " + condition)