# 🐦‍⬛ CORVINA — Intelligent Email Automation System

> CORVINA is a production-ready backend system that automatically reads emails, understands intent, generates responses, and sends replies — deployed as a cloud API.

---

## 🚀 Overview

CORVINA is designed as a **real-world backend automation system**, not a simple script.

It integrates:
- Email processing (IMAP)
- Intelligent parsing (rule-based NLP)
- Automated response generation
- Cloud deployment via Docker + Render

👉 Fully accessible as a **public API**

---

## 🌐 Live API

Base URL:
https://corvina-mnb3.onrender.com/

swagger Docs:
https://corvina-mnb3.onrender.com/docs

---

## 🧪 Live Demo (Try It Yourself)

You can test CORVINA in real-time:

### 📩 Step 1 — Send Email
Send an email to: corvina.system@gmail.com


Example:
- Subject: Internship Opportunity  
- Body: I am looking for an internship  

---

### ⚙️ Step 2 — Trigger Processing

Open Swagger:   https://corvina-mnb3.onrender.com/docs

Run endpoint:   GET /process-emails

---

### 📤 Step 3 — Get Response

- Email will be processed  
- Reply will be sent automatically  
- Email will be marked as read

---

## 🧠 Key Features

* 📥 Fetch unread emails using IMAP
* 🧹 Clean and normalize email content
* 🧠 Rule-based intent detection (internship, meeting, leave, etc.)
* 📄 Template-driven response system
* 📤 Automated email replies via SMTP
* 🔁 Retry mechanism for failed email sending
* 🪵 Structured logging system
* 🌐 REST API using FastAPI
* 🐳 Dockerized for portability
* ☁️ Deployed on Render (public API)

---

## 🏗️ System Architecture

```
Gmail Inbox
    ↓ (IMAP)
Email Reader
    ↓
Parser (clean + intent detection)
    ↓
Rule Engine (decision logic)
    ↓
Template Generator
    ↓
Email Sender (SMTP)
    ↓
Recipient Inbox
```

---

## 🔁 Execution Flow

1. Fetch unread emails from inbox  
2. Parse and clean email content  
3. Detect intent using rule-based logic  
4. Select response template  
5. Send automated reply via SMTP  
6. Log success/failure with retry mechanism

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|--------|-------------|
| GET | `/` | Health check |
| GET | `/process-emails` | Process unread emails |

---

## 🧪 Testing Scenarios Covered

✔️ Internship request → correct reply  
✔️ Meeting request → correct reply  
✔️ Leave request → handled  
✔️ General email → default response  
✔️ Empty email → safely handled  
✔️ SMTP failure → retry triggered  
✔️ No unread emails → handled gracefully  

---

## 🐳 Docker Usage

### Build Image
```bash
docker build -t corvina .

Run COntainer  : docker run -p 8000:8000 --env-file .env corvina

---

## ☁️ Deployment

Containerized using Docker
Hosted on Render
Environment variables securely managed
Public API accessible globally

## 🎥 Demo

Example:

Input Email:
"Looking for internship"

System Output:
- Intent detected: job_request
- Response sent automatically

---

## 📂 Project Structure

```
corvina/
├── api/
│   └── main.py
│
├── core/
│   ├── email_reader.py
│   ├── parser.py
│   ├── rule_engine.py
│   ├── email_sender.py
│   ├── logger.py
│
├── config/
│   └── rules.json
│
├── templates/
│   ├── internship_reply.txt
│   ├── meeting_reply.txt
│   ├── leave_reply.txt
│   └── support_reply.txt
├   └── info_reply.txt
│   └── default.txt
│
├── logs/
│   └── app.log
│
├── run.py
├── requirements.txt
├── Dockerfile
└── .env.example
```

---

## ⚙️ Setup (Local)

```bash
# Clone repo
git clone <your-repo-link>
cd corvina

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add environment variables
cp .env.example .env
# Fill credentials

# Run system
python run.py

# Run API locally
uvicorn api.amin:app --reload

# Open
http://127.0.0.1:8000/docs
```

---

## 🔐 Environment Variables

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
IMAP_SERVER=imap.gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

## 📈 What This Project Demonstrates

Backend system design (modular architecture)
Email automation using IMAP & SMTP
API development using FastAPI
Logging and retry mechanisms
Secure environment configuration
Docker containerization
Cloud deployment (Render)
End-to-end production workflow

---

## 🚧 Future Improvements

AI-based intent detection (fallback system)
Database for storing email history
Queue system (Redis/Celery)
Authentication & rate limiting
Frontend dashboard

---

## 👤 Author

**Raunak Pandey**
Backend & AI Systems Developer

Built CORVINA as a production-grade system to simulate real-world backend automation pipelines.
