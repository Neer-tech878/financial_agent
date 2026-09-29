# 💸 AI-Quant Financial Research Agent

[![Powered by PhiData](https://img.shields.io/badge/Framework-PhiData-blue)](https://www.phidata.com/)
[![Model-Groq](https://img.shields.io/badge/Model-Groq%20GPT--OSS--120B-orange)](https://groq.com/)
[![Data-YFinance](https://img.shields.io/badge/Data-YFinance-green)](#)
[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B)](https://agent-financial.streamlit.app/)

## 🌐 Live Demo
> **Try it now → [https://agent-financial.streamlit.app/](https://agent-financial.streamlit.app/)**

A high-frequency financial intelligence agent that combines real-time market data with web-based sentiment analysis. Built to bypass manual research gaps and provide immediate, data-driven **Buy / Hold / Sell** signals using **Groq's GPT-OSS-120B** model.

---

## 🚀 The Mission
Modern stock analysis is fragmented between fundamental data (YFinance) and live market news (DuckDuckGo). This agent bridges that gap by executing multi-step workflows to summarize analyst recommendations, track stock fundamentals, and analyze market sentiment — all in a single execution.

## 🧠 Core Intelligence
- **Real-Time Fundamentals:** Fetches stock prices, analyst ratings, and company health metrics via `YFinance`
- **Global Web Research:** Scrapes news and sentiment from the web using `DuckDuckGo`
- **Groq GPT-OSS-120B:** High-speed inference via Groq's LPUs for near-instant reasoning
- **Visual Reporting:** Outputs structured tables and formatted Markdown with clear sources and units

## 🛠️ Stack Components
| Component | Technology |
|-----------|-----------|
| Orchestration | [PhiData](https://github.com/phidatahq/phidata) |
| LLM Engine | Groq (`openai/gpt-oss-120b`) |
| Market Data | YFinanceTools |
| Web Search | DuckDuckGo |
| UI | Streamlit |
| Deployment | Streamlit Cloud |

---

## ⚡ Quick Start (Local)

### 1. Clone & Setup
```bash
git clone https://github.com/Neer-tech878/financial_agent.git
cd financial_agent
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free Groq API key at [console.groq.com/keys](https://console.groq.com/keys)

### 3. Run the Agent (CLI)
```bash
python financial_agent.py
```

### 4. Run the Playground UI (local)
```bash
python playground.py
```

---

## ☁️ Deploying to Streamlit Cloud

This app is deployed at **[https://agent-financial.streamlit.app/](https://agent-financial.streamlit.app/)**

### How it was deployed:
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Connect your GitHub repo → set **Main file** to `financial_agent.py`
4. Go to **Settings → Secrets** and add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
5. Click **Deploy** — Streamlit auto-redeploys on every `git push`

> ⚠️ **Never commit your `.env` file.** Use Streamlit Secrets for cloud deployments.

---

## 📊 Sample Workflow
By default, the agent is configured to analyze **NVIDIA (NVDA)** and **Cisco (CSCO)**, comparing their fundamentals and analyst sentiment to generate a unified recommendation score.

**Example output:**
| Stock | Recommendation | P/E | Analyst Buy% |
|-------|---------------|-----|-------------|
| NVIDIA (NVDA) | ✅ **BUY** | ~15 | 95% |
| Cisco (CSCO) | ⏸️ **HOLD** | ~19 | 68% |

---

*Created by [Neer-tech878](https://github.com/Neer-tech878)*
