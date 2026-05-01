import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv
from email.utils import parseaddr
from core.logger import get_logger

load_dotenv()
logger = get_logger()

def clean_text(text):
    return text.replace("\r", "").replace("\n", " ").strip()


def fetch_emails():
    emails_data = []

    # Load credentials
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    IMAP_SERVER = os.getenv("IMAP_SERVER")

    try:
        # Connect to server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        # Search for unread emails
        status, messages = mail.search(None, "UNSEEN")

        email_ids = messages[0].split() if messages and messages[0] else []

        for e_id in email_ids:
            res, msg_data = mail.fetch(e_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decode subject
                    subject = msg.get("Subject", "")
                    if subject:
                        subject, encoding = decode_header(subject)[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding if encoding else "utf-8", errors="ignore")
                    else:
                        subject = ""

                    # Get sender
                    sender = parseaddr(msg.get("From"))[1]

                    # Extract body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                payload = part.get_payload(decode=True)
                                if payload:
                                    body = payload.decode(errors="ignore")
                                    break
                    else:
                        payload = msg.get_payload(decode=True)
                        if payload:
                            body = payload.decode(errors="ignore")
                    

                    if not isinstance(body, str):
                        body = ""
                    
                    if not body.strip():
                        continue

                    logger.info(f"Fetched email from {sender} with subject '{subject}'")
                    
                    # adding date
                    date = msg.get("Date")

                    email_obj = {
                        "from": sender ,
                        "subject": clean_text(subject),
                        "body": clean_text(body),
                        "date": date
                    }

                    emails_data.append(email_obj)

        mail.logout()

    except Exception as e:
        logger.error(f"Error fetching emails: {e}")

    
    return emails_data