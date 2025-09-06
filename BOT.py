import discord
import os
import random  
from dotenv import load_dotenv
import APP

load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hola, hemos iniciado sesión como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("¡Hola, bienvenido a mi primer bot!")
    elif message.content.startswith("!pswd"):
        pswd = APP.pswd_gnrtor(25)
        await message.channel.send(f"Tu contraseña es {pswd}")
    elif message.content.startswith("!flipcoin"):  
        result = APP.flip_coin()
        await message.channel.send(f"El resultado es: {result}")

client.run(token)
