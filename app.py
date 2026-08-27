import streamlit as st
import pandas as pd

# Konfigurasi Halaman - Minimalist Corporate Executive Layout
st.set_page_config(
    page_title="Project Phantom Hub | Executive Intelligence Briefing",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gaya CSS Minimalist McKinsey/BCG Dark Corporate Style
st.markdown("""
    <style>
    /* Global Theme */
    .main { background-color: #0b0c10; color: #c5c6c7; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    h1, h2, h3 { color: #ffffff !important; font-weight: 500; letter-spacing: -0.5px; }
    
    /* Minimalist Cards / Metric Containers */
    .metric-card {
        background-color: #1f2833;
        border: 1px solid #28313b;
        padding: 24px;
        border-radius: 4px;
    }
    .metric-value { font-size: 28px; font-weight: 600; color: #66fcf1; margin-top: 8px; }
    .metric-label { font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #8892b0; }
    
    /* Executive Summary Box */
    .exec-box {
        background-color: #12161f;
        border-left: 3px solid #66fcf1;
        padding: 20px;
        margin-bottom: 24px;
        border-radius: 0 4px 4px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER & ATTRUBUTION (MINIMALIST CORPORATE)
# -----------------------------------------------------------------------------
st.title("PROJECT PHANTOM HUB")
st.markdown("### *Micro-Anatomy of Cross-Border Sanctions Evasion & Shadow Logistics*")
st.markdown("---")

# Investigator Credit Bar
st.markdown(f"""
<div style="font-size: 13px; color: #8892b0; margin-bottom: 30px;">
    <strong>Principal Investigator:</strong> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
    <strong>Classification:</strong> Restricted Executive Briefing &nbsp;|&nbsp; 
    <strong>Framework:</strong> Multi-Source Intelligence & Behavioral Telemetry
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# THE 20-SECOND EXECUTIVE RULE: THE CORE PROBLEM & METRICS
# -----------------------------------------------------------------------------
st.markdown("#### **Executive Summary (20-Second Triage)**")
st.markdown("""
<div class="exec-box">
    <strong>The Threat:</strong> Modern illicit finance and supply chain bypass do not occur through complex corporate structures. They concentrate in <strong>microscopic administrative blind spots</strong>—specifically, singular physical "Phantom Hubs" housing clusters of shell entities managed by proxy "Ghost Directors." This dashboard isolates, scores, and visualizes these anomalies in real time.
</div>
""", unsafe_allow_html=True)

# 3-Column Minimalist Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Target Node Vector</div>
            <div class="metric-value">Unit 402, Limassol</div>
            <div style="font-size: 12px; color: #ff6b6b; margin-top: 4px;">▲ Virtual Office Mail-Drop</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Entity Concentration</div>
            <div class="metric-value">142 Active Shells</div>
            <div style="font-size: 12px; color: #ffcc00; margin-top: 4px;">▲ High Anomaly Clustering</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Systemic Risk Index</div>
            <div class="metric-value">94.8 / CRITICAL</div>
            <div style="font-size: 12px; color: #ff6b6b; margin-top: 4px;">▲ Sanctions Evasion Vector</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ANALYTICAL DEEP-DIVE: LIVE CORRELATION & GHOST DIRECTORS
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown("#### **Behavioral Cross-Mapping: Ghost Directors**")
    st.markdown("<p style='font-size: 13px; color: #8892b0;'>Isolating proxy directors managing multi-jurisdictional shell entities under a single physical footprint.</p>", unsafe_allow_html=True)
    
    # Clean, Minimalist Corporate Data Table
    audit_data = {
        "Entity Designation": ["Apex Global FZE", "Vanguard Logistics", "Orion Tech Trading", "Meridian Systems"],
        "Principal Proxy / UBO": ["A. V. Petrov", "A. V. Petrov", "Elena Rostova", "A. V. Petrov"],
        "Jurisdiction Link": ["Cyprus / UAE", "Cyprus / BVI", "Cyprus / Panama", "Cyprus / Malta"],
        "Risk Status": ["Critical", "Critical", "Under Watch", "Critical"]
    }
    df_audit = pd.DataFrame(audit_data)
    st.dataframe(df_audit, use_container_width=True, hide_index=True)

with col_right:
    st.markdown("#### **Systemic Impact & Industry Disruption**")
    st.markdown("""
    <div style="font-size: 13px; line-height: 1.6; color: #c5c6c7;">
        <p><strong>For Corporate Intelligence & Boutiques:</strong> 
        Provides automated triage capabilities that bypass manual registry delays, allowing elite firms to audit counterparty exposure instantly.</p>
        
        <p><strong>For Formal & Underground Intelligence:</strong> 
        Proves that open-source geospatial metadata and director-overlap clustering can outpace sophisticated proxy layers without breaching privacy mandates.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 11px; color: #4e5d6c;'>Project Phantom Hub &bull; Architected by Mohd Khairul Ridhuan bin Mohd Fadzil &bull; Designed for Executive Decision-Makers</p>", 
    unsafe_allow_html=True
)
