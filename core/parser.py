import re 
from core.logger import get_logger

logger = get_logger()

def clean_text(text):
    if not isinstance(text, str):
        return ""
    import re
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()


def parse_email(email):
    if not email.get("body"):
        logger.warning("empty email body detected")
        return {
            "clean_text": "",
            "keywords": [],
            "intent": "general"
        }
    
    raw_body = email.get("body", "")

    # SAFETY CHECK
    if not isinstance(raw_body, str):
        raw_body = ""

    # cheaning the text from any special character 
    text = clean_text(raw_body)

    # getting keywords..
    keywords = []
    if "internship" in text:
        keywords.append("internship")
    if "meeting" in text:
        keywords.append("meeting")

    if not keywords:
        logger.warning("NO keyword detected, defaulting to general intent")

    # intent checking
    if "internship" in text or "job" in text:
        intent = "job_request"
    elif "meeting" in text or "schedule" in text:
        intent = "meeting"
    else:
        intent = "general"

    # imputing into logger file
    logger.info(f"Parsed intent: {intent}")

    return {
        "clean_text": text,
        "keywords": keywords,
        "intent": intent
    }

