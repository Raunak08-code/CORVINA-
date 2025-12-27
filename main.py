from utils.draft_store import save_draft
from utils.draft_store import mark_draft_sent
from utils.draft_store import get_pending_drafts
from utils.ai_responder import generate_ai_reply
from utils.email_reader import fetch_unread_emails
# from utils.draft_store import get_draft, delete_draft
from utils.email_sender import send_email
from pydantic import BaseModel
from fastapi import FastAPI
from utils.email_sender import send_email

app = FastAPI(
    title="CORVINA",
    description="Intelligent Email Understanding and Response System",
    version="1.0.0"
)


class WelcomeEmailRequest(BaseModel):
    email: str
    name: str

#os.getenv("PROJECT_NAME")

@app.post("/email/approve")
def approve_and_send(email_id: str, to_email: str):
    drafts = get_pending_drafts()
    draft = next((d for d in drafts if d["email_id"] == email_id),None)

    if not draft:
        return{"error": "draft Not found"}
    
    send_email(
        to_email=to_email,
        subject=f"Re: {email_id}",
        html_content=draft["draft"]
    )

    mark_draft_sent(email_id)
    return{"status": "EMAIL_SENT"}



@app.get("/email/drafts")
def view_drafts():
    drafts = get_pending_drafts()
    return{"pending_drafts": drafts}



@app.post("/email/ai-draft")
def generate_ai_draft():
    emails = fetch_unread_emails()
    if not emails:
        return {"message": "NO UNREAD EMAILS"}
    
    email = emails[0]
    email_id = email["subject"] #simple id for now..
    ai_reply = generate_ai_reply(email["body"])
        # try:                                                    # from here..,..........
        #     ai_reply = generate_ai_reply(email["body"])
        # except Exception as e:
        #     return {
        #         "error": "AI_REPLY_FAILED",  #//////////trial thing .............
        #         "details": str(e)
        #     }                                 # to here...............

    save_draft(email_id, ai_reply)

    return{
        "status" : "DRAFT_CREATED",
        "email_id": email_id,
        "draft": ai_reply
    }


@app.post("/email/ai-reply")
def ai_reply():
    emails = fetch_unread_emails()

    if not emails:
        return {"message": "No unread emails"}

    latest_email = emails[0]
    user_text = latest_email["body"]

    #print("BEFORE AI CALL", flush=True)
    ai_response = generate_ai_reply(user_text)
    #print("AFTER AI CALL", flush=True)
    
    return {
        "from": latest_email["from"],
        "subject": latest_email["subject"],
        "ai_reply": ai_response
    }


# @app.post("/email/approve")
# def approve_and_send(email_id: str, to_email: str):
#     draft = get_draft(email_id)

#     if not draft:
#         return {"error": "Draft not found"}

#     send_email(
#         to_email=to_email,
#         subject="CORVINA • AI Reply",
#         html_content=draft
#     )

#     delete_draft(email_id)

#     return {"status": "EMAIL_SENT"}




@app.get("/")
def home():
    return {"message": "CORVINA Backend is running!"}

@app.get("/email/read")
def read_email():
    emails = fetch_unread_emails()
    return {"unread_emails": emails}


def generate_welcome_template(name: str):
    return f"""
    <h2>Welcome to CORVINA~, {name}! 🎉</h2>

    <p>We’re excited to have you onboard.</p>

    <p>This is an auto-generated welcome email sent from CORVINA~.</p>

    <p>Feel free to reply — soon, our CORVINA will read and respond automatically!</p>

    <br/>
    <p>— CORVINA~ </p>
    """

@app.post("/email/send-welcome")
def send_welcome_email(request: WelcomeEmailRequest):

    html = generate_welcome_template(request.name)

    send_email(
        to_email=request.email,
    subject="🎉 Welcome to CORVINA~",
        html_content=html
    )

    return {"status": "welcome email sent"}


@app.post("/email/send-test")
def send_test_email():
    html = """
    <h2> Test Email Successful</h2>
    <p>This email was sent from CORVINA~ backend.</p>
    <p><b>THANK YOU</b></p>
    """

    send_email(
        to_email="praunak8105@gmail.com",
        subject="CORVINA ~ Intelligent Email System",
        html_content=html
    )

    return {"status": "email sent"}
