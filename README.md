# Metanoia - Customized News
## Alesha Gulamhusein - OPIM 244: Final Project 

The purposed of this README.md file is to help you install and use this customized news service. 

## Functionality 
A signifcant problem faced by many consumers today is action paralysis as a result of either information overload or lack of access to the right information. This often leaves people misinformed and making decisions based on heurestics rather than facts. 

Therefore this software, called Metanoia, is designed to give people the information they want at their finger tips. 

There are two ways to use this software; the NYT_news file allows you to search the New York Times (NYT) specfically for information you are interested in, while the all_news file allows you to search a combindation of websites for information and then send this information to you directly in an email.

The set-up for both uses is the same, but the rest of the README.md file will be distinguish the information inputs and outpbuts by these two functionalities. 

## Setup

Fork this repositry from GitHub and clone it to a convenient location on your local computer (for example your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/Final-Project/
```

Create and activate a new Anaconda virtual environment, perhaps named "final-project-env":

```sh
conda create -n final-project-env python=3.7 #(first time only)
conda activate final-project-env
```

Then, from within the virtual environment, install the necessary package dependencies:

```sh
pip install -r requirements.txt

```

## API Keys
In order to successfully gather real time news  the program will need two API Keys, one from the NYT and another News API Key.

You can obtain the NYT key by visitng the link below: 
https://developer.nytimes.com/get-started

For contect, this software uses the Article Search API key from the NYT

You can obtain the second API key by visiting the link below:
https://newsapi.org

Once you have done this, please create a ".env" file in the root directory of the project repository. Then enter both API Keys as environment variables as shown below. 

```sh
NYT_API = "abc123"

NEWS_API = "xyz456"

```

### Securing your credentials 

In order to ensure that your API keys remain secret and are not invluded in the source code or its revision history, please ensure to create a ".gitignore" file in the root directory of oyur repository. Then in the git ignore file place the following code inside:

``` sh
.env
```

### Information Input 
The system will first prompt you to input a stock symbol (e.g. "TSLA", "MSFT", "C", etc.). It will then prompt you to input your risk tolerance, either LOW, MEDIUM or HIGH, for investing that particular stock in order to generate a tailored reccommendation. The system will allow you to generate a reccomendation for multiple stock tickers at once - however please note that it will produce the reccomendation for each stock before prompting you to enter additional stock tickers. When you are finished entering data please type 'DONE'.

### Data Validation 
So as to ensure to provide you with the most accurate information the system also has a built-in two step data validation process which verifies that there is available for the stock ticker entered. 

### Information Output 
The program provide ouptut in three forms. 

First it will print out summary statistics of the stock along with a reccomendation as to whether or not to buy it and justification for that reccomendation. The reccomendation will be based upon two calculations; the frist will compare the latest closing price to the lowest price over the past 100 days, the second will compare the latest closing price to the average closing price over the past 52-weeks. The first calculation will vary depending on the risk level you entered for the stock, such that a greater level of risk averseness will require greater capital gains for the reccomendation to be in favour of buying the stock. 

```sh
-------------------------
SELECTED TICKER:  AAPL
-------------------------
REQUESTING STOCK MARKET DATA...
REQUEST AT:  2020 / 2 / 24    21 : 45
-------------------------
LATEST DAY:  2020-02-24
LATEST CLOSE:  $298.18
52 WEEK AVERAGE CLOSE: $232.64
100 DAY HIGH:  $327.85
52 WEEK HIGH: $327.85
100 DAY LOW:  $215.13
52 WEEK LOW: $169.50
-------------------------
RECOMMENDATION: BUY / DON'T BUY
RECOMMENDATION REASON: (REASON)
```

The second form of output will be a CSV file that has record historical stock data for the past 100 days. Each stock that you choose to analyse will have a unique CSV file that will be named with the stock ticker symbol and stored in the data folder within the project repository.

The third form of output will be a line graph that displays the trend in your chosen stock's closing price over the last 100 days. 

## Project Set Up
Use GitHub.com to first fork and then download or 'clone' the project repository onto your computer.  It is helpful to choose an easily accessible download location like the Desktop.  


After cloning the repository you can then use GitHub Desktop Software to access  the project repository or naivagte their using the command-line below:

```sh
 cd ~/Desktop/robo-adivsor/app
```


## Environment Set Up

Create and activate a new Anaconda virtual environment:

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```
From within the virtual environment install the required packages specfied in the requirements.txt file in the repository using the code below. 
```sh
pip install -r requirements.txt
```

From within this virtual environment, you can then run the Python script from the command-line:

```sh
python robo_advisor.py
```