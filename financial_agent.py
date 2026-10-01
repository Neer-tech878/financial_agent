from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------
# Model: qwen/qwen3.8-27b (free tier, 7K ITPM limit)
# Strategy: no company_news (too many tokens), query one stock at a time
# -----------------------------------------------------------------------

agent = Agent(
    name="Financial Research Agent",
    model=Groq(id="qwen/qwen3.8-27b"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=False,  # excluded — too token-heavy for free tier
        ),
    ],
    instructions=[
        "Use tables to display stock data",
        "Show values with units (e.g. USD, %)",
        "Only look up YFinance data for publicly traded companies with valid tickers",
        "End with a clear Buy / Hold / Sell recommendation",
    ],
    show_tool_calls=True,
    markdown=True,
)

# ── Query ─────────────────────────────────────────────────────────────
query = input("Ask the Financial Agent: ").strip()
if not query:
    query = "Should I invest in NVIDIA (NVDA)? Show stock price, fundamentals and analyst recommendations."

agent.print_response(query, stream=False)
