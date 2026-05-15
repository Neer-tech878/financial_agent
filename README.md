# 💸 AI-Quant Financial Research Agent

[![Powered by PhiData](https://img.shields.io/badge/Framework-PhiData-blue)](https://www.phidata.com/)
[![Model-Groq](https://img.shields.io/badge/Model-Groq--Llama3.1-orange)](https://groq.com/)
[![Intel-YFinance](https://img.shields.io/badge/Data-YFinance-green)](#)

A high-frequency financial intelligence agent that combines real-time market data with web-based sentiment analysis. Built to bypass manual research gaps and provide immediate, data-driven "Buy/Hold/Sell" signals using **Llama 3.1** via **Groq**.

## 🚀 The Mission
Modern stock analysis is fragmented between fundamental data (YFinance) and live market news (DuckDuckGo). This agent bridges that gap by executing multi-step workflows to summarize analyst recommendations, track stock fundamentals, and analyze market sentiment—all in a single execution.

## 🧠 Core Intelligence
- **Real-Time Fundamentals:** Fetches stock prices, analyst ratings, and company health metrics via `YFinance`.
- **Global Web Research:** Scrapes news and sentiment from the web using `DuckDuckGo`.
- **Llama 3.1 Infused:** High-speed inference via Groq's LPUs for near-instant reasoning.
- **Visual Reporting:** Outputs structured tables and formatted Markdown with clear sources.

## 🛠️ Stack Components
- **Orchestration:** [PhiData](https://github.com/phidatahq/phidata)
- **Engine:** Groq (Llama-3.1-8b-instant)
- **Tools:** YFinanceTools, DuckDuckGo
- **Optimization:** Native support for professional-grade formatting and unit tracking (USD, %, Multiples).

## ⚡ Quick Start

1. **Clone & Setup:**
   ```bash
   git clone https://github.com/Neer-tech878/financial_agent.git
   cd financial_agent
   ```

2. **Environment Configuration:**
   Create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Execution:**
   ```bash
   python financial_agent.py
   ```

## 📊 Sample Workflow
By default, the agent is configured to analyze tech giants like **NVIDIA (NVDA)** and **Cisco (CSCO)**, comparing their fundamentals and analyst sentiment to generate a unified recommendation score.

---
*Created by [Neer-tech878](https://github.com/Neer-tech878)*
