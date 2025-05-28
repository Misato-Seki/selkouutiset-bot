from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def translator(sentence):
    prompt = (
        "次のフィンランド語の記事を一文ずつ、各単語ごとに日本語で解説してください。"
        "出力例に倣って以下のように出力してください。\n"
        "出力例:\n\n"
        "🟦「Tämä on esimerkki.」\n\n"
        "Tämä: これは(tämä「これ」)\n"
        "on: である(olla「である」の現在形・三人称単数)\n"
        "esimerkki: 例(esimerkki「例」)\n\n"
        "➡️ 訳: 「これは例です。」\n\n"
        "次のフィンランド語の記事を解説してください。\n"
        f"文: {sentence}"
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",  # または "gpt-4" や "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "あなたはフィンランド語を日本語に単語ごとに説明する翻訳者です。"},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example usage
    example_sentence = "Avustusjärjestöt ja monet maailman johtajat arvostelevat Israelin tekoja"
    translation = translator(example_sentence)
    print(f"Translation:\n{translation}")