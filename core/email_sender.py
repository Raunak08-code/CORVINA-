import smtplib
import os
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    try:
        EMAIL_USER = os.getenv("EMAIL_USER")
        EMAIL_PASS = os.getenv("EMAIL_PASS")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(EMAIL_USER, EMAIL_PASS)

        server.send_message(msg)

        server.quit()

        print("EMAIL SENT SUCCESSFULLY")

        return True

    except Exception as e:
        print("SMTP ERROR:", str(e))
        return False