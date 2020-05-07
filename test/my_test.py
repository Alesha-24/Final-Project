
import pytest 
import os 
import requests
import json  

from app.NYT_news import date_validation, process_request, get_articles_1 
#from app.email_service import email_validation, send_email
from app.all_news import sources

CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, source: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
@pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

def test_get_articles_1():
    topic = "happiness"
    API_KEY = os.environ.get("NYT_API")
    response_status = get_articles_1(topic).status_code
    assert response_status == 200


def test_date_validation():
    '''
    This test ensures that the date validation function is working
    It first test whether the function successfully verifies that the input if fully numeric
    It then tests whether the function successfully verifies that the date is 8 digits long
    It then tests whether a valid date was entered - ie. 29th February 2020 is valid because 2020 is a leap year
    '''
    months = {'01': 31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31,'11':30, '12':31, 'leap':29 }
    date = "2020040q"
    assert date_validation(date, months) == False
    date = "202004091"
    assert date_validation(date, months) == False
    date = "20200431"
    assert date_validation(date, months) == False
    date = "20200229"
    assert date_validation(date, months) == True

# def test_email_validation():
#     email_address = "alesha@gmial.com"
#     assert email_validation(email_address) == False 
#     email_address = "alesha.com" 
#     assert email_validation(email_address) == False
#     email_address = "aig31@georgetown.edu"
#     assert email_validation(email_address) == True

def test_process_request():
    parsed_response  = json.dumps({'status': 'OK', 'copyright': 'Copyright', 
    'response': {'docs': [{'abstract': "Is python the best coding language.", 'web_url': "https://www.georgetown.edu"}], 
    'meta': {'hits': 3012482, 'offset': 0, 'time': 1076}}})
    hits, all_articles = process_request(parsed_response)
    assert hits == 3012482
    assert all_articles == [{'abstract': "Is python the best coding language.", 'web_url': "https://www.georgetown.edu"}]

def test_sources():
    all_sources = [{'id': 'abc-news', 'name': 'ABC News', 'country': 'us'}, {'id': 'bbc-news', 'name': 'BBC News', 'country': 'en'}]
    assert sources(all_sources) == ['abc-news', 'bbc-news']
