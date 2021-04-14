import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def common(ctx):
    common = ["newbie", "shadowlands", "leveling","worgenDKs", "femaleOgres", "warlocks", "auAzeroth", "demonDeath", "undeadLight", "classRace", "auTimelines", "error"]
    await ctx.send("Here's a list of commands for our most Frequently Asked Questions:")
    for i in common:
        await ctx.send("?" + i)

@bot.command()
async def newbie(ctx):
    await ctx.send("Freqeuntly Asked Question: I'm new, where do I start with the lore? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_i.27m_new.2C_where_do_i_start_with_the_lore.3F")
    
@bot.command()
async def shadowlands(ctx):
    await ctx.send("Frequently Asked Question: How should I prepare for Shadowlands? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_how_to_prepare_for_shadowlands.3F")

@bot.command()
async def leveling(ctx):
    await ctx.send("Freqeuntly Asked Question: I've been leveling through the quest zones for the first time, and I'm confused. Where do all of these expansions fit in time? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_i.27ve_been_leveling_through_the_quest_zones_for_the_first_time.2C_and_i.27m_confused._the_original_zones_seem_to_take_place_after_some_of_the_expansions.2C_like_the_burning_crusade.2C_what.27s_going_on_there.3F_where_do_all_of_these_expansions_fit_in_time.3F")
    
@bot.command()
async def worgenDKs(ctx):
    await ctx.send("Freqeuntly Asked Question: How do Worgen Death Knights exist? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_how_do_worgen_death_knights_exist.3F")
    
@bot.command()
async def femaleOgres(ctx):
    await ctx.send("Frequently Asked Question: Do female ogres exist? Answer: Yes. https://wow.gamepedia.com/Ogre#Female_ogres")
    
@bot.command()
async def warlocks(ctx):
    await ctx.send("Frequently Asked Question: How do Warlocks fit into Alliance or Horde society? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_what_is_the_deal_with_warlocks.3F")

@bot.command()
async def auAzeroth(ctx):
    await ctx.send("Frequently Asked Question: What about AU Azeroth? Is there another version of ourselves? What are they up to? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_what_about_au_azeroth.3F_is_there_another_version_of_ourselves.3F_what_are_they_up_to.3F")
    
@bot.command()
async def demonDeath(ctx):
    await ctx.send("Frequently Asked Question: What happens to a demon when they die? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_what_happens_to_a_demon_when_they_die.3F_what_was_antorus.3F")

@bot.command()
async def undeadLight(ctx):
    await ctx.send("Frequently Asked Question: What happens to undead when they use the Light? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_what_happens_to_undead_when_they_use_the_light.3F")
    
@bot.command()
async def classRace(ctx):
    await ctx.send("Frequently Asked Question: Why can't [class] be [race]? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_why_can.27t_.5Binsert_race.5D_be_.5Binsert_class.5D.3F")
    
@bot.command()
async def auTimelines(ctx):
    await ctx.send("Frequently Asked Question: What is the deal with AU Draenor from Warlords of Draenor? What does it mean ""There is only one Legion?"" Is there more than one Archimonde? https://www.reddit.com/r/warcraftlore/wiki/index#wiki_what_is_the_deal_with_au_draenor_from_warlords_of_draenor.3F_what_does_it_mean_.22there_is_only_one_legion.3F.22_is_there_more_than_one_archimonde.3F")
    
@bot.command()
async def error(ctx):
    await ctx.send("No known answer for your query. This message includes examples of why that may be: https://www.reddit.com/r/warcraftlore/wiki/index#wiki_frequently_asked_questions_with_no_canon_answers.")
    
@bot.command()
async def quiz(ctx):
    await ctx.send("Quiz starts in 30 seconds.") 
    time.sleep(30)
    
    
    
bot.run(TOKEN)