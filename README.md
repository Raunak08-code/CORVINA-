# 🐦‍⬛ CORVINA — Intelligent Email Automation System

> CORVINA is a production-ready backend system that automatically reads emails, understands intent, generates responses, and sends replies — deployed as a cloud API.

---

## 🚀 Overview

CORVINA is designed as a **real-world backend automation system**, not a simple script.

It integrates:

* Email processing (IMAP)
* Intelligent parsing (rule-based NLP)
* Automated response generation
* Cloud deployment via Docker + Render

👉 Fully accessible as a **public API**

---

## 🌐 Live API

**Base URL:**
https://corvina-mnb3.onrender.com/

**Swagger Docs:**
https://corvina-mnb3.onrender.com/docs

---

## 🧪 Live Demo (Try It Yourself)

You can test CORVINA in real-time:

### 📩 Step 1 — Send Email

Send an email to:
**[corvina.system@gmail.com](mailto:corvina.system@gmail.com)**

Example:

* Subject: Internship Opportunity
* Body: I am looking for an internship

---

### ⚙️ Step 2 — Trigger Processing

Open:
https://corvina-mnb3.onrender.com/docs

Run endpoint:
**GET /process-emails**

---

### 📤 Step 3 — Get Response

* Email will be processed
* Reply will be sent automatically
* Email will be marked as read

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

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| GET    | `/`               | Health check          |
| GET    | `/process-emails` | Process unread emails |

---

## 🧪 Testing Scenarios Covered

* ✔️ Internship request → correct reply
* ✔️ Meeting request → correct reply
* ✔️ Leave request → handled
* ✔️ General email → default response
* ✔️ Empty email → safely handled
* ✔️ SMTP failure → retry triggered
* ✔️ No unread emails → handled gracefully

---

## 🐳 Docker Usage

### Build Image

docker build -t corvina .

### Run Container

docker run -p 8000:8000 --env-file .env corvina

---

## ☁️ Deployment

* Containerized using Docker
* Hosted on Render
* Environment variables securely managed
* Public API accessible globally

---

## 📂 Project Structure

<pre>
corvina/
├── api/
│   └── main.py
├── core/
│   ├── email_reader.py
│   ├── parser.py
│   ├── rule_engine.py
│   ├── email_sender.py
│   ├── logger.py
├── config/
│   └── rules.json
├── templates/
│   ├── internship_reply.txt
│   ├── meeting_reply.txt
│   ├── support_reply.txt
│   ├── info_reply.txt
│   ├── leave_reply.txt
│   └── default.txt
├── logs/
│   └── app.log
├── run.py
├── requirements.txt
├── Dockerfile
└── .env.example
</pre>

---

## 🔐 Environment Variables

1. EMAIL_USER=[your_email@gmail.com](mailto:your_email@gmail.com)
2. EMAIL_PASS=your_app_password
3. IMAP_SERVER=imap.gmail.com
4. SMTP_SERVER=smtp.gmail.com
5. SMTP_PORT=587

---

## ⚙️ Local Setup

git clone <your-repo-link>
cd corvina

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

# Add credentials

python run.py

---

## 🌍 Run API Locally

uvicorn api.main:app --reload

Open:
http://127.0.0.1:8000/docs

---

## 📈 What This Project Demonstrates

* Backend system design (modular architecture)
* Email automation using IMAP & SMTP
* API development using FastAPI
* Logging and retry mechanisms
* Secure environment configuration
* Docker containerization
* Cloud deployment (Render)
* End-to-end production workflow

---

## 🚧 Future Improvements

* AI-based intent detection (fallback system)
* Database for storing email history
* Queue system (Redis/Celery)
* Authentication & rate limiting
* Frontend dashboard

---

## 👤 Author

**Raunak Pandey**
Backend & AI Systems Developer

Built CORVINA as a production-grade system to simulate real-world backend automation pipelines.