from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------
# Available models on this Groq account (as of Sep 2026):
#   - qwen/qwen3.8-27b     ← free tier, tool-calling supported (used here)
#   - openai/gpt-oss-120b  ← restricted, not available on all keys
#   - openai/gpt-oss-20b   ← restricted, not available on all keys
# NOTE: Most Llama/Gemma/Mixtral models have been decommissioned on Groq.
# Check https://console.groq.com/docs/deprecations for updates.
# -----------------------------------------------------------------------

agent = Agent(
    name="Financial & Web Research Agent",
    model=Groq(id="qwen/qwen3.8-27b"),
    tools=[
        DuckDuckGo(),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Always include sources",
        "Use tables to display stock data",
        "Show values with units (e.g. USD, %)",
        "Only look up YFinance data for publicly traded companies with valid tickers",
        "End with a clear Buy / Hold / Sell recommendation for each stock with units",
    ],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(
    "Summarize analyst recommendations for Cisco (CSCO) and NVIDIA (NVDA). "
    "Show current stock price, fundamentals, and latest news for each. "
    "Compare them and give a Buy/Hold/Sell recommendation with reasoning.",
    stream=False,
)

