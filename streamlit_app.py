import streamlit as st
import sys
import threading
import queue
import io
import yfinance as yf
import pandas as pd
from dotenv import load_dotenv

# ── Page config
st.set_page_config(
    page_title="AI Stock Analyst · CrewAI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()

# ── Custom CSS
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Dark Glassmorphism Background */
.stApp {
    background: radial-gradient(circle at 10% 20%, rgb(17, 24, 39) 0%, rgb(17, 24, 39) 90%);
    color: #f8fafc;
}

/* Sidebar Glassmorphism */
section[data-testid="stSidebar"] {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(148, 163, 184, 0.1);
}

/* Hero Section */
.hero-container {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 51, 234, 0.1) 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(to right, #60a5fa, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 1.1rem;
    font-weight: 400;
}

/* Agent Cards */
.agent-card {
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}

.agent-card:hover {
    transform: translateY(-2px);
    border-color: rgba(96, 165, 250, 0.5);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.agent-title {
    color: #60a5fa;
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.agent-desc {
    color: #cbd5e1;
    font-size: 0.9rem;
    line-height: 1.5;
}

/* Result Box */
.result-container {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 16px;
    padding: 2rem;
    margin-top: 1.5rem;
}

/* Badges */
.badge {
    padding: 0.5rem 1rem;
    border-radius: 9999px;
    font-weight: 600;
    font-size: 0.875rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.badge-buy { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.4); }
.badge-sell { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
.badge-hold { background: rgba(234, 179, 8, 0.2); color: #facc15; border: 1px solid rgba(234, 179, 8, 0.4); }

/* Buttons */
div.stButton > button {
    background: linear-gradient(to right, #4f46e5, #7c3aed);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s;
    width: 100%;
}

div.stButton > button:hover {
    opacity: 0.9;
    transform: scale(1.02);
}

/* Inputs */
.stTextInput input, .stSelectbox > div[data-baseweb="select"] > div {
    background-color: rgba(30, 41, 59, 0.5);
    border-color: rgba(148, 163, 184, 0.2);
    color: white;
}
</style>""", unsafe_allow_html=True)

# ── Header Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">AI Stock Analyst</div>
    <div class="hero-subtitle">High-frequency multi-agent intelligence for smarter trading decisions.</div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/bullish.png", width=64)
    st.markdown("### ⚙️ Analysis Config")
    
    stock_input = st.text_input(
        "Stock Ticker",
        value="AAPL",
        placeholder="e.g. NVDA, TSLA",
        help="Enter the symbol of the stock you want to analyze."
    ).strip().upper()
    
    st.markdown("---")
    
    with st.expander("👤 User Profile", expanded=True):
        risk_tolerance = st.select_slider(
            "Risk Tolerance",
            options=["Low", "Medium", "High"],
            value="Medium",
            help="Determines how aggressive the trading strategy should be."
        )
        
        investment_horizon = st.select_slider(
            "Investment Horizon",
            options=["Short-term", "Medium-term", "Long-term"],
            value="Medium-term",
            help="Short-term: Days/Weeks | Medium: Months | Long: Years"
        )
    
    st.markdown("---")
    
    st.markdown("### 🤖 Active Agents")
    st.markdown("""
    <div class="agent-card">
        <div class="agent-title">📊 Fundamental Analyst</div>
        <div class="agent-desc">Analyzes financial health, news sentiment, and market trends.</div>
    </div>
    <div style="height: 10px;"></div>
    <div class="agent-card">
        <div class="agent-title">📈 Technical Trader</div>
        <div class="agent-desc">Executes strategies based on price action and technical indicators.</div>
    </div>
    """, unsafe_allow_html=True)

# ── Main Content Area
col1, col2 = st.columns([7, 3])

with col1:
    if stock_input:
        try:
            # Quick Stock Preview Chart
            stock_data = yf.Ticker(stock_input)
            hist = stock_data.history(period="1y")
            
            if not hist.empty:
                st.subheader(f"Price History: {stock_input}")
                st.line_chart(hist['Close'], height=300, use_container_width=True)
            else:
                st.info("No historical data available for preview.")
        except Exception:
            st.info("Enter a valid ticker to see price history.")

with col2:
    st.markdown("### � How it Works")
    st.info(
        """
        **1. Data Ingestion:**
        Live market data is fetched via Yahoo Finance.
        
        **2. Multi-Agent Analysis:**
        Independent AI agents analyze fundamentals & technicals.
        
        **3. Strategic Synthesis:**
        Agents debate to form a cohesive strategy based on your risk profile.
        """
    )
    
    run_btn = st.button("🚀 Start Analysis", use_container_width=True)

# ── Analysis Logic
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
    st.session_state.trade_result = None
    st.session_state.running = False

def run_crew(stock, risk, horizon, result_q, log_q):
    old_stdout = sys.stdout
    sys.stdout = log_capture = io.StringIO()
    try:
        from crew import stock_crew
        # Pass the new inputs to the crew kickoff
        inputs = {
            "stock": stock,
            "risk_tolerance": risk,
            "investment_horizon": horizon
        }
        result = stock_crew.kickoff(inputs=inputs)
        log_q.put(log_capture.getvalue())
        result_q.put(("ok", str(result)))
    except Exception as e:
        log_q.put(log_capture.getvalue())
        result_q.put(("err", str(e)))
    finally:
        sys.stdout = old_stdout

if run_btn:
    if not stock_input:
        st.toast("Please enter a stock ticker.", icon="⚠️")
    else:
        st.session_state.running = True
        st.session_state.analysis_result = None
        
        result_q = queue.Queue()
        log_q = queue.Queue()
        
        with st.status(f"Analysing {stock_input}...", expanded=True) as status:
            st.write("🔍 Fetching market data...")
            st.write("🤖 Agents analyzing trends...")
            
            t = threading.Thread(target=run_crew, args=(stock_input, risk_tolerance, investment_horizon, result_q, log_q), daemon=True)
            t.start()
            t.join(timeout=300)
            
            status.update(label="Analysis Configuration Complete!", state="complete", expanded=False)
            
        if not result_q.empty():
            status_code, payload = result_q.get()
            logs = log_q.get() if not log_q.empty() else ""
            
            if status_code == "ok":
                st.session_state.trade_result = payload
                st.session_state.logs = logs
            else:
                st.error(f"Error: {payload}")

# ── Results Rendering
if st.session_state.trade_result:
    result_text = st.session_state.trade_result
    upper_res = result_text.upper()
    
    if "BUY" in upper_res:
        badge_html = '<span class="badge badge-buy">✅ Strong Buy</span>'
    elif "SELL" in upper_res:
        badge_html = '<span class="badge badge-sell">🔴 Strong Sell</span>'
    else:
        badge_html = '<span class="badge badge-hold">⚠️ Hold</span>'
        
    st.markdown("---")
    st.markdown(f"## 🎯 Strategic Recommendation: {badge_html}", unsafe_allow_html=True)
    
    with st.container():
        st.markdown(f"""
        <div class="result-container">
            {result_text}
        </div>
        """, unsafe_allow_html=True)
    
    # Logs Expander
    with st.expander("�️ View Agent Thoughts (Debug Logs)"):
        st.code(st.session_state.logs, language="text")

    # Download Report
    st.download_button(
        label="📥 Download Full Report",
        data=result_text,
        file_name=f"{stock_input}_analysis_report.txt",
        mime="text/plain",
    )
