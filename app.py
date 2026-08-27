import streamlit as st
import pandas as pd
import pydeck as pdk

# ---------------------------------------------------------
# KONFIGURASI ESTETIKA KORPORAT MINIMALIST
# ---------------------------------------------------------
st.set_page_config(
    page_title="Project Phantom Hub | Executive Intelligence Briefing",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Rekaan Stail Konsultansi Global (McKinsey/BCG/Dialectic Style: Clean, Light, Professional)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; color: #1a1a1a; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 6px; border: 1px solid #e1e4e8; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    .executive-card { background-color: #ffffff; padding: 25px; border-radius: 6px; border: 1px solid #e1e4e8; margin-bottom: 20px; }
    h1, h2, h3 { color: #111827; font-weight: 700; }
    p, li { color: #4b5563; font-size: 15px; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER & EXECUTIVE ATTRIBUTION
# ---------------------------------------------------------
st.title("PROJECT PHANTOM HUB")
st.markdown("### *Global Micro-Anatomy & Sanctions Evasion Vulnerability Assessment*")
st.markdown("---")

# Baris Atribusi Korporat Rasmi
st.markdown(
    """
    <div style="background-color: #edf2f7; padding: 12px 18px; border-radius: 6px; border-left: 4px solid #1a365d; margin-bottom: 25px;">
        <span style="font-weight: 600; color: #1a365d;">Principal Investigator:</span> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #1a365d;">Classification:</span> Executive Intelligence Briefing &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #1a365d;">Framework:</span> Multi-Jurisdictional Node Audit
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# PILIHAN NEGARA & NOD GLOBAL (SIDEBAR MINIMALIST)
# ---------------------------------------------------------
st.sidebar.header("Global Node Selector")
selected_node = st.sidebar.selectbox(
    "Select Strategic Jurisdiction",
    [
        "Cyprus (Limassol Transhipment Node)", 
        "British Virgin Islands (Tortola Holding Node)", 
        "United Arab Emirates (Dubai Free Zone Entity)",
        "United Kingdom (London Property Shell Node)"
    ]
)

# Data Tetapan Nod Berdasarkan Pilihan Negara
node_data_map = {
    "Cyprus (Limassol Transhipment Node)": {"lat": 34.6851, "lon": 33.0384, "shells": 142, "threat": "Critical (94/10)", "focus": "Dual-use technology and semiconductor diversion."},
    "British Virgin Islands (Tortola Holding Node)": {"lat": 18.4207, "lon": -64.6400, "shells": 489, "threat": "Severe (91/100)", "focus": "Anonymous ownership masking heavy machinery transit."},
    "United Arab Emirates (Dubai Free Zone Entity)": {"lat": 25.2048, "lon": 55.2708, "shells": 230, "threat": "High (87/100)", "focus": "Petrochemical re-routing and parallel banking channels."},
    "United Kingdom (London Property Shell Node)": {"lat": 51.5074, "lon": -0.1278, "shells": 95, "threat": "High (84/100)", "focus": "Sovereign wealth layering and luxury asset acquisition."}
}

current_node = node_data_map[selected_node]

# ---------------------------------------------------------
# BAHAGIAN 1: ATURAN 20-SAAT (EXECUTIVE METRICS)
# ---------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Selected Jurisdiction", selected_node.split(" ")[0], "Target Node")
col2.metric("Active Shell Entities", f"{current_node['shells']} Units", "Anomalous Density")
col3.metric("Systemic Threat Index", current_node['threat'], "Sanctions Vector")
col4.metric("Verification Status", "Verified Real-Time", "Open Telemetry")

st.markdown("---")

# ---------------------------------------------------------
# BAHAGIAN 2: ANALISIS MASALAH & MENGAPA IA BERBAHAYA
# ---------------------------------------------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("1. Strategic Context & The Problem Statement")
    st.write("""
    Global commerce relies on trust-based institutional frameworks. However, sophisticated bad actors exploit **microscopic regulatory blind spots** rather than breaching hard perimeters. 
    
    * **The Phantom Hub Mechanism:** A single physical address (often an unstaffed virtual office or small suite) acting as the registered legal home for hundreds of completely unrelated corporations.
    * **The Ghost Director Proxy:** The systematic appointment of recurring nominal directors to obscure ultimate beneficial ownership (UBO).
    """)
    
    st.subheader("2. Structural Hazard & Potential Harm")
    st.markdown(f"""
    * **Sanctions Evasion Vector:** Enables the unmonitored flow of restricted dual-use components, bypassing international trade restrictions.
    * **Systemic Financial Risk:** Facilitates illicit layering of funds, disguising state-backed or criminal proceeds as legitimate corporate trade.
    * **Specific Regional Risk ({selected_node.split(' ')[0]}):** <em>{current_node['focus']}</em>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("3. Geospatial Node Intelligence (GeoINT)")
    # Peta Minialist Korporat (Clean Light Theme)
    chart_data = pd.DataFrame({
        'lat': [current_node['lat']],
        'lon': [current_node['lon']],
        'name': [selected_node]
    })
    
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v10',
        initial_view_state=pdk.ViewState(
            latitude=current_node['lat'],
            longitude=current_node['lon'],
            zoom=12,
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[220, 38, 38, 200]', # Clean Corporate Red
                get_radius=800,
                pickable=True,
            ),
        ],
    ))

st.markdown("---")

# ---------------------------------------------------------
# BAHAGIAN 3: SOLUSI & SUMBANGAN KEPADA INDUSTRI / KOMUNITI
# ---------------------------------------------------------
st.subheader("4. Proprietary Solution & Industry Contribution")

col_sol1, col_sol2 = st.columns(2)

with col_sol1:
    st.markdown("""
    <div class="executive-card">
        <h4><b>The Algorithmic Solution</b></h4>
        <p>Project Phantom Hub deploys automated geospatial and network graph correlation to audit multi-jurisdictional shell networks in seconds. By flagging structural anomalies (such as high director clustering and virtual address saturation), compliance officers can preemptively intercept illicit pathways.</p>
    </div>
    """, unsafe_allow_html=True)

with col_sol2:
    st.markdown("""
    <div class="executive-card">
        <h4><b>Disrupting Formal & Underground Intelligence</b></h4>
        <p>This initiative bridges the gap between expensive proprietary intelligence tools and open-source transparency. It sets a new benchmark for corporate compliance boutiques and international legal practices, proving that open-source telemetry can outpace sophisticated proxy networks.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Project Phantom Hub // Architected and Deployed by Principal Investigator Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) for Global Strategic Intelligence Assessment.")
