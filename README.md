# 🤖 AI Desktop Assistant (Voice + LLM + Python)

A Personal AI Desktop Assistant built from scratch using Python, Whisper (Speech-to-Text), LLM, and AI Agent architecture.

This project demonstrates how to build a real Voice AI Assistant that can listen, understand, decide, and act.

---

## 🚀 Features

- 🎤 Speech-to-Text using Whisper
- 🔊 Text-to-Speech with Neural Voice
- 🧠 LLM-based Intent Classification
- 🛠 Tool-based AI Agent Architecture
- 🖥 Open Applications (Spotify, YouTube, etc.)
- 🐞 Debug Python Errors
- ⚡ Command Execution with Approval
- 🔁 Multi-step Interaction Handling
- 🧩 Modular Project Structure

---

## 🏗 Project Architecture


User Voice
↓
Speech-to-Text (Whisper)
↓
Intent Router (LLM)
↓
Tool Selection
↓
Tool Execution
↓
Text-to-Speech


---

## 📂 Project Structure


AI-desktop-assistant/
│
├── main.py
├── super_agent.py
│
├── tools/
│ ├── chat_tool.py
│ ├── command_tool.py
│ ├── debug_tool.py
│ ├── system_tool.py
│
├── voice/
│ ├── speech_to_text.py
│ ├── text_to_speech.py
│
├── utils/
│ └── llm.py
│
└── .env


---

## ⚙️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/vikas-m-sharma/AI-desktop-assistant.git
cd AI-desktop-assistant

2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Add your API key in .env

GROQ_API_KEY=your_api_key_here
▶️ Run the Assistant
python main.py
🧠 What You Learn From This Project

How AI Agents work

How LLM intent routing works

How to structure scalable AI systems

How to integrate tools with AI

How to handle multi-step conversations

Real-world AI architecture design

🎯 Ideal For

Python Developers

AI / ML Students

Developers building Voice AI systems

Anyone who wants to build a JARVIS-like assistant

⚠️ Note

Never upload your .env file or API keys to GitHub.

📌 Author

Vikas Sharma
YouTube: Code2Faith


---

# 🔥 Also Create requirements.txt

Run:

```bash
pip freeze > requirements.txt

Then commit:

git add .
git commit -m "Added README and requirements"
git push
