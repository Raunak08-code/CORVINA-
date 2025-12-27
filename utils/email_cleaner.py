import re
from bs4 import BeautifulSoup

def clean_email_text(raw_text: str) -> str:
    if not raw_text:
        return ""

    text = raw_text

    # Remove forwarded / replied text
    reply_patterns = [
        r"On .* wrote:",
        r"From:.*",
        r"Sent:.*",
        r"To:.*",
        r"Subject:.*"
    ]

    for pattern in reply_patterns:
        text = re.split(pattern, text, flags=re.IGNORECASE)[0]

    # Remove quoted lines (>)
    text = "\n".join(
        line for line in text.splitlines()
        if not line.strip().startswith(">")
    )

    # Remove email signatures
    signature_patterns = [
        r"--\s*\n.*",
        r"Thanks[,\s]*\n.*",
        r"Regards[,\s]*\n.*",
        r"Best[,\s]*\n.*"
    ]

    for pattern in signature_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)

    # Remove HTML if any
    if "<" in text and ">" in text:
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text()

    # Clean extra spaces
    text = re.sub(r"\n{2,}", "\n", text)
    text = text.strip()

    return text
