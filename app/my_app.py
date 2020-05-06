import os
import json 
import requests
from dotenv import load_dotenv
#from pprint import pprint
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NYT_API")
months = {'01': 31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31,'11':30, '12':31, 'leap':29 }

def get_articles_1():
    request_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&fq=&facet=true&sort=newest&api-key={API_KEY}'
    response = requests.get(request_url)
    return response 

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

def date_validation(date, months):
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
                        print("Please ensure you enter a valid day")
            else:
                print("Please ensure the year you have entered is not in the future!")
        else:
            print("Please ensure you enter a date that is eight digits in length!") 
    else:
        print("Please ensure you are inputting only numeric values")
    return correct 

if __name__ == "__main__":

    print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about!")
    print("---------------------------")
    print("To get started we need some information from you...")
    print("---------------------------")
    name = input("What is your name? ")
    topic = input(f"Hi {name}! Please input a topic you want to search the New York Times for: ")
    print("The search results will automatically return the most recent articles relevant to your chosen topic.") 
    #mention that it'll come up with articles that list the keywords - or find way to better filter
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
    
    #this should only run if in development mode - in product mode, just return latest news - ie 2020
    date_filter = input("You can filter your results by date of publishing. Please enter 'yes' if you would like to filter the results by date, otherwise enter 'no': ")
    while date_filter == "Yes" or "yes":
        print("Please format your dates in the following format YYYYMMDD, so for example: 24th August 2019 = 20190824")
        print("---------------------------")
        begin_date = input("Please enter a start date: ")
        end_date = input("Please enter an end date: ")
        if begin_date > end_date:
            print("Error! Please ensure that your start date is before the end date you enter.")
            date_filter = "Yes"
        elif begin_date <= end_date:
            correct = date_validation(begin_date,months) 
            while correct == False:
                begin_date =input("Error! Please enter a valid date: ")
                correct = date_validation(begin_date, months)
            correct = date_validation(begin_date,months) 
            while correct == False:
                end_date =input("Error! Please enter a valid date: ")
                correct = date_validation(end_date, months)
            print("---------------------------")
            print("Please wait, filtering results...")
            response = get_articles_2()
            _, all_articles = process_request(response)
            for x in all_articles:
                print(x["headline"]["main"])
                print(x["pub_date"])
                print(x["abstract"])
                print(x["web_url"])
            date_filter = "No"
            break
    #this should only run if its in development mode not production mode 
    if date_filter == "No" or "no":
        print("We hope you found that interesting!")
        keep_going = input("Would you like to search the news for another topic that you're interested? Please enter 'yes' or 'no': ")
        # if keep_going == "yes" or "Yes":
            
        # else:
        #     print("Thank you for using Metanoia!")

    #to do:
    #put whole thing in while loop to run again
    





