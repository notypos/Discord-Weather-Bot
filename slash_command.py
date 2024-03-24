import discord
import requests
from discord import app_commands
from discord.ext import commands
from sel_tut import get_weather_data

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="weather", description="Get current weather")
@app_commands.describe(location = "zip code, or city")
async def weather(interaction: discord.Interaction, location: str):
    await interaction.response.defer()
    temperature_, edited_address_, weather_icon_, weather_description_, image_url_, img_ = get_weather_data(location)
    webhook_url = 'https://discord.com/api/webhooks/1177670103752515584/DJd25scHB96dBa-2fgnEqwsbiKTsPGT6q2hnteuG0M87le79wvjD9cwdYHQo_2J2inPT'
    data = {
    "avatar_url": "https://www.shutterstock.com/image-photo/mostly-sunny-weather-260nw-286242953.jpg",
    "embeds": [
        {
            "title": f"Current Weather of {edited_address_}",
            "thumbnail": {
                "url": image_url_
            }, 
            "fields": [
                {
                    "name": "Temperature",
                    "value": f"{temperature_} °F", 
                    "inline": True
                }, 
                {
                    "name": "Weather",
                    "value": weather_description_,
                    "inline": False
                }
            ]
        }        
    ]
    }


#files_ = {'file': ('weather_icon.png', open('weather_icon.png', 'rb'))}
    r = requests.post(webhook_url, json=data)

    print(r)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"Hey {interaction.user.mention} said: '{thing_to_say}'")

bot.run("MTE3ODc2NzU0MjE0NDIyMTIxNQ.GrGUSa.XUWHcaBhNxkt8AgMGr8APYZwG-R-ERBhYJH2cE")