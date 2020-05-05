import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint
from datetime import datetime


load_dotenv()
from app import APP_ENV

API_KEY = os.environ.get("NEWS_API")
    
print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about!")
print("---------------------------")
print("To get started we need some information from you...")
print("---------------------------")
name = input("What is your name? ")
topic = input(f"Hi {name}! With Metanoia you can get your news from any website you would like. Below are the sources you can choose from: ")

sources_url = (f"https://newsapi.org/v2/sources?apiKey={API_KEY}")
response = requests.get(sources_url)
sources = json.loads(response.text)
#print(sources)
#print(sources.keys())
all_sources = sources["sources"]
list_of_sources = []
for x in all_sources:
    print(x["name"])
    list_of_sources.append(x["name"])
print(list_of_sources)

url = (f"http://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
#response = requests.get(url)
#print(json.loads(response.text))

#add filter for:
#country
#category
#language??

#url resting by ensuring code = 200

#key words in title 

