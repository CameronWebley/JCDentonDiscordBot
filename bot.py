import os, discord, quoteGenerator
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="_", intents=intents)

@bot.event
async def on_ready():
    print(
        f"{bot.user.name} has connected to the Discord!")

@bot.command(name="shame", help="Responds with 'What a shame'.")
async def shame(ctx):
    await ctx.send("What a shame.")

@bot.command(name="quote", help="Generates a new JC Denton quote")
async def quote(ctx, length: int):
    q = quoteGenerator.QuoteGenerator()
    q.createScript("jcScript.txt")
    await ctx.send(q.generateQuote(length))


'''
TODO -- THIS COMMAND REQUIRES DISCORD.PY [VOICE] (I THINK) AND ANOTHER EXTERNAL MODULE
@bot.command(name="test")
async def test(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="test.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()
'''

bot.run(TOKEN)