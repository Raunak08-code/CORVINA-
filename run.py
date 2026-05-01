import os
from core.email_reader import fetch_emails
from core.parser import parse_email
from core.rule_engine import get_reply_templates
from core.email_sender import send_email
from core.logger import get_logger

logger = get_logger()

emails = fetch_emails()

for e in emails:

    # safty check -->  very import to not reply its self it will couse infinite self loop 
    if e["from"] == os.getenv("EMAIL_USER"):
        continue

    parsed = parse_email(e)
    reply = get_reply_templates(parsed["intent"])

    logger.info(f"Processing email from {e.get('from')}")
    logger.info(f"Intent detected: {parsed['intent']}")

    success = send_email(
        to_email = e["from"],
        subject = e["subject"],
        body = reply
    )

    if success:
        logger.info(f"Reply seccessfully processed for {e['from']}")
    else:
        logger.error(f"Failed to process email for {e['from']}")
