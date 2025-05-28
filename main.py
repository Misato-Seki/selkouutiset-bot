from app.fetch_articles import fetch_articles
from app.translator import translator
from app.bot import send_message, client, TOKEN
from app.html_generator import generate_html, save_html, cleanup_old_html
import asyncio

async def main():
    # URL of the article to fetch
    article_url = "https://yle.fi/selkouutiset"
    
    # Fetch the articles from the URL
    articles = fetch_articles(article_url)    

    translated_articles = []
    
    # Translate each article
    if articles:
        for article in articles:
            # Translate the article paragraph
            translated_paragraph = translator(article['paragraph'])
            translated_articles.append({
                'heading': article['heading'],
                'paragraph': translated_paragraph
            })
    else:
        print("No articles found.")

    # Generate the HTML content from the translated articles
    html = generate_html(translated_articles)
    save_html(html)
    # Cleanup old HTML files
    cleanup_old_html()

    # Send the final message to the Discord channel
    await send_message()
        
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