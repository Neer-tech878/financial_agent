# Financial AI Agent

An AI-powered financial assistant built with [PhiData](https://docs.phidata.com/), Groq, YFinance, and DuckDuckGo.

## What it does
- Fetches real-time stock prices, fundamentals, and analyst recommendations via YFinance
- Searches the web for latest company news via DuckDuckGo
- Gives Buy / Hold / Sell recommendations with reasoning

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/financial-agent.git
cd financial-agent
```

### 2. Create and activate a virtual environment
```bash
conda create -p venv python=3.12
conda activate ./venv
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API keys
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at: https://console.groq.com

### 5. Run the agent
```bash
python financial_agent.py
```

## Project Structure
```
financial_agent.py   # Main financial AI agent
pdf_assistant.py     # PDF Q&A assistant
requirements.txt     # Python dependencies
.env                 # API keys (never commit this!)
```

## Models Used
- `llama-3.3-70b-versatile` via Groq API

## Note
-Never commit your `.env` file. It is already excluded in `.gitignore`.
## Error incase
1. For incase .venv files not reading 
inside:
.vscode folder >> settings.json>>
{
  "python.terminal.useEnvFile": true
}
paste this command for reading env api keys in terminal
2. Install multipart for playground.py functioning use command:
pip install python-multipart
