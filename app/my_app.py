import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint

load_dotenv()

API_KEY = os.environ.get("NYT_API")

#add in error detection for user input 

def get_articles_1():
#printing articles from 2012, only 4 printing - but attributes printing correctly 
    #request_url = f"http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_prog/amazon.json?fields=all&api-key={API_KEY}"
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:("Environment")&api-key={API_KEY}'
    response = requests.get(request_url)
    #print(response.text)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #print(parsed_response.keys())
    all_articles = parsed_response["response"]["docs"]
    print(parsed_response["response"]["meta"]["hits"])
    for x in all_articles:
        print(x["headline"]["main"])
        print(x["pub_date"]) #change to viewer friendly 
        print(x["abstract"])
        print(x["web_url"])
#get_articles_1()

print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about!")
print("---------------------------")
print("To get started we need some information from you...")
print("---------------------------")
name = input("What is your name? ")
topic = input(f"Hi {name}! Please input a topic you want to learn more about: ")
print("---------------------------")
print("Please wait, aggregating data...")

def get_articles_2():
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&fq=2020&api-key={API_KEY}'
    response = requests.get(request_url)
    #print(response.text)
    parsed_response = json.loads(response.text)
    #print(parsed_response["status"])
    all_articles = parsed_response["response"]["docs"]
    print(parsed_response["response"]["meta"]["hits"])
    hits = (parsed_response["response"]["meta"]["hits"])
    if int(hits) == 0:
        print("I'm sorry, your search returned 0 results, please ensure to enter your topic of interest carefully!")     
    print(f"Your search returned {hits} hits on the New York Times")
    # print(parsed_response)
    for x in all_articles:
        print(x["headline"]["main"])
        print(x["pub_date"])
        print(x["abstract"])
        print(x["web_url"])
get_articles_2()

# refine = input("Would you like to filter this search further? Please answer yes or no: ")
# if refine == "yes" or "Yes":
#     topic2 = input("Please enter a few more keywords to refine this search: ")
#     request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}AND{topic2}&api-key={API_KEY}'
#     response = requests.get(request_url)
#     print(response.text)
#     parsed_response = json.loads(response.text)
#     all_articles = parsed_response["response"]["docs"]
#     hits = (parsed_response["response"]["meta"]["hits"])
#     print(f"Your search returned {hits} hits on the New York Times")
#     for x in all_articles:
#         print(x["headline"]["main"])
#         print(x["pub_date"])
#         print(x["abstract"])
#         print(x["web_url"])
# if refine == "no" or "No":
#     print("Thank you for using Metanoia")
# else:
#     print("Error. Please enter either yes or no to continue: ")
