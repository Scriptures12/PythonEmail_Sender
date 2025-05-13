from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level = logging.INFO)

# Set up the email parameters and get environment vaariables
email_Sender = os.getenv("EMAIL_SENDER")
email_Password = os.getenv("EMAIL_PASSWORD")    
email_Receiver = os.getenv("EMAIL_RECIEVER")

# validate environment variables
if not email_Sender or not email_Password or not email_Receiver:
    logging.error("Missing environment variables: EMAIL_SENDER, EMAIL_PASSOWRD"
    "or EMAIL_RECIEVER. please check your .env file")

# Set up email content
email_Subject = "Don\'t forget to subscribe!"
email_Body = (
    "Hello, \n\n"
    "I hope this email finds you well. I wanted to take a moment to remind you to "
    "subscribe to my YouTube channel if you haven't already. Your support means a lot to me and helps me continue creating content.\n\n"
    "Thank you for your time and support!\n\n"
    "Best regards,\n"
    "Linkage Upwards\n\n"
)

# Function to send email
def send_email(Sender, Password, Receiver, Subject, Body):
    em = EmailMessage()
    em['From'] = Sender
    em['TO'] = Receiver
    em['Subject'] = Subject
    em.set_content(Body)

# Create a secure SSL context
context = ssl.create_default_context()
try:
    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(Sender, Password)
        smtp.sendmail(Sender, Receiver, em.as_string())
        logging.info("Email sent successfully!")
except Exception as e:
    logging.error(f"Failed to send email: {e}")

# Call the function to send the email
send_email(email_Sender, email_Receiver, email_Subject, email_Body)


