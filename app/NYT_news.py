import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NYT_API")
months = {'01': 31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31,'11':30, '12':31, 'leap':29 }

def get_articles_1(topic):
    '''
    This function retrieves articles from the NYT by issuing a get request
    '''
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&fq=&facet=true&sort=newest&api-key={API_KEY}'
    response = requests.get(request_url)
    return response 

def get_articles_2(topic, begin_date, end_date):
    '''
    This function retrieves articles from the NYT within a specifc timeframe by issuing a get request
    '''
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&facet=true&begin_date={begin_date}&end_date={end_date}&api-key={API_KEY}'
    response = requests.get(request_url)
    return response 

def process_request(response):
    try:
        parsed_response = json.loads(response.text)
    except:
        parsed_response = json.loads(response)
    all_articles = parsed_response["response"]["docs"]
    hits = (parsed_response["response"]["meta"]["hits"])
    print(f"Your search returned {hits} hits on the New York Times")
    return(hits, all_articles)

def date_validation(date, months):
    '''
    This function validates the dates entered by the user - extremely improtant to ensure the url is valid and the get request is successful
    It first check whether all values in the date are numeric
    It then checks if the date is eight digits long
    It then makes sure the date entered is before the current date
    It then ensures the date entered is valid so a user can't input the 31st of APril because this date doens't exist
    It also accounts for leap years by calcualting whether or not hte entered year is a leap year
     
    '''
    correct = False 
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    leap = False
    if date.isnumeric():
        if len(str(date)) == 8:
            if (datetime.now().year) >= int(year):
                if month == '02':
                    if int(year) % 4 == 0:
                        leap = True
                        if int(year) % 100 == 0:
                            if int(year) % 400 != 0:
                                leap = False 
                    if leap == True:
                        days = months['leap']  
                        if int(day) <= days:
                            correct = True
                    else:
                        days = months[month]
                        if int(day) <= days:
                            correct = True 
                elif int(month) <= 12:
                    days = months[month]
                    if int(day) <= days:
                        correct = True 
                    else:
                        print("Error! Please ensure you enter a day that exists!")
                else:
                    print("Error! PLease ensure you enter a month that exists!")
            else:
                print("Error! Please ensure the year you have entered is not in the future!")
        else:
            print("Error! Please ensure you enter a date that is eight digits in length!") 
    else:
        print("Error! Please ensure you are inputting only numeric values!")
    return correct 

def run_code():
    topic = input("Please input a topic you want to search the New York Times for: ")
    print("The search results will automatically return the most recent articles that contain your chosen topic within the body of the article.") 
    print("---------------------------")
    print("Please wait, aggregating data...")

    response = get_articles_1(topic)
    hits, all_articles = process_request(response)

    while hits == 0:
        print("I'm sorry, your search returned 0 results, please ensure to enter your topic of interest carefully!")  
        topic = input("PLease input a topic you want to learn more about: ")   
        print("---------------------------")
        print("Please wait, aggregating data...")
        hits, all_articles = get_articles_1(topic)

    #put this in a function 
    for x in all_articles:
        print("Article Title: ", x["headline"]["main"])
        print("Published At: ", x["pub_date"][0:10])
        print("Abstract: ", x["abstract"])
        print("URL: ", x["web_url"])
        print("---------------------------")
    
    date_filter = input("You can filter your results by date of publishing. Please enter 'yes' if you would like to filter the results by date, otherwise enter 'no': ")
    print(date_filter)
    while date_filter.lower() == "yes":
        print("Please format your dates in the following format YYYYMMDD, so for example: 24th August 2019 = 20190824")
        print("---------------------------")
        begin_date = input("Please enter a start date: ")
        correct = date_validation(begin_date,months) 
        while correct == False:
            begin_date =input("Please enter a valid begin date: ")
            correct = date_validation(begin_date, months)
        end_date = input("Please enter an end date: ")
        correct = date_validation(end_date,months) 
        while correct == False:
            end_date =input("Please enter a valid end date: ")
            correct = date_validation(end_date, months)
        if int(begin_date) > int(end_date):
            print("Error! Please ensure that your start date is before the end date you enter.")
            date_filter = "Yes"
        elif begin_date <= end_date:
            print("---------------------------")
            print("Please wait, filtering results...")
            response = get_articles_2(topic, begin_date, end_date)
            _, all_articles = process_request(response)
            for x in all_articles:
                print("Article Title: ", x["headline"]["main"])
                print("Published At: ", x["pub_date"][0:10])
                print("Abstract: ", x["abstract"])
                print("URL: ", x["web_url"])
                print("---------------------------")
            date_filter = "No"
            break
    
    if date_filter.lower() == "no":
        print("We hope you found that interesting!")
    
    
if __name__ == "__main__":

    print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about!")
    print("---------------------------")
    print("To get started we need some information from you...")
    print("---------------------------")
    name = input("What is your name? ")
    print(f"Hi {name}!")
    
    run_code()
    keep_going = input("Would you like to search the news for another topic that you're interested? Please enter 'YES' or 'NO': ")
    while keep_going.lower() == "yes":
        run_code()
        keep_going = input("Would you like to search the news for another topic that you're interested? Please enter 'YES' or 'NO': ")
    print("Thank you for using Metanoia!")
    





