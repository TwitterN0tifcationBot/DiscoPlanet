def create_bot(data):
    bot_name = data.get('bot_name', 'MyBot')
    token = data.get('token', 'YOUR_DISCORD_BOT_TOKEN')
    
    bot_code = f"""
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {{bot.user}}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('{token}')
"""
    return bot_code
