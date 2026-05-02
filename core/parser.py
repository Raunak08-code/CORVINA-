import re 
from core.logger import get_logger

logger = get_logger()

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()


def parse_email(email):
    body = email.get("body", "")

    # checking  condition if body is empty
    if not isinstance(body, str) or not body.strip():
        logger.warning("Empty email body detected, skipping processing")
        return {
            "clean_text": "",
            "keywords": [],
            "intent": "general"
        }

    # cleaning the exts
    text = clean_text(body)

    # checking for keywords
    keywords = []
    if "internship" in text:
        keywords.append("internship")
    if "meeting" in text:
        keywords.append("meeting")
    if "leave" in text:
        keywords.append("leave")
    if "issue" in text:
        keywords.append("issue")
    if "information" in text:
        keywords.append("information")

    if not keywords:
        logger.warning("NO keyword detected, defaulting to general intent")

    # cecking for intent
    if "internship" in text or "job" in text:
        intent = "job_request"

    elif "meeting" in text or "schedule" in text:
        intent = "meeting"

    elif "leave" in text or "vacation" in text or "sick" in text:
        intent = "leave_request"

    elif "issue" in text or "error" in text or "problem" in text:
        intent = "support_issue"

    elif "information" in text or "details" in text or "query" in text:
        intent = "request_info"

    else:
        intent = "general"

    # adding into logs
    logger.info(f"Parsed intent: {intent}")

    return {
        "clean_text": text,
        "keywords": keywords,
        "intent": intent
    }