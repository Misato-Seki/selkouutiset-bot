# Selkouutiset Discord Bot

This bot fetches the latest news from Yle Selkouutiset (Easy Finnish News), translates and explains each word in Japanese using OpenAI, and posts the result to a Discord channel.

## Features

- Automatically fetches the latest articles from [Yle Selkouutiset](https://yle.fi/selkouutiset)
- Uses OpenAI API to translate and explain Finnish articles word-by-word in Japanese
- Posts to a Discord channel daily (scheduled via GitHub Actions)

## Project Structure

```
.
├── main.py                # Main entry point
├── app/
│   ├── fetch_articles.py  # Logic for fetching articles
│   ├── translator.py      # Translation and explanation logic
│   └── bot.py             # Discord bot logic
├── debug/                 # Debug HTML and resources
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys, etc.)
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

## Automation with GitHub Actions

- The workflow in `.github/workflows/deploy.yml` runs `main.py` automatically every day at 6:00 AM (JST).

## Main Files

- [`main.py`](main.py): Main controller and Discord posting
- [`app/fetch_articles.py`](app/fetch_articles.py): Fetches news articles
- [`app/translator.py`](app/translator.py): Explains each word in Japanese using OpenAI
- [`app/bot.py`](app/bot.py): Discord bot implementation

## License

MIT License

---

Copyright for Yle Selkouutiset belongs to Yle.  
This is an unofficial personal project.