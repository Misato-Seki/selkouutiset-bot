from app.fetch_articles import fetch_articles
from app.translator import translator
from app.bot import send_message, client, TOKEN
import asyncio
from datetime import datetime

async def main():
    # URL of the article to fetch
    article_url = "https://yle.fi/selkouutiset"
    
    # Fetch the articles from the URL
    articles = fetch_articles(article_url)

    today = datetime.now().strftime("%m月%d日")

    message = f"{today}のニュース\n\n{article_url}\n\n"
    
    # Translate each article and send bot messages
    if articles:
        for idx, article in enumerate(articles, 1):
            translation = translator(article)
            message += f"{translation}\n---\n"
            print(f"記事{idx}\n{translation}\n\n")
    else:
        print("No articles found.")

    # Send the final message to the Discord channel
    await send_message(message)
        
if __name__ == "__main__":
    async def run_bot():
        """
        Logins to Discord and connects to the gateway, then runs the bot until stopped.
        """
        await client.login(TOKEN)
        await client.connect()

    loop = asyncio.get_event_loop() 
    
    loop.create_task(run_bot()) 
    loop.run_until_complete(main()) 