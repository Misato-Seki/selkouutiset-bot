import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    """
    Fetches the article content from the given URL and returns it as a list of dicts.

    :param url: The URL of the article to fetch.
    :return: A list of dicts with 'heading' and 'paragraph' keys.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    current_heading = None
    current_paragraphs = []

    for tag in soup.find_all(class_=["yle__article__heading", "yle__article__paragraph"]):
        text = tag.get_text(strip=True)
        if text:
            if "yle__article__heading" in tag.get("class", []):
                if current_heading is not None:
                    articles.append({
                        "heading": current_heading,
                        "paragraph": "\n".join(current_paragraphs)
                    })
                    current_paragraphs = []
                current_heading = text
            elif "yle__article__paragraph" in tag.get("class", []):
                current_paragraphs.append(text)
    if current_heading is not None:
        articles.append({
            "heading": current_heading,
            "paragraph": "\n".join(current_paragraphs)
        })

    return articles

if __name__ == "__main__":
    # Example usage
    article_url = "https://yle.fi/a/74-20163650"
    article_content = fetch_articles(article_url)
    print(article_content)