from utils.email_cleaner import clean_email_text
import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("PROJECT_NAME")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def fetch_unread_emails():
    try:
        print("Connecting to IMAP...", flush=True)
        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        print("Logged into IMAP", flush=True)
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        print("Inbox selected", flush=True)
        mail.select("inbox")
        
        
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()

        unread_emails = []

        for e_id in email_ids:
            status, msg_data = mail.fetch(e_id, '(RFC822)')
            raw_email = msg_data[0][1]

            msg = email.message_from_bytes(raw_email)

            sender = msg["From"]
            subject = msg["Subject"]

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        except:
                            body = part.get_payload(decode=True).decode("latin-1", errors="ignore")
                        break
            else:
                try:
                    body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
                except:
                    body = msg.get_payload(decode=True).decode("latin-1", errors="ignore")


            cleaned_body = clean_email_text(body)
            unread_emails.append({
                "from": sender,
                "subject": subject,
                "body": cleaned_body
            })

        mail.logout()
        return unread_emails

    except Exception as e:
        print("❌ Error fetching email:", e)
        return []
