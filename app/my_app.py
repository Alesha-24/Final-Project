import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NYT_API")

#add in error detection for user input 


def get_articles_1():
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&facet=true&sort=newest&api-key={API_KEY}'
    response = requests.get(request_url)
    return response 
    # #print(response.text)
    # parsed_response = json.loads(response.text)
    # #print(parsed_response["status"])
    # all_articles = parsed_response["response"]["docs"]
    # #print(parsed_response["response"]["meta"]["hits"])
    # hits = (parsed_response["response"]["meta"]["hits"])
    # print(f"Your search returned {hits} hits on the New York Times")
    # return(hits, all_articles)

# def get_articles_2():
#     request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&facet=true&begin_date={begin_date}&end_date={end_date}&api-key={API_KEY}'
#     response = requests.get(request_url)
#     parsed_response = json.loads(response.text)
#     all_articles = parsed_response["response"]["docs"]
#     hits = (parsed_response["response"]["meta"]["hits"])
#     print(f"Your search returned {hits} hits on the New York Times")
#     return(all_articles)

def get_articles_2():
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&facet=true&begin_date={begin_date}&end_date={end_date}&api-key={API_KEY}'
    response = requests.get(request_url)
    return response 

def process_request(response):
    parsed_response = json.loads(response.text)
    all_articles = parsed_response["response"]["docs"]
    hits = (parsed_response["response"]["meta"]["hits"])
    print(f"Your search returned {hits} hits on the New York Times")
    return(hits, all_articles)

print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about!")
print("---------------------------")
print("To get started we need some information from you...")
print("---------------------------")
name = input("What is your name? ")
topic = input(f"Hi {name}! Please input a topic you want to learn more about: ")
print("The search results will automatically return the most recent articles relevant to your chosen topic.") 
print("---------------------------")
print("Please wait, aggregating data...")

response = get_articles_1()
hits, all_articles = process_request(response)

while hits == 0:
    print("I'm sorry, your search returned 0 results, please ensure to enter your topic of interest carefully!")  
    topic = input("PLease input a topic you want to learn more about: ")   
    print("---------------------------")
    print("Please wait, aggregating data...")
    hits, all_articles = get_articles_1()

#put this in a function 
for x in all_articles:
    print(x["headline"]["main"])
    print(x["pub_date"])
    print(x["abstract"])
    print(x["web_url"])

date_filter = input("You can filter your results by date of publishing. Please enter 'yes' if you would like to filter the results by date, otherwise enter 'no': ")
if date_filter == "Yes" or "yes":
    print("Please format your dates in the following format YYYYMMDD, so for example: 24th August 2019 = 20190824")
    print("---------------------------")
    begin_date = input("Please enter a start date: ")
    end_date = input("Please enter an end date: ")
    if begin_date > end_date:
        print("Error! Please ensure that your start date is before the end date you enter.")
        #code must stop here or loop back to start 
    #how to catch error if date doesn't exist
    print("---------------------------")
    print("Please wait, filtering results...")
    response = get_articles_2()
    _, all_articles = process_request(response)
    for x in all_articles:
        print(x["headline"]["main"])
        print(x["pub_date"])
        print(x["abstract"])
        print(x["web_url"])
elif date_filter == "No" or "no":
    print("Cheers mate") #something happens here 


# refine = input("Would you like to filter this search further? Please answer yes or no: ")
# if refine == "yes" or "Yes":
#     topic2 = input("Please enter a few more keywords to refine this search: ")
#     request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic,topic2}&fq=2020&api-key={API_KEY}'
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
