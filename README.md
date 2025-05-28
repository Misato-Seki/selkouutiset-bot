# Selkouutiset Discord Bot

This bot fetches the latest news from Yle Selkouutiset (Easy Finnish News), translates and explains each word in Japanese using OpenAI, generates daily HTML pages for publication via GitHub Pages, and posts the URL of translated news to a Discord channel.

## Features

- Automatically fetches the latest articles from [Yle Selkouutiset](https://yle.fi/selkouutiset)
- Uses OpenAI API to translate and explain Finnish articles word-by-word in Japanese
- Generates and saves daily HTML files in the `translated_news/` directory
- Automatically removes old HTML files
- Posts daily translated news URL to a specified Discord channel
- Supports scheduled automation and deployment to GitHub Pages via GitHub Actions

## Project Structure

```
.
├── main.py                # Main entry point
├── app/
│   ├── fetch_articles.py  # Logic for fetching articles
│   ├── translator.py      # Translation and explanation logic
│   ├── html_generator.py  # Generate and save html file
│   └── bot.py             # Discord bot logic
├── debug/                 # Debug HTML and resources
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys, etc.)
├── Dockerfile             # Build instructions for the container image
└── .github/workflows/     # GitHub Actions workflows
```

## Setup

1. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Create a `.env` file and set the following environment variables:

   ```
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_BOT_TOKEN=your_discord_bot_token
   DISCORD_CHANNEL_ID=your_channel_id
   ```

3. Run the bot locally:

   ```sh
   python main.py
   ```

4. Using Docker

   Build the Docker image:
   ```shell
   docker build -t selkouutiset-bot .
   ```
   Run the container:
   ```shell
   docker run --rm \
   -e DISCORD_BOT_TOKEN=your_discord_bot_token \
   -e DISCORD_CHANNEL_ID=your_discord_channel_id \
   -e OPENAI_API_KEY=your_openai_api_key \
   -v $(pwd)/translated_news:/app/translated_news \
   selkouutiset-bot
   ```
   *Make sure your Discord bot is enabled and invited to the target channel.*

## Automation with GitHub Actions

- The workflow in `.github/workflows/deploy.yml` runs `main.py` automatically at 0:00 UTC every day.

## Main Files

- [`main.py`](main.py): Main controller and Discord posting
- [`app/fetch_articles.py`](app/fetch_articles.py): Fetches news articles
- [`app/translator.py`](app/translator.py): Explains each word in Japanese using OpenAI
- [`app/html_generator.py`](app/html_generator.py): Generates and manages HTML files
- [`app/bot.py`](app/bot.py): Discord bot implementation

## License

MIT License

---

Copyright for Yle Selkouutiset belongs to Yle.  
This is an unofficial personal project.