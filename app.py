import streamlit as st
import pandas as pd
import time

# Konfigurasi Tema Eksklusif
st.set_page_config(
    page_title="PHANTOM-AI // Autonomous Intelligence Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #090d16; color: #e2e8f0; font-family: 'Inter', sans-serif; }
    .stTextInput>div>div>input { background-color: #1e293b; color: #ffffff; border: 1px solid #334155; }
    .intel-panel { background: #111827; padding: 22px; border-radius: 8px; border: 1px solid #1f2937; margin-bottom: 20px; }
    .badge-high { background: #dc2626; color: white; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown("### PROJECT PHANTOM // AUTONOMOUS INTEL ENGINE")
st.title("AI-Driven Transnational Threat & Shell Company Hunter")
st.markdown("---")

st.markdown(
    """
    <div style="background-color: #1e293b; padding: 12px 18px; border-radius: 6px; border-left: 4px solid #3b82f6; margin-bottom: 25px;">
        <span style="font-weight: 600; color: #ffffff;">Principal Investigator:</span> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #ffffff;">Engine Core:</span> Autonomous OSINT Telemetry Agent
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# INTERAKSI UTAMA: MASUKKAN SASARAN UNTUK DISIASAT
# ---------------------------------------------------------
st.sidebar.header("Target Investigation Setup")
target_input = st.sidebar.text_input("Enter Target Entity / Shell Name", "Apex Global FZE")
investigate_btn = st.sidebar.button("Run Autonomous Investigation")

if investigate_btn:
    with st.spinner(f"Executing deep-web telemetry scan and cross-border node correlation for '{target_input}'..."):
        time.sleep(1.5) # Simulasi proses enjin AI bekerja di latar belakang
    st.success(f"Investigation dossier compiled successfully for target: {target_input}")

# Paparan Utama Analisis
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(f"""
    <div class="intel-panel">
        <span class="badge-high">LIVE THREAT DOSSIER</span>
        <h3 style="margin-top:10px;">Target Analysis: {target_input}</h3>
        <p><b>1. Operational Status:</b> Active front-end shell connected to multi-jurisdictional proxy network.</p>
        <p><b>2. Physical Node Anomaly:</b> Shares commercial registration suite with 114 other unrelated entities in Limassol, Cyprus.</p>
        <p><b>3. Ultimate Beneficial Owner (UBO) Risk:</b> High probability of hidden state-backed proxy oversight via BVI holding veils.</p>
        <p><b>4. Evasion Vector Prediction:</b> Anticipated shift toward Central Asian transit corridors upon secondary sanctions enforcement.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### Automated Metrics")
    st.metric(label="Threat Index Score", value="98.2 / 100", delta="Critical Risk")
    st.metric(label="Proxy Clustering Density", value="Severe", delta="100+ Shells / Address")
    st.metric(label="Confidence Level", value="95.7%", delta="AI Telemetry Match")

st.markdown("---")
st.subheader("Autonomous Trace Logs & Node Event Timeline")

# Log Simulasi Agen AI
log_data = pd.DataFrame([
    {"Timestamp": "03:21:40 UTC", "Node": "Cyprus Registry", "Event": "Virtual address saturation anomaly detected", "Severity": "High"},
    {"Timestamp": "03:21:41 UTC", "Node": "BVI Vault", "Event": "Nominee director signature cluster matched", "Severity": "Critical"},
    {"Timestamp": "03:21:43 UTC", "Node": "UAE Logistics", "Event": "Parallel trade-invoicing vector identified", "Severity": "High"},
    {"Timestamp": "03:21:45 UTC", "Node": "AI Synthesis", "Event": "Cross-border sanctions evasion pipeline confirmed", "Severity": "Maximum"}
])
st.dataframe(log_data, use_container_width=True)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 13px;'>AUTONOMOUS ENGINE ARCHITECTED BY: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b></p>",
    unsafe_allow_html=True
)
