import discord
from discord.ext import commands
import random

# Set up bot command prefix (e.g., !rps)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Define available choices
choices = ["rock", "paper", "scissors"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def rps(ctx, user_choice: str):
    user_choice = user_choice.lower()

    # Validate the user's input
    if user_choice not in choices:
        await ctx.send("Please choose one of: rock, paper, or scissors.")
        return

    # Bot makes a random choice
    bot_choice = random.choice(choices)

    # Determine the result
    if user_choice == bot_choice:
        result = "It's a draw!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        result = "You win! 🎉"
    else:
        result = "You lose! 😢"

    # Send the result back to the Discord channel
    await ctx.send(f'You chose **{user_choice}**, I chose **{bot_choice}**.\n{result}')

# Replace with your actual bot token
bot.run("YOUR_DISCORD_BOT_TOKEN")
