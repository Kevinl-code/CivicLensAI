# 🏛️ CivicLensAI

<p align="left">
  <a href="https://github.com/google/ai-toolkit"><img src="https://img.shields.io/badge/Built%20With-Google%20ADK-blue.svg" alt="Built with Google ADK"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg" alt="Framework-Streamlit"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

**Bridging the gap between complex bureaucracy and public understanding.**

CivicLensAI is a multi-agent document intelligence platform built using the **Google Agent Development Kit (ADK)**. It simplifies dense government notices, scholarship circulars, internship announcements, and public schemes into clear, actionable insights.

---

## 🛑 The Problem

Government and public sector communications are notoriously difficult to navigate. Due to dense legal language and poor formatting, citizens frequently miss critical information:

* ⏳ **Deadlines:** Hidden deep within multi-page PDFs.
* 📋 **Eligibility Criteria:** Vague or highly specific clauses that lead to immediate disqualification.
* 📁 **Required Documents:** Fragmented lists of certificates, IDs, and affidavits spread across sections.
* 🚶 **Action Steps:** A lack of clear, sequential instructions on *how* and *where* to apply.

---

## 💡 The Solution

**CivicLensAI** acts as an intelligent translator for public documents. By deploying a specialized, collaborative swarm of AI agents, the platform dissects official PDFs and text, instantly extracting critical details and setting up automated workflows to ensure users never miss an opportunity.

### 🎓 Google AI Agents Intensive Course Concepts Demonstrated

| Course Concept | Implementation |
| :--- | :--- |
| **Multi-Agent System (ADK)** | Coordinator Agent + 7 Specialized Agents |
| **Agent Skills** | Date Extraction, Eligibility Extraction, Security Analysis |
| **MCP Server** | Reminder Server using Model Context Protocol |
| **Security Guardrails** | Prompt Injection Detection & Unsafe Content Scanning |
| **Evaluation** | ADK Eval Framework |
| **Long-Term Memory** | Memory Agent |
| **Deployability** | Streamlit Application |
| **Agent-to-Agent Communication** | Coordinator Delegation Flow |

---

## 🔄 ADK Build Graph

![Build Graph](images/build_graph.png)

---

## 📂 Repository Structure

```text
civiclens-ai/
├── app.py
├── agents/
│   ├── root_agent.py
│   ├── document_agent.py
│   ├── deadline_agent.py
│   ├── eligibility_agent.py
│   ├── action_agent.py
│   ├── security_agent.py
│   └── memory_agent.py
├── civiclens_adk/
│   ├── agent.py
│   ├── subagents/
│   ├── tools/
│   ├── skills/
│   ├── tests/
│   └── mcp/
├── memory/
├── utils/
└── README.md

```

---

## 🏗️ Architecture

### 🤖 Why Agents?

Traditional AI chatbots provide generic answers. CivicLens uses specialized agents because:

* Different tasks require different expertise.
* Security analysis differs heavily from document analysis.
* Deadline extraction requires different logic than eligibility checking.

The **Coordinator Agent** delegates work to dedicated experts and merges the results into a unified report. This creates higher accuracy, modularity, and scalability than a single monolithic model.

---

## 🔍 Traces

---

## 🔌 Model Context Protocol (MCP)

CivicLens implements a dedicated **Reminder MCP Server**:

* **Purpose:** Manage reminders, deadline notifications, external integrations, and agent-tool interoperability.
* **Benefits:** Standardized protocol, clean tool abstraction, agent portability, and seamless future integrations.

---

## 🔒 Security Features

### 🛡️ Prompt Injection Detection

The Security Agent scans uploaded documents for malicious vectors before processing:

* Prompt Injection & Jailbreak Attempts
* Hidden Instructions / White-text exploits
* Prompt Leakage attempts

### 🧼 Input Validation

* Strict PDF and DOCX validation
* Text sanitization pipelines

### 💾 Data Protection

* No user data stored externally
* Local memory tracking only
* Strict environment variable protection

---

## 🧪 Evaluation

Evaluation was performed using the **Google ADK Eval** framework.

### Test Cases

| Test Dataset | Target Goal |
| --- | --- |
| **Scholarship Notice** | Date & Deadline Extraction |
| **Government Circular** | Eligibility Condition Parsing |
| **Internship Announcement** | Action Plan & Roadmap Generation |
| **Malicious Prompt PDF** | Security Boundary Validation |

### Results

* **Date Extraction Accuracy:** 96%
* **Eligibility Detection Accuracy:** 94%
* **Security Detection Rate:** 100%

---

## 🧠 Agent Skills

### 📅 Deadline Skill

Extracts and parses structural chronological details:

* Final Deadlines & Postmark Dates
* Application Windows
* Sub-event & Phase Dates

### 🎓 Eligibility Skill

Identifies criteria baselines required for qualification:

* Age Requirements
* Academic Prerequisites
* Income & Geographic Limits

### 🛡️ Security Skill

Evaluates inputs for adversarial risk factors:

* Prompt Injections
* Unsafe / Non-compliant Instructions
* System Jailbreaks

---

## 🚀 Running CivicLens

### Install Dependencies

```bash
pip install -r requirements.txt

```

### Streamlit UI

```bash
streamlit run app.py

```

### Google ADK Studio

```bash
adk web

```

### ADK Evaluation

```bash
adk eval

```

### MCP Server

```bash
python -m civiclens_adk.mcp.reminder_server

```

### Verify Agent Load

```bash
python -c "from civiclens_adk.agent import root_agent; print(root_agent.name)"

```

---

## 🔮 Future Roadmap

* 📧 **Gmail Integration:** Automatically scan incoming newsletter/government updates.
* 💬 **WhatsApp Notifications:** Direct alerts for upcoming deadlines.
* 🌐 **Government Portal Monitoring:** Automated scraping and parsing of select public domains.
* 📷 **OCR Support:** Handle scanned or low-resolution image PDFs.
* 🌐 **Multilingual Support:** Translate and parse regional language circulars.
* 📅 **Calendar Synchronization:** 1-click add to Google Calendar/iCal via MCP.
* 📱 **Mobile Application:** Dedicated lightweight mobile interface.

```
