# 🧠 AI Multi-Agent Stock Analysis & Trading System

## 📌 Summary

This project is an AI-powered multi-agent stock analysis platform that uses collaborative AI agents to analyze real-time market data and generate Buy, Sell, or Hold recommendations. It integrates CrewAI with live financial data and provides an interactive Streamlit web interface for user interaction.

---

## 🛠️ Technologies Used

* Python
* CrewAI (Multi-Agent Framework)
* LLM Integration (Groq / LiteLLM)
* Yahoo Finance API (yfinance)
* Streamlit (Web Interface)
* dotenv (Environment Variables)
* Object-Oriented Programming (OOP)
* Modular Architecture

---

## ✨ Features

* Real-time stock market analysis
* Multi-agent collaboration workflow
* Financial analyst agent for insights
* Trader agent for decision-making
* Automated Buy / Sell / Hold recommendations
* Interactive Streamlit user interface
* Live data integration using Yahoo Finance
* Scalable modular project structure

---

## ⌨️ Keyboard Shortcuts

```
Ctrl + C   → Stop application
Enter      → Submit command
R          → Refresh Streamlit app
```

---

## ⚙️ Process

```
1. User enters a stock symbol in the Streamlit interface
2. Analyst Agent fetches real-time stock data
3. Analyst performs market analysis
4. Trader Agent evaluates the analysis
5. System generates Buy / Sell / Hold recommendation
6. Results are displayed in the web dashboard
```

---

## 🏗️ How I Built It

```
- Designed modular multi-agent architecture using CrewAI
- Created Analyst and Trader agents with defined responsibilities
- Implemented task pipeline for agent communication
- Integrated real-time stock data via Yahoo Finance API
- Connected LLM reasoning using LiteLLM / Groq
- Built interactive frontend using Streamlit
- Structured project into agents, tasks, and tools folders
```

---

## 📚 What I Learned

```
- Multi-agent AI system design
- CrewAI framework implementation
- LLM integration and prompt engineering
- Streamlit web app development
- Real-time API data handling
- Workflow automation between AI agents
- Modular Python project structuring
```

---

## 🚀 How It Could Be Improved

```
- Add historical price prediction models
- Portfolio optimization and risk analysis
- Sentiment analysis using news data
- Brokerage API integration for automated trading
- Advanced UI dashboards and charts
- Additional specialized AI agents
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Multi-Agent-Stock-Analysis-Trading-System.git
cd AI-Multi-Agent-Stock-Analysis-Trading-System
```

### Create Virtual Environment

```bash
python -m venv crewai-env
crewai-env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Environment Variables (.env)

```
GROQ_API_KEY=your_api_key_here
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
AI-Multi-Agent-Stock-Analysis-Trading-System/
│
├── streamlit_app.py      # Streamlit interface
├── main.py               # Core execution logic
├── crew.py               # Crew workflow
│
├── agents/
│   ├── analyst_agent.py
│   └── trader_agent.py
│
├── tasks/
│   ├── analyse_task.py
│   └── trade_task.py
│
├── tools/
│   └── stock_research_tool.py
│
├── .env
└── README.md
```

---

## ⭐ About

An AI-powered multi-agent stock analysis system with a Streamlit interface that analyzes real-time market data and provides Buy/Sell/Hold trading recommendations using collaborative AI agents built with CrewAI.
