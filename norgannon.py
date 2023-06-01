import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import random
import asyncio
import time

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

quiz = {
    "Who was the last Guardian of Tirisfal?": ["Medivh"],
    "Who was the first Guardian of Tirisfal?": ["Alodi"],
    "Kalimdor translates from Titan and Darnassian to \"land of eternal ____.\"": ["starlight"],
    "The youngest World Tree, Teldrassil, was planted unde the leadership of Archdruid ____.": ["Fandral Staghelm", "Fandral", "Staghelm"],
    "Name the first Lich King.": ["Ner'zhul", "Nerzhul", "Ner zhul"],
}

@bot.command()
async def start_quiz(ctx):
    await ctx.send('The quiz is about to start in 2 minutes. Get ready!')
    await asyncio.sleep(2*60)
    
    questions = list(quiz.items())
    player_scores = {}

    for _ in range(5):
        question, answer = questions.pop(random.randint(0, len(questions) -1))
        
        await ctx.send(question)

        def check(m):
            return m.content.lower() in map(str.lower, answer) and m.channel == ctx.channel
        
        try:
            msg = await bot.wait_for('message', check=check, timeout=10)
            author = msg.author

            if author.id not in player_scores:
                player_scores[author.id] = 0
            
            player_scores[author.id] += 1
            await ctx.send(f"{msg.author.mention} got it right!")
        except asyncio.TimeoutError:
            await ctx.send("Time is up! No one answered correctly.")

        time.sleep(5)

    await ctx.send("The quiz has ended. Here are the final scores:")

    for player_id, score in player_scores.items():
        player = bot.get_user(player_id)
        await ctx.send(f"{player.mention}: {score} points")

bot.run(token)