import discord
from sel_tut import get_weather_data

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=713587252952957029))  # Your server ID
    print("ready")

@tree.command(name="weather", description="Get the current weather")
async def slash_command(interaction: discord.Interaction):
    # Get the weather data
    temperature_, edited_address_, weather_icon_, weather_description_, image_url_, img_ = get_weather_data()
    
    # Create the Discord embed
    embed = discord.Embed(title=f"Current Weather of {edited_address_}")
    embed.set_thumbnail(url=image_url_)
    embed.add_field(name="Temperature", value=f"{temperature_} °F", inline=True)
    embed.add_field(name="Weather", value=weather_description_, inline=False)
    
    await interaction.response.send_message(embed=embed)

# run the bot
client.run("MTE3ODc2NzU0MjE0NDIyMTIxNQ.GrGUSa.XUWHcaBhNxkt8AgMGr8APYZwG-R-ERBhYJH2cE")


