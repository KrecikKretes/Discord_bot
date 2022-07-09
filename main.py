import discord
import os
import requests
import json
import random
import datetime

from discord.ext import commands
from discord.utils import get


client = discord.Client()
client = commands.Bot(command_prefix = '<3', case_insensitive=True)


def jprint(obj):
  for d in obj:
    test =d['media']
  for d in test:
    testy =d['gif']
    #text = json.dumps(testy, sort_keys=True, indent=4)
  return testy['url']


@client.command()
async def hello(ctx):
    await ctx.send('Hello!')
    print(ctx)

@client.command()
async def EasyGirl(ctx):
    await ctx.send('I love you <3')

@client.command()
async def Romantic(ctx):
  apikey = os.getenv('TOKENgif')
  pos = random.randint(0, 50)
  search_term = "love bear"
  r = requests.get ("https://g.tenor.com/v1/search?q=%s&key=%s&pos=%s" % (search_term, apikey, pos))
  if r.status_code == 200:
    await ctx.send(jprint(r.json()['results']))

@client.command()
async def Kiss(ctx):
    apikey = os.getenv('TOKENgif')
    pos = random.randint(0, 50)
    search_term = " cute kiss"
    r = requests.get ("https://g.tenor.com/v1/search?q=%s&key=%s&pos=%s" % (search_term, apikey, pos))
    if r.status_code == 200:
     await ctx.send(jprint(r.json()['results']))

@client.command()
async def ilove(ctx, arg=None):
  if arg is not None:
    apikey = os.getenv('TOKENgif')
    pos = random.randint(0, 50)
    search_term = "love"
    r = requests.get ("https://g.tenor.com/v1/search?q=%s&key=%s&pos=%s" % (search_term, apikey, pos))
    if r.status_code == 200:
      message= await ctx.send(arg + 'Someone love You :point_right: :point_left:')
      emoji ='\U0001F497'
      await message.add_reaction(emoji)
      await ctx.send(jprint(r.json()['results']))
  else:
    emoji='\U0001F615'
    await ctx.send("But who do you love? "+emoji)

@client.command()
async def Bunny(ctx, arg=None):
  if arg is not None:
   apikey = os.getenv('TOKENgif')
   pos = random.randint(0, 50)
   search_term = "animal bunny"
   r = requests.get ("https://g.tenor.com/v1/search?q=%s&key=%s&pos=%s" % (search_term, apikey, pos))
   emoji='\U0001f97a'
   if r.status_code == 200:
    await ctx.send(arg + 'Someone send you a sweet bunny '+emoji+'\n'+jprint(r.json()['results']))
  else:
    emoji='\U0001F62D'
    await ctx.send("You can't send someone a bunny without someone"+emoji)

@client.command()
async def hug(ctx, arg=None):
  if arg is not None:
    apikey = os.getenv('TOKENgif')
    pos = random.randint(0, 50)
    search_term = "hugging"
    r = requests.get ("https://g.tenor.com/v1/search?q=%s&key=%s&pos=%s" % (search_term, apikey, pos))
    if r.status_code == 200:
      messagee= await ctx.send(arg + 'Someone want hug You. Do you hug him/her back? :hugging:')
      emojii ='\U0001F497'
      await messagee.add_reaction(emojii)
      await ctx.send(jprint(r.json()['results']))
  else:
    emoji='\U0001F615'
    await ctx.send("To hug you need 2 or more people, know you? "+emoji)


@client.command(pass_context=True)
async def helpo(ctx):
    embed = discord.Embed(
      colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='<3EasyGirl', value='When someone got turned on', inline=False)
    embed.add_field(name='<3Romantic', value='Send Love Bears', inline=False)
    embed.add_field(name='<3Kiss', value='Send someone kiss or kisses', inline=False)
    embed.add_field(name='<3Ilove', value='Confess your love to someone', inline=False)
    embed.add_field(name='<3Bunny', value='Sweet Bunny for everyone', inline=False)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):
  id=payload.channel_id
  if payload.member.name != 'Kretbot':
    channel = client.get_channel(id)
    message = await channel.fetch_message(payload.message_id)
    message_data = message.created_at
    if message.author.name == "Kretbot":
      reaction = get(message.reactions, emoji=payload.emoji.name)
      heartpulse = '\U0001F497'
      now = datetime.datetime.now()
      timestamp = datetime.datetime.timestamp(message_data)
      timestamp = timestamp + 60
      dt_object = datetime.datetime.fromtimestamp(timestamp)
      if dt_object >= now :
        if reaction.emoji == heartpulse and reaction.count > 1:
          await message.channel.send(":point_right: :point_left: Oh how sweet!!! :point_right: :point_left:")

client.run(os.getenv('TOKEN'))