from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------
# IMPORTANT: Do NOT use team= with Groq. It breaks in two ways:
#   1. Groq passes additional_information=None -> pydantic validation error
#   2. Sub-agent models need tool-calling support, most Groq models lack it
# Solution: single agent with all tools on llama3-70b-8192
#   - llama3-70b-8192 supports tool calling
#   - 500K tokens/day (5x more than llama-3.3-70b-versatile)
#   - 6K tokens/minute (enough for single-agent requests)
# -----------------------------------------------------------------------

agent = Agent(
    name="Financial & Web Research Agent",
    model=Groq(id="llama-3.1-8b-instant"),
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

