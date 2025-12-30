# 👶 Nurtura – AI Parental Care Chatbot

Nurtura is an AI-powered parental care chatbot designed to support parents with
practical advice, emotional reassurance, and child development guidance.
The chatbot is built using Python and integrates Google Gemini API for intelligent responses.

---

## 🚀 Features
- AI-based parenting advice
- Natural language conversation
- Secure API key handling using environment variables
- Simple and clean web interface

---

## 🛠 Tech Stack
- Python
- Google Gemini API
- Flask
- HTML, CSS

---

## 📂 Project Structure
parental-chatbot/
│── app.py
│── chatter.py
│── templates/
│── static/
│── README.md
│── .gitignore


---

## ▶️ How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/divyaa12345/parental-chatbot.git
cd parental-chatbot

2.Create virtual environment
python -m venv venv
venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4.Create a .env file and add:
GEMINI_API_KEY=your_api_key_here

5.Run the application
python app.py
