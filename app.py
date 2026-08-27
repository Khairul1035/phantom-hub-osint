import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

# Konfigurasi Tema Korporat Elit
st.set_page_config(
    page_title="PROJECT PHANTOM HUB | Granular Intelligence Dossier",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #f8fafc; color: #0f172a; font-family: 'Inter', sans-serif; }
    .intel-card { background: #ffffff; padding: 22px; border-radius: 6px; border: 1px solid #cbd5e1; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    h1, h2, h3 { color: #0f172a; font-weight: 700; }
    .tag-alert { background: #dc2626; color: white; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Header Utama Projek
st.markdown("### PROJECT PHANTOM HUB // GRANULAR INTEL DOSSIER")
st.title("Deep-Dive Transnational Network & Evasion Vector Analysis")
st.markdown("---")

# Baris Atribusi Principal Investigator
st.markdown(
    """
    <div style="background-color: #f1f5f9; padding: 12px 18px; border-radius: 6px; border-left: 4px solid #0f172a; margin-bottom: 25px;">
        <span style="font-weight: 600; color: #0f172a;">Principal Investigator:</span> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #0f172a;">Analytical Depth:</span> Granular UBO & Financial Flow Tracing &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #0f172a;">Classification:</span> Restricted Eyes-Only
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR: PEMILIHAN KES OPERASI MENDALAM
# ---------------------------------------------------------
st.sidebar.header("Target Syndicate Dossier")
selected_syndicate = st.sidebar.selectbox(
    "Select Investigated Network",
    [
        "Syndicate Alpha: Dual-Use Tech Diversion (Cyprus-UAE Corridor)",
        "Syndicate Beta: State-Backed Capital Flight (BVI-London Shield)",
        "Syndicate Gamma: Maritime Sanctions Evasion (APAC Transit)"
    ]
)

# Pangkalan Data Perincian Mendalam (Granular Intelligence Breakdown)
dossier_data = {
    "Syndicate Alpha: Dual-Use Tech Diversion (Cyprus-UAE Corridor)": {
        "ubo": "A. V. Petrov (Linked to state intelligence directorate procurement arms)",
        "transactions": "Over-invoicing via shell trade credits, layered through Dubai free zone parallel accounts, supplemented by crypto-stablecoin staging.",
        "backers": "Jurisdictional regulatory arbitrage in non-FATF aligned financial enclaves and permissive transit hubs.",
        "alt_routes": "Shifting transit nodes from Limassol to Turkish free zones and Central Asian land corridors (Kazakhstan/Armenia re-export).",
        "vulnerabilities": "High dependency on single port container bottlenecks and recurring proxy director signatures."
    },
    "Syndicate Beta: State-Backed Capital Flight (BVI-London Shield)": {
        "ubo": "Anonymous Trust Structures acting for sanctioned oligarch families.",
        "transactions": "Sovereign wealth layering, high-end London residential property acquisitions via offshore mortgage notes, and promissory note loops.",
        "backers": "BVI confidential registry protections coupled with specialized London wealth management boutiques.",
        "alt_routes": "Rerouting asset holding vehicles through Caribbean alternative trusts (Bahamas/Nevis) and Singapore family offices.",
        "vulnerabilities": "Public registries of beneficial ownership pressures and stringent UK Unexplained Wealth Orders (UWOs)."
    },
    "Syndicate Gamma: Maritime Sanctions Evasion (APAC Transit)": {
        "ubo": "Consortium of unregistered shipping brokers operating via Singaporean shell entities.",
        "transactions": "Ship-to-ship (STS) transfer financing, cash-settled bunker fuel invoices, and trade-based laundering of raw commodities.",
        "backers": "Flag-state convenience registries and lenient maritime enforcement zones in Southeast Asia.",
        "alt_routes": "Using dark-vessel AIS spoofing and switching insurance providers to non-Western maritime syndicates.",
        "vulnerabilities": "Satellite geospatial telemetry tracking vessel dark-period anomalies and port-call mismatches."
    }
}

current_dossier = dossier_data[selected_syndicate]

# ---------------------------------------------------------
# PAPARAN UTAMA: ANALISIS GRANULAR (UBO, TRANSACTIONS, BACKERS)
# ---------------------------------------------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("Granular Intelligence Breakdown")
    st.markdown(f"""
    <div class="intel-card">
        <span class="tag-alert">CONFIDENTIAL DOSSIER</span>
        <h4 style="margin-top:10px;"><b>Target Network: {selected_syndicate.split(':')[0]}</b></h4>
        <p><b>1. Ultimate Beneficial Owner (UBO):</b><br>{current_dossier['ubo']}</p>
        <p><b>2. Transaction & Financial Vector:</b><br>{current_dossier['transactions']}</p>
        <p><b>3. State Backers & Jurisdictional Shields:</b><br>{current_dossier['backers']}</p>
        <p><b>4. Alternative Evasion Routes:</b><br>{current_dossier['alt_routes']}</p>
        <p><b>5. Strategic Vulnerabilities:</b><br>{current_dossier['vulnerabilities']}</p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("Intelligence Metrics & Threat Vector")
    st.metric(label="Network Confidence Level", value="HIGH (96.4%)", delta="Verified Cross-Match")
    st.metric(label="Financial Flow Opacity", value="CRITICAL", delta="Obfuscated Layers")
    st.metric(label="Enforcement Priority", value="TIER-1 TARGET", delta="Active Evasion")
    
    st.markdown("""
    ### Why This Precision Matters
    Agencies like CIA or MI6 do not look at names alone; they map the **financial DNA and escape vectors**. By identifying who backs them and how money flows beneath the surface, investigators can predict their next move before sanctions are bypassed.
    """)

st.markdown("---")

# ---------------------------------------------------------
# VISUALISASI RANGKAIAN MENDALAM (DEEP LINK ANALYSIS)
# ---------------------------------------------------------
st.subheader("Deep-Dive Entity Relationship & Financial Routing Graph")
st.write("Graf ini memetakan perkaitan antara UBO di belakang tabir, syarikat hadapan (*front companies*), dan laluan alternatif aliran dana.")

net = Network(height="450px", width="100%", bgcolor="#ffffff", font_color="#0f172a", directed=True)

# Tambah Nod Hubungan Mendalam
net.add_node("UBO / State Actor", label="UBO / State Actor\n(Real Mastermind)", color="#dc2626", size=32, shape="box")
net.add_node("BVI Holding", label="Offshore Holding\n(Asset Veil)", color="#1e293b", size=25)
net.add_node("Cyprus Front", label="Front Company\n(Operational Shell)", color="#2563eb", size=25)
net.add_node("UAE Layer", label="Parallel Bank / FX\n(Financial Layering)", color="#d97706", size=25)
net.add_node("Alternative Route", label="Alt Evasion Route\n(Central Asia / Dark Vessel)", color="#059669", size=28, shape="box")

# Tambah Hubungan Aliran
net.add_edge("UBO / State Actor", "BVI Holding", label="Conceals Ownership", color="#dc2626")
net.add_edge("BVI Holding", "Cyprus Front", label="Directs Capital", color="#64748b")
net.add_edge("Cyprus Front", "UAE Layer", label="Invoices & FX Flow", color="#2563eb")
net.add_edge("UAE Layer", "Alternative Route", label="Activates Evasion Vector", color="#059669")

net.save_graph("granular_network.html")
with open("granular_network.html", "r", encoding="utf-8") as f:
    html_data = f.read()
components.html(html_data, height=480)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 13px;'>PROJECT PHANTOM HUB // ARCHITECTED BY PRINCIPAL INVESTIGATOR: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b></p>",
    unsafe_allow_html=True
)
