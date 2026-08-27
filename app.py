import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import time

# Elite Dark Geopolitical War-Room Configuration
st.set_page_config(
    page_title="PROJECT PHANTOM-NEXUS // Geopolitical Intelligence War-Room",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #030712; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    .war-card { background: #0f172a; padding: 22px; border-radius: 8px; border: 1px solid #1e293b; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    .badge-classified { background: #991b1b; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    .badge-override { background: #b45309; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    h1, h2, h3 { color: #f8fafc; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("### PROJECT PHANTOM-NEXUS // STRATEGIC INTELLIGENCE DOSSIER")
st.title("Multi-Billion Hybrid Cartel, Shell Matrix & Geopolitical Override Engine")
st.markdown("---")

# Attribution Bar
st.markdown(
    """
    <div style="background-color: #0f172a; padding: 12px 18px; border-radius: 6px; border-left: 4px solid #ef4444; margin-bottom: 25px;">
        <span style="font-weight: 600; color: #ffffff;">Lead Strategic Investigator:</span> Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #ffffff;">Target Code:</span> Operation Phantom-Nexus &nbsp;|&nbsp; 
        <span style="font-weight: 600; color: #ffffff;">Classification:</span> EYES-ONLY / TOP SECRET
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------------
st.sidebar.header("War-Room Scenario Controls")
selected_view = st.sidebar.selectbox(
    "Select Intelligence Layer",
    [
        "1. The Front-Business Laundering Core",
        "2. The 300-Shell Company Network Matrix",
        "3. Dual-Use Cargo & Cartel Operations",
        "4. The Geopolitical Override & Dismissal Protocol"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Simulation Actions")
simulate_raid = st.sidebar.button("Execute Global Interpol Raid (04:00 UTC)")

# ---------------------------------------------------------
# MAIN DISPLAY LOGIC
# ---------------------------------------------------------
col_left, col_right = st.columns([1.3, 1])

with col_left:
    if "4. The Geopolitical Override" in selected_view or simulate_raid:
        if simulate_raid:
            with st.spinner("Executing simultaneous multi-nation raids across Geneva, Cyprus, and BVI..."):
                time.sleep(1.2)
            st.error("INTERPOL RAID SUCCESSFUL: All primary suspects detained, assets frozen.")
            time.sleep(1.0)
            st.warning("GEOPOLITICAL OVERRIDE TRIGGERED: Incoming classified Washington/Eurasia directive received. Suspending prosecution...")
        
        st.markdown("""
        <div class="war-card" style="border: 1px solid #b45309;">
            <span class="badge-override">STATE IMMUNITY OVERRIDE (SECTION 9-B)</span>
            <h3 style="margin-top:15px;">The Geopolitical Plot Twist</h3>
            <p><b>1. The Intervention:</b> 48 hours post-raid, international prosecutors received a classified diplomatic order to halt all proceedings and release the suspects.</p>
            <p><b>2. State-Backed Proxies:</b> The microchip and dual-use supply chain networks were covert state sub-contractors moving hardware to strategic conflict zones without official military footprint.</p>
            <p><b>3. Final Disposition:</b> Charges expunged. Assets unfrozen and transferred to strategic offshore accounts. The network remains fully operational under diplomatic shield.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="war-card">
            <span class="badge-classified">ACTIVE HYBRID SYNDICATE DOSSIER</span>
            <h3 style="margin-top:15px;">Phantom-Nexus Architecture Breakdown</h3>
            <p><b>1. Front Businesses (The Laundering Machines):</b> Fast-food chains and local eateries injecting bulk cash via manipulated POS records; luxury real estate converting funds into physical assets; charity foundations masking cross-border transfers and securing social immunity.</p>
            <p><b>2. Dark Core Operations:</b> Dual-use microchip smuggling for state-aligned drone fabrication, parallel cartel drug networks, and terrorist financing channels.</p>
            <p><b>3. Corporate Veil:</b> Over 300 interconnected shell entities across BVI, Cyprus, and Labuan obfuscating the Ultimate Beneficial Owners (UBOs).</p>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.subheader("Telemetry & Financial Metrics")
    st.metric(label="Total Illicit Volume", value="$840,000,000 USD", delta="Multi-Billion Scale")
    st.metric(label="Active Shell Companies", value="312 Entities", delta="High Obfuscation")
    st.metric(label="Interpol Raid Status", value="ABORTED BY DIPLOMATIC VETO", delta="State Immunity Active")
    
    st.markdown("""
    ### Strategic Reality
    In high-stakes geopolitics, the most powerful cartels do not hide in the shadows—they operate behind corporate boards, charity foundations, and state-backed intelligence umbrellas.
    """)

st.markdown("---")

# ---------------------------------------------------------
# NETWORK GRAPH VISUALIZATION
# ---------------------------------------------------------
st.subheader("Phantom-Nexus: Corporate Fronts, Shell Matrix & State Shield Network")
st.write("This graph maps how illicit drug and microchip capital flows through legitimate front businesses (restaurants, real estate, charities) into 300+ shell companies, ultimately protected by geopolitical overrides.")

net = Network(height="460px", width="100%", bgcolor="#0f172a", font_color="#f3f4f6", directed=True)

# Add Nodes
net.add_node("Cartel / Dual-Use Revenue\n($840M USD)", label="Cartel & Microchip Revenue\n($840M USD)", color="#dc2626", size=32, shape="box")
net.add_node("Front Businesses\n(Fast-Food, Real Estate, Charities)", label="Front Businesses\n(Restaurants & Charities)", color="#d97706", size=26)
net.add_node("300+ Shell Network\n(BVI / Cyprus / Labuan)", label="300+ Shell Matrix\n(Layering Hub)", color="#2563eb", size=26)
net.add_node("Geopolitical Immunity\n(State-Backed Override)", label="Geopolitical Immunity\n(Diplomatic Shield)", color="#059669", size=32, shape="box")

# Add Edges
net.add_edge("Cartel / Dual-Use Revenue\n($840M USD)", "Front Businesses\n(Fast-Food, Real Estate, Charities)", label="Injects Cash & Assets", color="#dc2626")
net.add_edge("Front Businesses\n(Fast-Food, Real Estate, Charities)", "300+ Shell Network\n(BVI / Cyprus / Labuan)", label="Launders via Multi-Nodes", color="#d97706")
net.add_edge("300+ Shell Network\n(BVI / Cyprus / Labuan)", "Geopolitical Immunity\n(State-Backed Override)", label="Protected by Veto", color="#059669")

net.save_graph("nexus_network.html")
with open("nexus_network.html", "r", encoding="utf-8") as f:
    html_data = f.read()
components.html(html_data, height=490)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 13px;'>PROJECT PHANTOM-NEXUS // ARCHITECTED BY LEAD STRATEGIC INVESTIGATOR: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b></p>",
    unsafe_allow_html=True
)
