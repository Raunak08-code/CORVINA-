import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, body):
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))

    try:
        # creating a message 
        msg = MIMEText(body)
        msg["Subject"] = f"Re: {subject}"
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        # connecting to smtp server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)


        # sending mail
        server.sendmail(EMAIL_USER, to_email, msg.as_string())

        server.quit()

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f" Failed to send email: {e}")
    
