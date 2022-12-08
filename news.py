from newsapi import NewsApiClient
import requests

URL = ('https://newsapi.org/v2/top-headlines?')
API_KEY = '********************'  # Keys Redacted
ClientAPI_Key = '***************************'

#Init
newsapi = NewsApiClient(api_key = 'f75****************')
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
    q='etherium',
    sources='bbc-news, the-verge',
    category='business',
    language='en',
    country='us')
# /v2/everything
all_articles = newsapi.get_everything(
    q='bitcoin',
    sources='bbc-news,the-verge',
    domains='bbc.co.uk,techcrunch.com',
    from_param='2017-12-01',
    to='2017-12-12',
    language='en',
    sort_by='relevancy',
    page=2)
# /v2/top-headlines/sources
sources = newsapi.get_sources()

def get_articals_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters) 

# Specific Query by search string
def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

# HTTP Request with requests library
def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    result = []

    for article in articles:
        results.append({"titles": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')


if __name__ == "__main__":
   """  print(f"Getting news from {argv[1]}...\n")
    get_articals_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines") """