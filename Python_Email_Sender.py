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
email_Subject = "Request for Meeting to Discuss Collaboration Opportunities"
email_Body = (
    "Dear Figures,\n\n"
    "I hope this message finds you well.\n\n"
    "My name is Rivers, and I am the Chief Engineer at GO_IT Solutions. I am reaching out to explore potential "
    "opportunities for collaboration between our organizations. We believe that working together could bring mutual "
    "benefits and help us achieve shared objectives.\n\n"
    "I would appreciate the opportunity to schedule a brief meeting at your convenience to discuss this further. "
    "Please let me know your availability, and I will do my best to accommodate.\n\n"
    "Thank you for your time and consideration. I look forward to your response.\n\n"
    "Best regards,\n"
    "Rivers\n"
    "Chief Engineer\n"
    "GO_IT Solutions\n"
    "000-000-0000\n"
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
send_email(email_Sender, email_Password,email_Receiver, email_Subject, email_Body)


