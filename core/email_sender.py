import smtplib
import os
import time
from email.mime.text import MIMEText
from dotenv import load_dotenv
from core.logger import get_logger

logger = get_logger()

load_dotenv()

def send_email(to_email, subject, body, max_retries=3, delay=2):
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    #SMTP_SERVER = "wrong.smtp.server"  # only for testing
    SMTP_PORT = int(os.getenv("SMTP_PORT"))

    for attempt in range(1,max_retries+1):
        try:
            # creating a message 
            msg = MIMEText(body)
            msg["Subject"] = f"Re: {subject}"
            msg["From"] = EMAIL_USER
            msg["To"] = to_email

            # connecting to SMTP server
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)

            # sending mail
            server.sendmail(EMAIL_USER, to_email, msg.as_string())
            server.quit()
            
            logger.info(f"Email sent to {to_email} on attempt {attempt}")
            return True

        except Exception as e:
            logger.error(f"Attempt {attempt} failed for {to_email}: {e}")

            if attempt < max_retries:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error(f"All retry attempts failed for {to_email}")
                return False
