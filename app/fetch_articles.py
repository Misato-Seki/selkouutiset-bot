import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    """
    Fetches the article content from the given URL and returns it as a string.

    :param url: The URL of the article to fetch.
    :return: The plain text content of the article.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    current_article = []

    # Extract headings and paragraphs, group by heading
    for tag in soup.find_all(class_=["yle__article__heading", "yle__article__paragraph"]):
        text = tag.get_text(strip=True)
        if text:
            if "yle__article__heading" in tag.get("class", []):
                # 新しい記事の開始
                if current_article:
                    articles.append("\n".join(current_article))
                    current_article = []
                current_article.append(f"{text}")
            elif "yle__article__paragraph" in tag.get("class", []):
                current_article.append(f"{text}")
    if current_article:
        articles.append("\n".join(current_article))

    return articles

if __name__ == "__main__":
    # Example usage
    article_url = "https://yle.fi/a/74-20163650"
    article_content = fetch_articles(article_url)
    print(article_content[1])