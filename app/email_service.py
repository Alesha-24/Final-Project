import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from validate_email import validate_email 
from datetime import datetime

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
APP_ENV = os.environ.get("APP_ENV")


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
        email_address = input("Please input your email address (eg. hello@gmail.com) : ")
        is_valid = email_validation(email_address)
        while is_valid == False:
            print("I'm sorry that appears to be an invalid email address, please try again: ")
            email_address = input("Please input your email address again (eg. hello@gmail.com) : ")
            is_valid = email_validation(email_address)
    else:
        print("HI")

    subject = "Floof delivery order"
    html = f"""
    <h3> Floof delivery order </h3>
    <h4> 5th May 2020 </h4>
    <p> One floof delivered to 3700 Ost NW, Washington DC.  </p>
    <p> Please hurry floof needed ASAP.  </p>
    """
    send_email(subject, html)
    