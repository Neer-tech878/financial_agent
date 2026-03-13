from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os#pulls keys from memory loaded by dotenv to the sys/program to use it authenticate or connectr with that groq or phidata
import phi
from phi.playground import Playground,serve_playground_app
#load env variables from .env files
load_dotenv()
phi.api_key=os.getenv("API_KEY")

# web_search_agent=Agent(
#     name="Web Search Agent",
#     role="Search the web for the information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources"],
#     show_tools_calls=True,
#     markdown=True,

# )

# financial_agent = Agent(
#     name="Financial Assistant",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[
#         YFinanceTools(
#             stock_price=True,
#             analyst_recommendations=True,
#             stock_fundamentals=True,
#             company_news=True,
#         ),
#     ],
#     instructions=[
#         "Use tables to display stock data",
#         "Show values with units (e.g. USD, %)",
#         "Only look up YFinance data for publicly traded companies with valid tickers",
#         "End with a clear Buy / Hold / Sell recommendation for each stock with units",
#     ],
#     show_tool_calls=True,
#     markdown=True,
# )


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

app=Playground(agents=[agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)