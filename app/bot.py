import discord
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
article_url = "https://yle.fi/selkouutiset"

async def send_message():
    await client.wait_until_ready()
    
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f"Translated Selkouutiset for {yesterday.strftime('%m/%d')}: https://misato-seki.github.io/selkouutiset-bot/{yesterday.strftime('%Y-%m-%d')}.html")
    await client.close()

if __name__ == "__main__":
    if not TOKEN or not CHANNEL_ID:
        print("Please set DISCORD_BOT_TOKEN and DISCORD_CHANNEL_ID in your .env file.")
    else:
        print("Bot is ready to run. Use main.py to start the bot.")