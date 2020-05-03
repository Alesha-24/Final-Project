import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint

load_dotenv()

API_KEY = os.environ.get("NYT_API")


def get_articles_1():
    #request_url = f"http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_prog/amazon.json?fields=all&api-key={API_KEY}"
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:("Environment")&api-key={API_KEY}'
    response = requests.get(request_url)
    #print(response.text)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #print(parsed_response.keys())
    all_articles = parsed_response["response"]["docs"]
    for x in all_articles:
        print(x["headline"]["main"])
        print(x["pub_date"])
        print(x["abstract"])
        print(x["web_url"])
get_articles_1()

  