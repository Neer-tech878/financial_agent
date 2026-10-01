import os
import streamlit as st
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Load local .env if available
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Financial Research Agent",
    page_icon="💸",
    layout="wide",
)

st.title("💸 AI-Quant Financial Research Agent")
st.caption("Powered by PhiData, Groq (Qwen 3.8-27B), and Yahoo Finance")

# Sidebar for API key configuration & info
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Retrieve key from Streamlit secrets, environment variables, or user input
    secret_key = ""
    try:
        secret_key = st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        pass

    env_key = os.getenv("GROQ_API_KEY", "")
    default_key = secret_key or env_key

    groq_api_key = st.text_input(
        "Groq API Key",
        value=default_key,
        type="password",
        help="Get a free key from console.groq.com",
    )

    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    else:
        st.warning("Please provide a Groq API Key to run the agent.")

    st.markdown("---")
    st.markdown("### 📊 Features")
    st.markdown(
        """
        - **Stock Fundamentals**
        - **Analyst Recommendations**
        - **Real-Time Prices**
        - **Buy / Hold / Sell Recommendation**
        """
    )

# Predefined example queries
default_prompt = "Should I invest in NVIDIA (NVDA)? Show stock price, fundamentals and analyst recommendations."

query = st.text_input(
    "Ask the Financial Agent:",
    value=default_prompt,
    placeholder="e.g. Analyze Apple (AAPL) stock and give a recommendation",
)

col1, col2 = st.columns([1, 5])
with col1:
    submit_button = st.button("🚀 Analyze Stock", use_container_width=True)

if submit_button:
    if not os.getenv("GROQ_API_KEY"):
        st.error("Missing Groq API Key! Please enter it in the sidebar or configure it in Streamlit Secrets.")
    elif not query.strip():
        st.warning("Please enter a valid stock query.")
    else:
        with st.spinner("Fetching financial data & analyzing metrics..."):
            try:
                # Same agent architecture as financial_agent.py
                agent = Agent(
                    name="Financial Research Agent",
                    model=Groq(id="qwen/qwen3.8-27b"),
                    tools=[
                        YFinanceTools(
                            stock_price=True,
                            analyst_recommendations=True,
                            stock_fundamentals=True,
                            company_news=False,  # Excluded — token heavy for free tier
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

                response = agent.run(query)
                response_text = response.content if hasattr(response, "content") else str(response)

                st.markdown("### 📈 Research Analysis")
                st.markdown(response_text)
            except Exception as e:
                st.error(f"Error during analysis: {e}")
