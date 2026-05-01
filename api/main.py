from fastapi import FastAPI
from core.email_reader import fetch_emails
from core.parser import parse_email
from core.rule_engine import get_reply_templates
from core.email_sender import send_email
from core.logger import get_logger
import os

app = FastAPI()
logger = get_logger()

@app.get("/")
def root():
    return {"message": "CORVINA API is running"}

@app.get("/process-emails")
def process_email():
    emails = fetch_emails()
    results = []

    for e in emails:
        # skip self mail
        if e.get("from") == os.getenv("EMAIL_USER"):
            continue

        parsed = parse_email(e)
        reply = get_reply_templates(parsed["intent"])

        success = send_email(
            to_email=e["from"],
            subject=e["subject"],
            body=reply
        )

        results.append({
            "from": e["from"],
            "intent": parsed["intent"],
            "status": "sent" if success else "failed"
        })

    return {"processed": results}