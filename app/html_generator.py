import os
import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

def generate_html(articles):
    """
    Generates an HTML page containing a summary of the given news articles.

    Args:
        articles (list): A list of dictionaries where each dictionary contains
            the title, URL, date and summary of a news article.

    Returns:
        str: The HTML content.
    """
    html = '''
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { font-size: xx-large; }
        h2 { font-size: larger; }
        p { font-size: medium; }
    </style>
    </head>
    <body>
      <h1>Selkouutiset ''' + yesterday.strftime("%m-%d") + '''</h1>
      <a href="https://yle.fi/selkouutiset">https://yle.fi/selkouutiset</a>
    '''
    for article in articles:
        html += f'''
        <h2>{article['heading']}</h2>
        <p>{article['paragraph'].replace('\n', '<br>')}</p>
        '''
    html += '</body></html>'
    return html

def save_html(html):
    """
    Saves the given HTML content to a file named with yesterday's date.

    Args:
        html (str): The HTML content to be saved.

    The file is saved in the 'translated_news' directory with the filename
    format 'YYYY-MM-DD.html', where 'YYYY-MM-DD' is yesterday's date.
    """

    os.makedirs('translated_news', exist_ok=True)  # Create the directory if it doesn't exist

    filename = f"translated_news/{yesterday.strftime('%Y-%m-%d')}.html"
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(html)
    print(f"HTML file saved as {filename}")

def cleanup_old_html(days_to_keep=7):
    """
    Deletes HTML files older than the specified number of days.
    """
    now = datetime.datetime.now()
    dir_path = 'translated_news'
    for file in os.listdir(dir_path):
        if file.endswith('.html'):
            try:
                date_str = file.replace('.html', '')
                file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                if (now - file_date).days > days_to_keep:
                    os.remove(os.path.join(dir_path, file))
                    print(f"Deleted old file: {file}")
            except Exception:
                pass

if __name__ == "__main__":
    # Example usage
    articles = [
        {
            "heading": "Ruokalähetit",
            "paragraph": "Sitten asiaa ruokalähettien työstä.\nOikeus on tehnyt tärkeän päätöksen ruokalähetin asemasta.\nKorkein hallinto-oikeus on päättänyt, että ruokalähetti on firman työntekijä. Oikeuden päätös koskee ruokaa kuljettavaa Wolt-firmaa.\nOikeuden päätös tarkoittaa, että lähettien tilanne paranee. Heitä koskevat pian lait, jotka liittyvät lomaan, työsopimukseen ja työn turvallisuuteen.\nLähetit voivat kuitenkin itse päättää, milloin ja miten paljon he tekevät töitä.\nOikeus on tehnyt tärkeän päätöksen ruokalähetin asemasta."
        },
        {
            "heading": "Selkokieli",
            "paragraph": "Lopuksi asiaa selkokielestä.\nSelkokieltä tarvitaan Suomessa enemmän kuin ennen.\nSelkokieltä tarvitsee yli 800 000 ihmistä. Tämä selviää uudesta arviosta.\nSelkokielen tarve on kasvanut jo monta vuotta.\nEsimerkiksi moni yli 65-vuotias tarvitsee selkokieltä. Selkokieli auttaa myös maahanmuuttajia.\nSelkokieltä tarvitaan Suomessa yhä enemmän.\nSelkokielen rakenne ja sanat ovat helppoja ymmärtää.",
        }
    ]

    html_content = generate_html(articles)
    save_html(html_content)