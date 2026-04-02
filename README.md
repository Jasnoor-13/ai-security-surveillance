# 🚨 AI Surveillance System

An intelligent real-time surveillance system that detects suspicious human behavior like loitering and triggers instant alerts.

---

## 💡 Problem
Traditional CCTV systems are passive — they only help after incidents occur.

---

## 🚀 Solution
We built an AI-powered system that:
- Detects human presence in real time
- Tracks duration of activity
- Identifies suspicious behavior (loitering)
- Triggers instant alerts (visual + sound)
- Displays live monitoring dashboard

---

## 🧠 Features
- 🎥 Real-time video streaming
- 🧍 Person detection using YOLOv8
- ⏱️ Loitering detection (time-based)
- 🚨 Alert system (on-screen + sound)
- 📊 Live dashboard (status + alert count)

---

## 🛠️ Tech Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- FastAPI

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Jasnoor-13/ai-security-surveillance.git
cd ai-security-surveillance
pip install -r requirements.txt
uvicorn main:app --reload

## ⚙️ How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/Jasnoor-13/ai-security-surveillance.git
cd ai-security-surveillance

pip install -r requirements.txt
uvicorn main:app --reload

Open in browser:
👉 http://127.0.0.1:8000/
