import os
from core.email_reader import fetch_emails
from core.parser import parse_email
from core.rule_engine import get_reply_templates
from core.email_sender import send_email

emails = fetch_emails()

for e in emails:
    print("RAW EMAIL:", e)
    print("-------")

    # safty check -->  very import to not reply its self it will couse infinite self loop 
    if e["from"] == os.getenv("EMAIL_USER"):
        print("Skipping self email...")
        continue

    parsed = parse_email(e)

    print("PARSED:")
    print(parsed)

    reply = get_reply_templates(parsed["intent"])

    print("SENDING REPLY...")

    send_email(
        to_email = e["from"],
        subject = e["subject"],
        body = reply
    )

    print("===============")