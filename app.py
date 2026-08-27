import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# McKinsey Executive Dark Theme Configuration
st.set_page_config(
    page_title="EXECUTIVE WAR-ROOM // Project Phantom-Nexus",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #f8fafc; font-family: 'Inter', sans-serif; }
    .metric-container { background: #111827; padding: 16px; border-radius: 6px; border: 1px solid #1f2937; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
    .exec-card { background: #111827; padding: 20px; border-radius: 6px; border: 1px solid #374151; margin-bottom: 16px; }
    .live-dot { height: 10px; width: 10px; background-color: #10b981; border-radius: 50%; display: inline-block; animation: pulse 1.5p infinite; }
    h1, h2, h3 { color: #f8fafc; font-weight: 600; letter-spacing: -0.025em; }
    </style>
""", unsafe_allow_html=True)

# Executive Header Block
st.markdown("### STRATEGIC EXECUTIVE WAR-ROOM // INTELIGENCE BRIEFING")
st.title("Project Phantom-Nexus: Real-Time Hybrid Cartel & Shell Telemetry")
st.markdown("---")

# Attribution & Live Feed Bar
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown(
        """
        <div style="background-color: #111827; padding: 10px 14px; border-radius: 4px; border-left: 3px solid #3b82f6;">
            <span style="font-weight: 500; color: #9ca3af;">Principal Lead:</span> Mohd Khairul Ridhuan bin Mohd Fadzil &nbsp;|&nbsp; 
            <span style="font-weight: 500; color: #9ca3af;">Architecture:</span> McKinsey Tier-1 Forensic Grid &nbsp;|&nbsp; 
            <span style="font-weight: 500; color: #9ca3af;">Classification:</span> EYES-ONLY
        </div>
        """,
        unsafe_allow_html=True
    )
with col_h2:
    current_time_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
        <div style="text-align: right; padding-top: 5px;">
            <span class="live-dot"></span> <span style="font-size: 13px; color: #10b981; font-weight: bold;">LIVE FEED ACTIVE</span><br>
            <span style="font-size: 11px; color: #9ca3af;">UTC: {current_time_utc}</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# EXECUTIVE KPI METRICS (McKinsey Style)
# ---------------------------------------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
    <div class="metric-container">
        <span style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Total Capital Tracked</span>
        <h2 style="margin: 4px 0 0 0; color: #f8fafc;">$840.2M <span style="font-size: 14px; color: #ef4444;">(+4.2%)</span></h2>
        <span style="font-size: 11px; color: #6b7280;">Cross-Border Layering Volume</span>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
    <div class="metric-container">
        <span style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Active Shell Matrix</span>
        <h2 style="margin: 4px 0 0 0; color: #f8fafc;">312 Nodes</h2>
        <span style="font-size: 11px; color: #6b7280;">BVI, Cyprus, Labuan Enclaves</span>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
    <div class="metric-container">
        <span style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Front Business Vectors</span>
        <h2 style="margin: 4px 0 0 0; color: #f8fafc;">48 Units</h2>
        <span style="font-size: 11px; color: #6b7280;">Restaurants, Realty, Charities</span>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
    <div class="metric-container">
        <span style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Geopolitical Override</span>
        <h2 style="margin: 4px 0 0 0; color: #f59e0b;">ACTIVE</h2>
        <span style="font-size: 11px; color: #6b7280;">Section 9-B Veto Enforced</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# SIDEBAR CONTROLS & REAL-TIME SIMULATION
# ---------------------------------------------------------
st.sidebar.header("Executive Parameters")
analysis_mode = st.sidebar.selectbox(
    "Select Intelligence View",
    [
        "1. Executive Summary & Architecture",
        "2. Real-Time Transaction Stream Telemetry",
        "3. Front-Business Laundering Anomaly Audit",
        "4. Geopolitical Veto & State Override Dossier"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Live Telemetry Actions")
refresh_stream = st.sidebar.button("Poll Live Registry Streams")

if refresh_stream:
    with st.spinner("Polling global registry nodes (Cyprus, BVI, UAE)..."):
        time.sleep(0.8)
    st.sidebar.success("Telemetry synchronized successfully.")

# ---------------------------------------------------------
# MAIN EXECUTIVE VIEW SWITCHER
# ---------------------------------------------------------
if "1. Executive Summary" in analysis_mode:
    col_main1, col_main2 = st.columns([1.5, 1])
    
    with col_main1:
        st.markdown("""
        <div class="exec-card">
            <h3 style="margin-top:0;">Strategic Synthesis</h3>
            <p><b>Core Insight:</b> The Phantom-Nexus syndicate bypasses traditional financial surveillance by weaponizing legal commercial structures—specifically high-turnover hospitality fronts and non-profit foundations—to inject illicit bulk capital before dispersing it across a 312-node offshore shell matrix.</p>
            <p><b>Operational Vector:</b> Microchip smuggling and parallel cartel logistics are cross-collateralized through these corporate layers, ensuring complete financial obfuscation.</p>
            <p><b>Systemic Risk:</b> High exposure for international compliance frameworks due to multi-jurisdictional regulatory arbitrage.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_main2:
        st.markdown("""
        <div class="exec-card">
            <h3 style="margin-top:0;">Risk Distribution Matrix</h3>
        """, unsafe_allow_html=True)
        risk_df = pd.DataFrame({
            "Vector": ["Front Businesses", "Shell Matrix", "Cargo Routing", "State Shields"],
            "Risk Score": [88, 96, 91, 99]
        })
        st.dataframe(risk_df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif "2. Real-Time Transaction" in analysis_mode:
    st.subheader("Live Cross-Border Transaction & Packet Stream")
    st.write("Simulated real-time WebSocket telemetry capturing capital flight movements across global node clusters.")
    
    # Generate dynamic mock real-time stream data
    stream_data = pd.DataFrame([
        {"Timestamp": datetime.utcnow().strftime("%H:%M:%S") + " UTC", "Source Node": "Cyprus Front #14", "Destination": "BVI Vault Holding", "Amount ($USD)", "Type": "Over-Invoicing", "Status": "Masked"},
        {"Timestamp": datetime.utcnow().strftime("%H:%M:%S") + " UTC", "Source Node": "Fast-Food POS #09", "Destination": "Labuan Clearing House", "Amount ($USD)", "Type": "Cash Injection", "Status": "Layered"},
        {"Timestamp": datetime.utcnow().strftime("%H:%M:%S") + " UTC", "Source Node": "Charity Foundation A", "Destination": "Swiss Private Vault", "Amount ($USD)", "Type": "Tax-Exempt Transfer", "Status": "Secured"},
        {"Timestamp": datetime.utcnow().strftime("%H:%M:%S") + " UTC", "Source Node": "Dubai Free Zone", "Destination": "Singapore Switch Node", "Amount ($USD)", "Type": "Trade Settlement", "Status": "Routed"}
    ])
    # Fix dataframe column assignment for display
    stream_df = pd.DataFrame({
        "Timestamp": ["19:33:02 UTC", "19:33:04 UTC", "19:33:07 UTC", "19:33:10 UTC"],
        "Source Node": ["Cyprus Front #14", "Fast-Food POS #09", "Charity Foundation A", "Dubai Free Zone"],
        "Destination": ["BVI Vault Holding", "Labuan Clearing", "Swiss Private Vault", "Singapore Switch"],
        "Volume ($USD)": ["$4,250,000", "$1,890,000", "$6,500,000", "$12,400,000"],
        "Vector Classification": ["Over-Invoicing", "Cash Injection", "Tax-Exempt Transfer", "Trade Settlement"]
    })
    st.dataframe(stream_df, use_container_width=True, hide_index=True)

elif "3. Front-Business Laundering" in analysis_mode:
    st.subheader("Front-Business Point-of-Sales (POS) Anomaly Audit")
    st.write("Comparing physical foot-traffic analytics against reported digital sales revenue to expose cash-injection laundering.")
    
    audit_df = pd.DataFrame({
        "Front Enterprise": ["Metro Burger Outlet #4", "Central Spice Bistro", "Elite Holdings Realty", "Hope Haven Charity"],
        "Reported Revenue": ["$450,000 / mo", "$620,000 / mo", "$2,100,000 / mo", "$1,800,000 / mo"],
        "Estimated Foot Traffic": ["Low (12 customers/day)", "Low (18 customers/day)", "Nominal", "Nominal"],
        "Anomaly Variance": ["+940% (Critical Flag)", "+880% (Critical Flag)", "Masked Asset Loop", "Exempt Status"]
    })
    st.dataframe(audit_df, use_container_width=True, hide_index=True)

elif "4. Geopolitical Veto" in analysis_mode:
    st.subheader("Diplomatic Override & State Immunity Documentation")
    st.markdown("""
    <div class="exec-card" style="border: 1px solid #f59e0b;">
        <span style="background: #f59e0b; color: #000; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">CLASSIFIED DIRECTIVE // SECTION 9-B</span>
        <h3 style="margin-top:10px;">Intervention Audit Log</h3>
        <p><b>Issuing Authority:</b> Inter-Agency Strategic Oversight Committee (Washington / Eurasia)</p>
        <p><b>Operational Impact:</b> Immediate cessation of Interpol prosecution protocols. Freezing orders rescinded.</p>
        <p><b>Strategic Justification:</b> Continued operation of the microchip supply network is deemed critical for ongoing state-level technology acquisition channels. Asset integrity protected under diplomatic immunity frameworks.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #6b7280; font-size: 12px;'>PROJECT PHANTOM-NEXUS // ARCHITECTED FOR EXECUTIVE BRIEFING BY: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b></p>",
    unsafe_allow_html=True
)
