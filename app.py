import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

# Konfigurasi Tema Korporat Elit
st.set_page_config(
    page_title="PROJECT PHANTOM HUB | Transnational Intelligence Grid",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #f8fafc; color: #0f172a; font-family: 'Inter', sans-serif; }
    .dossier-box { background: #ffffff; padding: 22px; border-radius: 6px; border: 1px solid #cbd5e1; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    h1, h2, h3 { color: #0f172a; font-weight: 700; }
    .tag-badge { background: #0f172a; color: white; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Header Utama Projek
st.markdown("### PROJECT PHANTOM HUB // GLOBAL INTEL GRID")
st.title("Transnational Sanctions Evasion & Shell Corridor Mapping")
st.markdown("---")

# Baris Atribusi Principal Investigator
st.markdown(
    """
    <div style="background-color: #f1f5f9; padding: 12px 18px; border-radius: 6px; border-left: 4px solid #0f172a; margin-bottom: 25px;">
        <span style="font-weight: 600; color: #0f172a;">Principal Investigator:</span> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #0f172a;">Operational Scope:</span> 5-Nation Cross-Border Node Telemetry &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #0f172a;">Classification:</span> Executive Intelligence Briefing
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR: PEMILIHAN KORIDOR 5 NEGARA
# ---------------------------------------------------------
st.sidebar.header("5-Nation Corridor Switch")
selected_nation = st.sidebar.selectbox(
    "Select Target Operational Node",
    [
        "1. Cyprus (The Operational Front-End)",
        "2. British Virgin Islands (The Ownership Vault)",
        "3. United Arab Emirates (The Trade Re-Routing Hub)",
        "4. United Kingdom (The Asset Layering Node)",
        "5. Singapore (The Asia-Pacific Transit Switch)"
    ]
)

# Maklumat Terperinci Operasi Setiap Negara
nation_details = {
    "1. Cyprus (The Operational Front-End)": {
        "role": "Virtual Office Saturation & Ghost Director Clustering",
        "mechanism": "Unstaffed commercial suites housing 100+ active trading shells simultaneously to fake operational substance.",
        "risk": "Critical (94/100) - Primary vector for dual-use technology diversion."
    },
    "2. British Virgin Islands (The Ownership Vault)": {
        "role": "Anonymous Beneficial Ownership Masking",
        "mechanism": "Nominee shareholder layers hiding state-backed actors and criminal syndicates behind impenetrable legal veils.",
        "risk": "Severe (92/100) - Ultimate holding shield for illicit capital."
    },
    "3. United Arab Emirates (The Trade Re-Routing Hub)": {
        "role": "Parallel Logistics & Dual-Use Transit",
        "mechanism": "Re-exporting restricted industrial hardware and utilizing parallel informal settlement channels.",
        "risk": "High (89/100) - Physical supply chain bottleneck bypass."
    },
    "4. United Kingdom (The Asset Layering Node)": {
        "role": "Luxury Real Estate & Wealth Laundering",
        "mechanism": "Converting illicit corporate proceeds into high-end London property portfolios via opaque offshore trusts.",
        "risk": "High (86/100) - Terminal capital laundering endpoint."
    },
    "5. Singapore (The Asia-Pacific Transit Switch)": {
        "role": "Regional Capital Re-direction",
        "mechanism": "Intermediary corporate accounts moving funds swiftly across APAC maritime trade lanes to blur transaction trails.",
        "risk": "Elevated (82/100) - High-speed liquidity distribution node."
    }
}

current_info = nation_details[selected_nation]

# ---------------------------------------------------------
# PAPARAN UTAMA: BAGAIMANA IA BEROPERASI (HOW IT OPERATES)
# ---------------------------------------------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader(f"Operational Node Analysis: {selected_nation.split('(')[0]}")
    st.markdown(f"""
    <div class="dossier-box">
        <span class="tag-badge">CORRIDOR FUNCTION</span>
        <h4 style="margin-top:10px;"><b>{current_info['role']}</b></h4>
        <p><b>How the Mechanism Operates:</b> {current_info['mechanism']}</p>
        <p><b>Systemic Threat Level:</b> {current_info['risk']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### The Intelligence Value Proposition
    By monitoring how these 5 nations interact, our telemetry engine detects **synchronised behavioral anomalies**. When a shell entity changes its registration address in Cyprus on the exact week its BVI holding structure mutates, the system flags a **Cross-Border Syndicate Alert** before enforcement agencies intervene.
    """)

with col_right:
    st.subheader("Transnational Node Matrix")
    df_nations = pd.DataFrame([
        {"Nation": "Cyprus", "Role": "Front-End Shells", "Status": "Active Surveillance"},
        {"Nation": "BVI", "Role": "Holding Vault", "Status": "Masked UBO"},
        {"Nation": "UAE", "Role": "Logistics Hub", "Status": "Re-routing"},
        {"Nation": "UK", "Role": "Asset Layering", "Status": "Real Estate Sink"},
        {"Nation": "Singapore", "Role": "Capital Switch", "Status": "Fast Transit"}
    ])
    st.dataframe(df_nations, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# VISUALISASI RANGKAIAN KORIDOR (NETWORK GRAPH)
# ---------------------------------------------------------
st.subheader("Cross-Border Intelligence Network: Connecting the 5 Nodes")
st.write("Graf visual di bawah menunjukkan bagaimana aliran kawalan dan aset bergerak merentasi koridor antarabangsa ini melalui proksi dan syarikat cengkerang.")

net = Network(height="420px", width="100%", bgcolor="#ffffff", font_color="#0f172a", directed=True)

# Tambah Nod 5 Negara
net.add_node("BVI (Holding)", label="BVI\n(Ownership Vault)", color="#1e293b", size=30, shape="box")
net.add_node("Cyprus (Front)", label="Cyprus\n(Front-End Hub)", color="#dc2626", size=30, shape="box")
net.add_node("UAE (Logistics)", label="UAE\n(Logistics Hub)", color="#2563eb", size=30, shape="box")
net.add_node("UK (Assets)", label="UK\n(Asset Layering)", color="#059669", size=30, shape="box")
net.add_node("Singapore (Capital)", label="Singapore\n(Capital Switch)", color="#d97706", size=30, shape="box")

# Tambah Aliran Hubungan Koridor
net.add_edge("BVI (Holding)", "Cyprus (Front)", label="Controls Shells", color="#64748b")
net.add_edge("Cyprus (Front)", "UAE (Logistics)", label="Diverts Cargo", color="#dc2626")
net.add_edge("UAE (Logistics)", "Singapore (Capital)", label="Routes Proceeds", color="#2563eb")
net.add_edge("BVI (Holding)", "UK (Assets)", label="Purchases Property", color="#059669")

net.save_graph("corridor_network.html")
with open("corridor_network.html", "r", encoding="utf-8") as f:
    html_data = f.read()
components.html(html_data, height=450)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 13px;'>PROJECT PHANTOM HUB // ARCHITECTED BY PRINCIPAL INVESTIGATOR: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b></p>",
    unsafe_allow_html=True
)
