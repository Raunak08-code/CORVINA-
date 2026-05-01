import re 

def clean_text(text):
    if not isinstance(text, str):
        return ""
    import re
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()


def parse_email(email):
    raw_body = email.get("body", "")

    # SAFETY CHECK
    if not isinstance(raw_body, str):
        raw_body = ""

    text = clean_text(raw_body)

    keywords = []

    if "internship" in text:
        keywords.append("internship")
    if "meeting" in text:
        keywords.append("meeting")

    # intent checking
    if "internship" in text or "job" in text:
        intent = "job_request"
    elif "meeting" in text or "schedule" in text:
        intent = "meeting"
    else:
        intent = "general"

    return {
        "clean_text": text,
        "keywords": keywords,
        "intent": intent
    }

