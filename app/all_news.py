import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NEWS_API")

def get_sources():
    '''
    This function retrieves all available sources using the NewsAPI key by issuing a get request
    It then uses json to process this data into a useable format
    '''
    sources_url = (f"https://newsapi.org/v2/sources?apiKey={API_KEY}")
    response = requests.get(sources_url)
    sources = json.loads(response.text)
    return sources

def get_articles(url_sources):
    '''
    This function retrieves news from the selected sources using the NewsAPI key by issuing a get request
    It then uses json to process this data into a useable format
    '''
    url = f"http://newsapi.org/v2/everything?sources={url_sources}&language=en&pagesize=5&apiKey={API_KEY}"
    response = requests.get(url)
    news = json.loads(response.text)
    return news

def aggregate_articles(articles):
    article_list = []
    for x in articles:
        article = {"Article Title: ": x["title"]
                ,"Published At: ": x["publishedAt"][0:10]
                ,"News Source: ": x["source"]["name"]
                ,"Article URL: ": x["url"]}
        article_list.append(article)
    return(article_list)

def sources(all_sources):
    list_of_sources = []
    for x in all_sources:
        print(x["id"])
        list_of_sources.append(x["id"])
    return list_of_sources

def get_filtered_articles(url_sources,topic):
    #searches for the user's topic in the title of the article only 
    filtered_url = f"https://newsapi.org/v2/everything?sources={url_sources}&qInTitle={topic}&language=en&pagesize=7&apiKey={API_KEY}"
    response = requests.get(filtered_url)
    filtered_news = json.loads(response.text)
    return filtered_news


def get_news():
    topic = input(f"With Metanoia you can get your news from any website you would like. Press enter to continue and you will see below the sources you can choose from... ")
    print("---------------------------")
    sources = get_sources()
    print("From the list above you may select a maximum of 20 sources you would like to get your news from.")
    print("Type in the name of each source one at a time and ensure to include the hyphen(-) in the name.")
    print("---------------------------")
    all_sources = sources["sources"]
    list_of_sources = sources(all_sources)
    source_choice = ""
    source_choices = []
    while source_choice != "DONE":
        source_choice = input("Please enter the name of a source, otherwise enter 'DONE': ")
        if source_choice.lower() not in list_of_sources and source_choice.lower() != "done":
        #validating whether the user entered one of the given sources
            print("Error! That seems to be an invalid source")
        elif source_choice.lower() in list_of_sources:
            source_choices.append(source_choice)
    if source_choice == "DONE":
        url_sources = ", ".join(source_choices)
        news = get_articles(url_sources)
        articles = (news["articles"])
        hits = (news["totalResults"])
        print("---------------------------")
        print(f"Your search returned {hits} results!")
        print("---------------------------")
        all_articles = aggregate_articles(articles)

    print("You can further filter your news by topics that interest you.")
    topic = input("Please enter a topic: ")
    filtered_news = get_filtered_articles(url_sources, topic)
    more_articles = (filtered_news["articles"])
    hits_filtered = (filtered_news["totalResults"])
    if hits_filtered == 0:
        #refines the search further to return some resutls the user
        #searches for the topic in the body of the articles and title
        filtered_url = f"https://newsapi.org/v2/everything?sources={url_sources}&q={topic}&language=en&pagesize=7&apiKey={API_KEY}"
        response = requests.get(filtered_url)
        filtered_news = json.loads(response.text)
        hits_filtered = (filtered_news["totalResults"])
        more_articles = (filtered_news["articles"])
    print(f"Your search returned {hits_filtered} results!")
    filtered_articles = aggregate_articles(more_articles)
    print("---------------------------")
    print("Please wait while we send all these articles to your inbox!")
    print("---------------------------")
    print("Thank you for using Metanoia!")
    return source_choices, all_articles, topic, filtered_articles
     

if __name__ == "__main__":
    get_news()