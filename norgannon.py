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
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

quiz = {
    "In the chronicles of Azeroth, who is known as the progenitor of the dragonflights, often revered as the 'Earth-Warder'?": ["Neltharion", "Deathwing"], #1
    "The name of which ancient Titan is associated with the ordering of Azeroth and the creation of the Titan-forged?": ["Aman'Thul", "Aman Thul", "Amanthul"], #2
    "The World Tree, Nordrassil, was grown atop which ancient and powerful well?": ["Well of Eternity"], #3
    "In the World of Warcraft: Shadowlands expansion, which realm serves as the afterlife for mortal druids, hunters, and nature-lovers?": ["Ardenweald"], #4
    "Named after the queen of the Naga, what is the underwater capital of the serpentine Naga race?": ["Nazjatar"], #5
    "Illidan Stormrage, the Betrayer, was transformed into a demon by consuming the power of which object?": ["Skull of Gul'dan", "Skull of Guldan", "Skull of Gul dan"], #6
    "In the World of Warcraft: Legion expansion, what is the name of the homeworld of the Burning Legion?": ["Argus"], #7
    "Who is the Zandalari troll loa of death?": ["Bwonsamdi"], #8
    "In the Cataclysm expansion, which elemental lord did adventurers confront in the Throne of the Tides?": ["Neptulon"], #9
    "Who is known as the Lightbringer, a paladin of the Silver Hand, who had a significant role in the human resistance against the undead Scourge?": ["Uther"], #10
    "What is the name of the neutral Pandaren faction dedicated to the brewing of powerful beverages?": ["Brewmasters", "The Brewmasters"], #11
    "What is the name of the Draenei's dimensional ship, crashed in Azuremyst Isle, called?": ["Exodar", "the Exodar"], #12
    "What are the vampiric elves, introduced in the Wrath of the Lich King expansion, called?": ["San'layn", "Sanlayn", "San layn"], #13
    "The Ashbringer sword is a powerful weapon against the undead. Who was its original wielder?": ["Alexandros Mograine", "Alexandros", "Mograine"], #14
    "Who was the troll that became the first of all death knights, created by Gul'dan?": ["Teron Gorefiend", "Teron", "Gorefiend", "Teron'gor", "Teron gor", "Terongor"], #15
    "Which Pandaren originally traveled with the orcish Horde during the events of Warcraft III?": ["Chen", "Chen Stormstout", "Stormstout"], #16
    "Who was the legendary blacksmith that crafted the Ashbringer?": ["Magni", "Magni Bronzebeard", "King Magni", "The King Under the Mountain"], #17
    "What do the initials 'K.T.' stand for in the name of the powerful lich boss found in Naxxramas?": ["Kel'thuzad", "Kel thuzad", "kelthuzad"], #18
    "Who took up the mantle of the Lich King after the defeat of Arthas Menethil?": ["Bolvar", "Bolvar Fordragon", "Highlord Bolvar", "Highlord Bolvar Fordragon", "Highlord Fordragon"], #19
    "Who was the dragon aspect enslaved by the Orc Dragonmaw Clan during the Second War?": ["Alexstrasza"], #20
    "What are the elite Horde warriors who ride wyverns into battle called? (Warcraft 3 title)": ["Wind Rider", "Wind Riders"], #21
    "What is the title given to the chief shaman of the Earthen Ring?": ["Farseer"], #22
    "What does the laid back Pandaren phrase 'sio'tha ti'nu!' translate to?": ["Slow down, life is to be savored!", "Slow down life is to be savored"] #23
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def start_quiz(ctx):
    await ctx.send('The Trial of Knowledge is set to commence in precisely two minutes. Prepare yourselves, Seekers of Truth!')
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
            await ctx.send(f"Well executed, Champion {msg.author.mention}!")
        except asyncio.TimeoutError:
            await ctx.send("Alas, time has slipped away in the sands of the Titan's Hourglass. It is a reminder that even in the vast cosmos governed by the Titans, every moment is precious. Do not be disheartened, Seeker of Truth. Fortify your resolve and be ready for the next inquiry.")

        time.sleep(5)
        print(player_scores)

    await ctx.send("The Trial of Knowledge, bestowed by the Titans, has reached its conclusion. The Scales of Wisdom now reveal the culmination of your efforts:")

    for player_id, score in player_scores.items():
        player = bot.get_user(player_id)
        await ctx.send(f"{player.display_name}: {score} Sparks of Enlightment")

bot.run(token)
