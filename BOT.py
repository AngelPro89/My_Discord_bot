import discord,os
import APP
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name= "pswd")
async def pswds(ctx,lenght = 25):
    data= APP.pswd_gnrtor(lenght)
    await ctx.send(f"🔒Contraseña generada: {data}")

bot.run(token)
