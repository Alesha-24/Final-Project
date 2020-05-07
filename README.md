# Metanoia - Customized News
## Alesha Gulamhusein - OPIM 244: Final Project 

The purposed of this README.md file is to help you install and use this customized news service. 

## Functionality 
A significant problem faced by many consumers today is action paralysis as a result of either information overload or lack of access to the right information. This often leaves people misinformed and making decisions based on heuristics rather than facts. 

Therefore this software, called Metanoia, is designed to give people the information they want at their fingertips. 

There are two ways to use this software; the "NYT_news" file allows you to search the New York Times (NYT) specifically for information you are interested in, while the "all_news" file allows you to search a combination of websites for information and then send this information to you directly in an email.

The set-up for both uses is the same, but the rest of the README.md file will be distinguish the information inputs and outputs by these two functionalities. 

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

## New York Times News
This file allows you to search the NYT for specifc topics and filter oyour search by date. 
### Information Input 

The system will first prompt you to enter your name and then a topic that you want to search the New York Times for. For example if you're itnerested in cliamte change oyu can type that in when prompted. It will then ask you if you want to narrow your search results by date, allowing to search for information from a specifc time frame. For example if you searched for cliamte change but wnat to learn more about the infamous and horrifying IPCC report that was release in 2001, you can narrow you search to only articles produced in 2001. The program will ask you to enter a start date and an end date in the format 20200406 (6th April 2020). Please ensure that the start date is before the end date.

The system will allow you to search for multiple topics however please note that it will show the search results for one topic before prompting you to enter and additional one.

### Data Validation 
So as to ensure to provide you with the most accurate information the system also has built-in data validation processes. The first verifies the topic oyu entered - such that if the get request generates 0 hits it recognizes there is like to have been a typo and prompts you to input a topic again. The second data validation is for the dates entered; the system will check first whether the date entered is all numeric, then it verifies that it is eight digits long, it then checks whether the date entered exists (for example if you enter 31st of April 2020 it will sned a message saying this date doesn't exist)

### Information Output 
First the program will print out the number of hits your search returned, so you can get an idea of the amount of information that exists for your specfic search. Then it  prints out the 10 most relevant articles for you search. It prints the heading of the article prints, the date it was published, a summary of the article and the url so you can copy it into your browser and read the full article should you so choose.  

### Running the file 
In order to run this file copy and past the following into the command line. 
```sh

python app/NYT_news.py

```
## All News 
This file allows you to search tons of different news sites from all over the world. 

### Information Input 

The system will first prompt you to enter your name and email address. It then displays all the available sources you can search and will prompt you to choose upto 20 news sites. It will then ask if you want to further filter your news search by topic, and you can enter any topic you like. 

### Data Validation 
This file also has system also has built-in data validation processes. The  verifies the sources you choose, such that if the sources entered are not in the given list it prompts you to reenter the source.

### Information Output 
The program will return two sets of output. First it will return seven top articles from your chosen news sources. You can edit the numbner of articles returned by editting the url. Where it says 'pagesize=7', as shown in the URL below, you can edit this to range to any number between 1-50, depnding on how many articles you chooose

``` sh
filtered_url = f"https://newsapi.org/v2/everything?sources={url_sources}&qInTitle={topic}&language=en&pagesize=7&apiKey={API_KEY}"
```

Then the program will return the seven most relevant articles to your selected topic from your chosen sources. Again, as above you can edit the number of articles dispalyed by changing the appropriate URL. 

In order to provide users with most relevant information the program first search for the keyword in article titles. However, if no resutls are found it then searches for the keyword in the body and title of an article to optimize the search for the user.

Finally the program will aggregate all this information and send you an email to your entered address containing the headlines, news sources and URLs for each of the articles the search returned. 


### Running the file 
In order to run this file copy and past the following into the command line. 
```sh

python app/all_news.py

```
## Testing

The software also has built in testing, which is also run remotely on the Travis CI server when the repository is updated. 
In order to run the tests on your local computer ensure that you have first activated a virtual environment and installed the "requirements.txt" file as mentioned above because this contains the pytest package. 

Then from the command line simply run the code below:

``` sh 
pytest
```