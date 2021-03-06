import requests

from const import  NEWS_API_URL, NEWS_FORMAT
from keys import NEWS_API_KEY


def get_news(country_code='us'):

    response=requests.get(NEWS_API_URL.format(country_code=country_code, api_key=NEWS_API_KEY))

    if response.ok:
        data=response.json()
    else:
        data=None
    return data

def parse_news(news_output=None):

    news_articles=[]

    for article in news_output['articles']:
        source_name=article['source']['name']
        title=article['title']
        description=article['description']

        try:
            news_text= NEWS_FORMAT.format(title=title,body=description,source=source_name)

            news_articles.append(news_text)
        except UnicodeEncodeError:
            pass

    return news_articles

def write_news(article=None, top_x=5):
    with open('article.txt','w') as file:
        for i in range(top_x):
            file.write(articles[i])

if __name__=='__main__':

    news_output = get_news()
    articles=parse_news(news_output)
    write_news(articles)
