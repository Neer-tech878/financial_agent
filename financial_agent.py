import os
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# -----------------------------------------------------------------------
# Load API key — works both locally (.env) and on Streamlit Cloud (secrets)
# -----------------------------------------------------------------------
try:
    # Streamlit Cloud: reads from App Settings → Secrets
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    # Local: reads from .env file
    from dotenv import load_dotenv
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

# -----------------------------------------------------------------------
# Available models on this Groq account (as of Sep 2026):
#   - qwen/qwen3.8-27b     ← free tier, tool-calling supported (used here)
#   - openai/gpt-oss-120b  ← restricted, not available on all keys
# NOTE: Most Llama/Gemma/Mixtral models have been decommissioned on Groq.
# Check https://console.groq.com/docs/deprecations for updates.
# -----------------------------------------------------------------------

# ── Page config ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="📊 Financial Agent",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Financial AI Agent")
st.caption("Powered by Groq · YFinance · DuckDuckGo · PhiData")
st.markdown("---")

# ── Build agent ─────────────────────────────────────────────────────────
@st.cache_resource
def get_agent():
    return Agent(
        name="Financial & Web Research Agent",
        model=Groq(id="qwen/qwen3.8-27b", api_key=groq_api_key),
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

# ── UI ──────────────────────────────────────────────────────────────────
default_query = (
    "Summarize analyst recommendations for Cisco (CSCO) and NVIDIA (NVDA). "
    "Show current stock price, fundamentals, and latest news for each. "
    "Compare them and give a Buy/Hold/Sell recommendation with reasoning."
)

query = st.text_area(
    "Ask the Financial AI Agent",
    value=default_query,
    height=120,
    placeholder="e.g. Should I invest in Apple (AAPL)? Show fundamentals and analyst ratings.",
)

col1, col2 = st.columns([1, 5])
with col1:
    run = st.button("🔍 Analyze", type="primary", use_container_width=True)
with col2:
    st.caption("Tip: Ask about any publicly traded stock by name or ticker symbol.")

if run:
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Researching... this may take 20–40 seconds ⏳"):
            try:
                agent = get_agent()
                response = agent.run(query, stream=False)
                st.markdown("### 📈 Analysis Result")
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info(
                    "💡 **Tip:** If you see an API error, check that your GROQ_API_KEY "
                    "is set correctly in Streamlit Secrets (App Settings → Secrets)."
                )
