import discord
from discord.ext import commands
import cloudscraper

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

s = cloudscraper.create_scraper()

@bot.tree.command()
async def roulette(interaction: discord.Interaction):
    risk = "Nothing"
    guess = "Error"
    streak = "Error"
    currentid = s.get("https://rest-bf.blox.land/games/roulette").json()["current"]["_id"]
    first = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][0]["winningColor"]
    second = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][1]["winningColor"]
    third = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][2]["winningColor"]
    fourth = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][3]["winningColor"]
    fifth = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][4]["winningColor"]
    current_round = s.get("https://rest-bf.blox.land/games/roulette").json()["history"][0]["winningColor"]
    winning_colors_str = f"{first.title()}, {second.title()}, {third.title()}, {fourth.title()}, {fifth.title()}"

    if first == "purple" and second == "red" and third == "red":
        streak = "1 Purple 2 Red Winstreak"
        guess = "Purple"
    if first == "purple" and second == "purple" and third == "purple":
        streak = "3 Win Streak On Purple"
        guess = "Purple (50%)"
    if first == "red" and second == "red" and third == "red":
        streak = "3 Win Streak On Red"
        guess = "Red (50%)"
    if first == "yellow" and second == "yellow" and third == "yellow":
        streak = "3 Win Streak On Yellow"
        guess = "Error"

    if first == "purple" and second == "red" and third == "purple":
        streak = "2 Purple 1 Red Winstreak"
        guess = "Red"
    if first == "yellow" and second == "red" and third == "yellow":
        streak = "2 Yellow 1 Red Winstreak"
        guess = "Red Or Purple"
    if first == "yellow" and second == "purple" and third == "yellow":
        streak = "2 Yellow 1 Purple Winstreak"
        guess = "Red Or Purple"
    if first == "red" and second == "purple" and third == "purple":
        streak = "2 Purple 1 Red Winstreak"
        guess = "Red"
    if first == "purple" and second == "red" and third == "red":
        streak = "2 Red 1 Purple Winstreak"
        guess = "Purple"
    if first == "red" and second == "purple" and third == "red":
        streak = "2 Red 1 Purple Winstreak"
        guess = "Risky"
    if first == "purple" and second == "red" and third == "purple":
        streak = "2 Purple 1 Red Winstreak"
        guess = "Risky"
    if first == "red" and second == "red" and third == "purple":
        streak = "2 Red 1 Purple Winstreak"
        guess = "Red"
    if first == "purple" and second == "purple" and third == "red":
        streak = "2 Purple 1 Red Winstreak"
        guess = "Purple"


    if [first, second, third].count("red") == 1 and [first, second, third].count("purple") == 1 and [first, second, third].count("yellow") == 1:
    # Do something else
        streak = "1 Red 1 Purple 1 Yellow Winstreak"
        guess = "Couldn't Predict"
    if [first, second, third].count("red") == 1 and [first, second, third].count("yellow") == 2:
    # Do something else
        streak = "1 Red 2 Yellow Winstreak"
        guess = "Couldn't Predict"
    if [first, second, third].count("red") == 2 and [first, second, third].count("yellow") == 1:
    # Do something else
        streak = "2 Red 1 Yellow Winstreak"
        guess = "Couldn't Predict"
    if [first, second, third].count("purple") == 1 and [first, second, third].count("yellow") == 2:
    # Do something else
        streak = "1 Purple 2 Yellow Winstreak"
        guess = "Couldn't Predict"
    if [first, second, third].count("purple") == 2 and [first, second, third].count("yellow") == 1:
    # Do something else
        streak = "2 Purple 1 Yellow Winstreak"
        guess = "Couldn't Predict"




    if [first, second, third, fourth].count("red") == 4:
    # Do something else
        streak = "4 Red Winstreak"
        guess = "Red (50%)"
    if [first, second, third, fourth, fifth].count("red") == 5:
    # Do something else
        streak = "5 Red Winstreak"
        guess = "Couldn't Predict"
    if [first, second, third, fourth].count("purple") == 4:
    # Do something else
        streak = "4 Purple Winstreak"
        guess = "Purple (50%)"
    if [first, second, third, fourth, fifth].count("purple") == 5:
    # Do something else
        streak = "5 Purple Winstreak"
        guess = "Couldn't Predict"
    embed = discord.Embed(title="Roulette Prediction", color=discord.Color.yellow())
    embed.add_field(name="`🎮` Game Info", value=f"> **Round ID: {currentid}**")
    embed.add_field(name="`⭐ ` Prediction Info", value=f"> **Prediction:** **{guess}**\n> **Streak:** **{streak}**\n> **Last Games: {winning_colors_str}**\n> **Warnings:** **{risk}**")
    await interaction.response.send_message(embed=embed)
@bot.run("your token")
