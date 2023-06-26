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
    "Who is known as the 'Highfather of the Pantheon' among the Titans?": ["Aman'Thul", "Aman Thul", "Amanthul"], #2
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
    "What does the laid back Pandaren phrase 'sio'tha ti'nu!' translate to?": ["Slow down, life is to be savored!", "Slow down life is to be savored"], #23
    "What is the name of the poison used to kill King Llane Wrynn, leader of the Alliance?": ["Kingsbane"], #24
    "Who is the leader of the Ethereal race that provides various services to players in Shattrath City?": ["Haramad", "Nexus Prince Haramad", "Nexus-Prince Haramad"], #25
    "What is the native tongue of the Tauren race?": ["Taur-ahe", "Taur ahe", "Taurahe"], #26
    "What is the name of the legendary bow crafted by Alleria Windrunner?": ["Thas'dorah", "Thas dorah", "Thasdorah"], #27
    "What is the name of Thrall's wolf companion?": ["Snowsong"], #28
    "What does the Titan term 'Algalon' mean?": ["Observer"], #29
    "Who was the first death knight to be created by the Lich King in the Third War?": ["Arthas", "Arthas Menethil"], #30
    "Illidan once wielded the warglaives of this doomguard commander he defeated during the War of the Ancients.": ["Azzinoth"], #31
    "Who is the final boss in the raid 'Castle Nathria' in the Shadowlands expansion?": ["Sire Denathrius", "Denathrius"], #32
    "Who is the brother of Varok Saurfang?": ["Broxigar", "Broxigar the Red", "Broxigar the Red Axe", "Broxigar Saurfang"], #33
    "Who is the leader of the Shado-Pan, the elite military organization of the Pandaren?": ["Taran Zhu"], #34
    "Which Guardian of Tirisfal had a secret child with a human mage?": ["Aegwynn"], #35
    "Which archdruid planted the World Tree, Teldrassil?" : ["Fandral", "Fandral Staghelm"], #36
    "Who is the leader of the Blackwater Raiders of Booty Bay?": ["Baron Revilgaz", "Revilgaz"], #37
    "What is the name of the Zandalari troll who allied with the Mogu to bring back the Thunderking?": ["Zul", "Zul the Prophet", "Prophet Zul"], #38
    "Who became the Aspect of Magic after the death of Malygos?": ["Kalecgos", "Kalec"], #39
    "What is the name of the desert that lies east of Ironforge?": ["Badlands", "The Badlands"], #40
    "Who is the Naaru that was captured by the Blood Elves and later turned into the Void God Entropius?": ["M'uru", "Muru", "M uru"], #41
    "Who was the leader of the High Elves during the Troll Wars?": ["Dath'Remar", "Dath Remar", "Dath'Remar Sunstrider", "Dath Remar Sunstrider", "Dathremar"], #42
    "What is the title given to the leader of the Gnomes?": ["High Tinker"], #43
    "What is the highest rank that can be achieved in the Knights of the Silver Hand?": ["Highlord", "High Lord"], #44
    "The twin blades, Shalla'tor and Ellemayne, combine to create this legendary sword.": ["Shalamayne"], #45
    "What legendary blade, forged by night elves and the five dragonflights, is known as the 'high blade' in Thalassian?": ["Quel'Serrar", "Quel Serrar", "Quelserrar"], #46
    "Who is the final boss in the Blackwing Lair?": ["Nefarian"], #47
    "Who was the queen of Azjol-Nerub before the Scourge invaded?": ["Nezar'Azret", "Nezarazret", "Nezar Azret"], #48
    "Which region in the Eastern Kingdoms is known for its large lumber operation and is home to Gilneas Liberation Front?": ["Silverpine Forest", "Silverpine"], #49
    "Who led the Dragonmaw Clan in the Second War?": ["Zuluhed", "Zuluhed the Whacked"], #50
    "Onyxia used to spy on the Alliance in Stormwind by disguising herself as this persona.": ["Lady Katrana Prestor", "Katrana Prestor", "Lady Prestor"], #51
    "In which raid can you play a game of chess?": ["Karazhan"], #52
    "Who is the leader of the Earthen Ring?": ["Thrall"], #53
    "Who was the original Lich King before Arthas?": ["Ner'zhul", "Ner zhul", "Nerzhul"], #54
    "What is the name of the second raid of the World of Warcraft: Shadowlands expansion?": ["The Sanctum of Domination", "Sanctum of Domination"], #55
    "What is the name of Varian Wrynn's gladiatorial twin persona?": ["Lo'Gosh", "Logosh", "Lo gosh"], #56
    "What is the name of the elite Horde military group formed by Sylvanas Windrunner and lead by Nathanos Blightcaller?": ["Dark Rangers", "The Dark Rangers"], #57
    "Which deity do the Night Elves primarily worship?": ["Elune"], #58
    "What was the name of the Titanic watcher who bestowed life upon the mogu?": ["Ra-den", "Ra den", "RaDen", "Highkeeper Ra", "Highkeeper Ra-den", "Highkeeper Raden"], #59
    "Who is the leader of the Draenei?": ["Prophet Velen", "Velen"], #60
    "Who was Thrall's master during his days as a slave in Durnholde Keep?": ["Aedelas Blackmoore", "Blackmoore"], #61
    "Who was the origina leader of the Defias Brotherhood?": ["Edwin VanCleef", "VanCleef"], #62
    "In the events of the Cataclysm, who becomes the Aspect of Earth in Neltharion's place?": ["Thrall", "Goel", "Go'el", "Go el"], #63
    "Who was the original Warchief of the Horde?": ["Blackhand", "Blackhand the Destroyer"], #64
    "What is the name of the goblin Capital city, located in Azshara?": ["Bilgewater Harbor", "Bilgewater"], #65
    "Who is the leader of the Blood Knights of Silvermoon?": ["Lady Liadrin", "Liadrin"], #66
    "Which dragonflight was tasked with the protection of time?" : ["Bronze", "Bronze Dragonflight", "The Bronze"], #67
    "What is the name of the prison located in the western part of Stormwind City?": ["The Stockade", "Stockade"], #68
    "Who is the demigod responsible for teaching druidism to the night elves?": "Cenarius", #69
    "What is the name of Grommash Hellscream's famous axe?": ["Gorehowl"], #70
    "In which zone can one find the Caverns of Time?": ["Tanaris"], #71
    "What is the name of the first boss in the Black Temple?": ["High Warlord Naj'entus", "Naj'entus", "Naj entus, Najentus, High Warlord Najentus, High Warlord naj entus"], #72
    "What was the alternative universe name for the Horde?": ["Iron Horde", "The Iron Horde"], #73
    "What was the name of the ship that transported the human forces to the Broken Shore in the Legion expansion?": ["Skyfire", "The Skyfire"], #74
    "Who is the half-ogre, half-orc Champion of the Horde?": ["Rexxar"], #75
    "What is the name of the ancient Titan facility located in Storm Peaks?": ["Ulduar"], #76
    "Varian Wrynn reclaimed a belt that once belonged to this former Stormwind hero.": ["Anduin Lothar", "Lothar"], #77
    "This tiger loa is worshipped by the Farraki and the Zandalari trolls at his temple in Vol'dun.": ["Kimbul", "Eraka no Kimbul"], #78
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

    for _ in range(10):
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
