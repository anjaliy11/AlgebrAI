## 🧮 AlgebrAI — AI-Powered Algebra Learning Assistant



![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Framework-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Framework-0B5FFF)
![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-orange)
[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?logo=streamlit)](https://algebrai-ikmdmzjwiwdldpnssu2ez6.streamlit.app/)
![Build](https://img.shields.io/badge/Build-Stable-success)
![License](https://img.shields.io/badge/License-MIT-green)


## ✨ Overview

AlgebrAI is a modern AI-powered web application designed to help users solve and understand algebraic problems in a clear and structured way.

The application converts natural language math queries into accurate solutions, providing either:

a final numeric answer, or

a fully explained step-by-step solution, depending on user preference.

Built using Streamlit, LangChain, and Groq LLMs, AlgebrAI is fast, interactive, and beginner-friendly.

---

## 🚀 Features

 AI-powered algebra problem solving

 Step-by-step mathematical reasoning

 Toggleable explanation mode

 Ultra-fast LLM inference with Groq

 Clean Streamlit chat-based interface

 ---
 
 ## Tech Stack

 | Layer          | Technology       |
| -------------- | ---------------- |
| Frontend       | Streamlit        |
| Backend        | Python           |
| LLM Framework  | LangChain        |
| Model Provider | Groq (LLaMA 3.x) |
| Deployment     | Streamlit Cloud  |

---
## Project Structure

algebrai/
│
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .env.example        # Environment variables template

---

 ## ⚙️ Installation & Local Setup
1️⃣ Clone the Repository

git clone https://github.com/anjaliy11/AlgebrAI.git

cd AlgebrAI

---

## 2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

source venv/bin/activate   # Windows: venv\Scripts\activate

---

## 3️⃣ Install Dependencies

pip install -r requirements.txt

---



##  🔑 Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key

---

## ▶️ Run the Application
streamlit run app.py


📍 App will be available at:

http://localhost:8501

