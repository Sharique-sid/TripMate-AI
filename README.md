<div align="center">
  <h1>🌍 TripMate AI</h1>
  <p><strong>Autonomous Multi-Agent Orchestration Platform for Travel Planning</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python Version" />
    <img src="https://img.shields.io/badge/FastAPI-0.103+-009688.svg" alt="FastAPI" />
    <img src="https://img.shields.io/badge/LangGraph-AI-orange.svg" alt="LangGraph" />
    <img src="https://img.shields.io/badge/PostgreSQL-Supabase-green.svg" alt="PostgreSQL" />
  </p>
</div>

---

## 🚀 Overview
**TripMate AI** is a production-grade multi-agent system designed to synthesize complex, dynamic travel itineraries. Built on **LangGraph** and exposed via a non-blocking **FastAPI** backend, the platform leverages a Supervisor routing architecture to delegate tasks to specialized AI agents.

### ✨ Key Features
* 🤖 **Multi-Agent Orchestration**: A central Supervisor agent seamlessly coordinates specialized worker agents (e.g., Weather MCP, Search) to gather context and build itineraries.
* 🛑 **Human-In-The-Loop (HITL)**: Integrated state checkpoints using PostgreSQL (via Supabase) allow users to intercept AI drafts, inject feedback, and force revisions *before* the final generation, drastically reducing LLM hallucination and saving tokens.
* 🛡️ **Input Guardrails**: Prevents prompt injection and off-topic requests (e.g., "Write me a poem") using pre-computation validation nodes.
* 🌐 **Model Context Protocol (MCP)**: Features a custom MCP weather server, demonstrating extensibility for enterprise data adapters.
* 💎 **Glassmorphism UI**: A sleek, custom-designed frontend connected to asynchronous FastAPI endpoints.

---

## 🏗️ Architecture

1. **Supervisor Node**: Evaluates user intent and routes the query to either the validation node, the planning node, or external MCP tools.
2. **State Management**: LangGraph's `AsyncPostgresSaver` persists the thread state to a remote PostgreSQL database, allowing for asynchronous HITL interruptions.
3. **Frontend Integration**: An asynchronous API (`/api/travel` and `/api/travel/approve`) handles long-running LLM streams without blocking the main event loop.

---

## 🛠️ Tech Stack
* **Core**: Python, FastAPI, Uvicorn
* **AI/LLM**: LangChain, LangGraph, Groq, Tavily
* **Database**: PostgreSQL (Supabase) for Checkpoint Memory
* **Extensibility**: Model Context Protocol (MCP)
* **Frontend**: HTML5, Vanilla JavaScript, Custom CSS (Glassmorphism)
* **Deployment**: Docker, Render

---

## 💻 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sharique-sid/TripMate-AI.git
   cd TripMate-AI
   ```

2. **Set up environment variables**  
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_key
   TAVILY_API_KEY=your_key
   DATABASE_URL=postgresql://user:password@host:port/db
   ```

3. **Run with Docker**
   ```bash
   docker build -t tripmate-ai .
   docker run -p 8000:8000 --env-file .env tripmate-ai
   ```

4. **Access the application**
   Navigate to `http://localhost:8000` in your browser.

---

## 👤 Author
**Sharique Hussain**  
*Full Stack & AI Engineer*  
[LinkedIn](https://linkedin.com/in/sharique-hussain-a21ab1283/) | [GitHub](https://github.com/Sharique-sid)
