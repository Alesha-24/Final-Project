import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from validate_email import validate_email 
from datetime import datetime

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
APP_ENV = os.environ.get("APP_ENV")

from all_news import get_news


def email_validation(email_address):
    '''
    Assesses whether the email address entere by the user is valid
    check_regex will check will the email address has a valid structure and defaults to True
    check_mx: check the mx-records and check whether the email actually exists
    from_address: the email address the probe will be sent from,
    helo_host: the host to use in SMTP HELO when checking for an email,
    smtp_timeout: seconds until SMTP timeout
    dns_timeout: seconds until DNS timeout
    use_blacklist: use the blacklist of domains downloaded from https://github.com/martenson/disposable-email-domains

    Source: https://pypi.org/project/py3-validate-email/

    '''
    is_valid = validate_email(email_address=email_address, check_regex=True, check_mx=True, from_address='my@from.addr.ess', 
    helo_host='my.host.name', smtp_timeout=10, dns_timeout=10, use_blacklist=True)
    return(is_valid) 

def send_email(subject = "Your Daily Briefing from Metanoia", html = "<p>Hello Word </p>"):
    '''
    The purpose of this function is to create an email and send it to the email address entered by the user
    '''
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=email_address, to_emails=email_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None


if __name__ == "__main__":
    if APP_ENV == "development": #if the app is run on the computer it will ask for user input
        print("Welcome to Metanoia. This is a customized news app, where you can get the latest news tailored to your interests and what you care about straight to your inbox!")
        print("---------------------------")
        print("To get started we need some information from you...")
        print("---------------------------")
        name = input("What is your name? ")
        email_address = input(f"Hi {name}! Please input your email address (eg. hello@gmail.com) : ")
        is_valid = email_validation(email_address)
        while is_valid == False:
            print("I'm sorry that appears to be an invalid email address, please try again: ")
            email_address = input("Please input your email address again (eg. hello@gmail.com) : ")
            is_valid = email_validation(email_address)
        source_choices, all_articles,topic, filtered_articles = get_news()
    else:
        print("This app is not configured to run remotely yet")
        #remote configuration coming soon

    def format_articles(all_articles):
        '''
        This function formats the list of article dicitonaries in a more user friendly way
        This new formatting makes the articles easier to read in the email  
        '''
        article_strings = []

        for article in all_articles:
            article_string = f"Article Title: {article['Article Title: ']}, Published At: {article['Published At: ']} \n News Source: {article['News Source: ']}, Article URL: {article['Article URL: ']}"
            article_strings.append(article_string)
        return('\n\n'.join(article_strings))

    subject = "Your Customized Newsletter from Metanoia"
    html = ""

    html += "<h2>You Customized News, brought to you by Metanoia</h2>"

    html += f"<h3>Hi, {name}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{datetime.today().strftime('%A %B %d %Y, %r')}</p>"

    html += "<h4>Your Chosen News Sources: </h4>"
    html += f"<p>{source_choices}</p>"

    html += "<h4>The Top Headlines: </h4>"
    html += f"<p>{format_articles(all_articles)}</p>"

    html += f"<h4>All About {topic.capitalize()}</h4>"
    html += f"<p>{format_articles(filtered_articles)}</p>"

    html += "</ul>"

    
    send_email(subject, html)
    