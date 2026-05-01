import json
import os
from datetime import datetime

DRAFT_FILE = "drafts.json"

def save_draft(email_id: str, draft_text: str):
    draft = {
        "email_id": email_id,
        "draft": draft_text,
        "status": "PENDING",
        "created_at": datetime.utcnow().isoformat()
    }

    drafts = []
    if os.path.exists(DRAFT_FILE):
        with open(DRAFT_FILE, "r") as f:
            drafts = json.load(f)

    drafts.append(draft)

    with open(DRAFT_FILE, "w") as f:
        json.dump(drafts, f, indent=2)

def get_pending_drafts():
    if not os.path.exists(DRAFT_FILE):
        return []
    with open(DRAFT_FILE, "r") as f:
        drafts = json.load(f)
    return [d for d in drafts if d["status"] == "PENDING"]

def mark_draft_sent(email_id: str):
    if not os.path.exists(DRAFT_FILE):
        return

    with open(DRAFT_FILE, "r") as f:
        drafts = json.load(f)

    for d in drafts:
        if d["email_id"] == email_id:
            d["status"] = "SENT"

    with open(DRAFT_FILE, "w") as f:
        json.dump(drafts, f, indent=2)
