
import pytest 
import os 
# from all_news import 
from NYT_news import date_validation 

# CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, source: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
# @pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

#url testing by ensuring code = 200

def date_validation_test():
    months = {'01': 31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31,'11':30, '12':31, 'leap':29 }
    date = "2020040q"
    assert date_validation(date, months) == False
    date = "202004091"
    assert date_validation(date, months) == False
    date = "20200431"
    assert date_validation(date, months) == False
    date = "2020029"
    assert date_validation(date, months) == True
    


