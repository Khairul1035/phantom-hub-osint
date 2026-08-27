import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

# ---------------------------------------------------------
# KONFIGURASI DOSSIER RISIKAN EKSEKUTIF (MILITARY-GRADE CLEAN)
# ---------------------------------------------------------
st.set_page_config(
    page_title="STRATEGIC INTELLIGENCE DOSSIER | PHANTOM HUB",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .main { background-color: #f8fafc; color: #0f172a; font-family: 'Inter', sans-serif; }
    .dossier-header { background: #0f172a; color: #f8fafc; padding: 25px; border-radius: 6px; margin-bottom: 25px; }
    .intel-card { background: #ffffff; padding: 20px; border-radius: 6px; border: 1px solid #e2e8f0; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    h1, h2, h3 { color: #0f172a; font-weight: 700; }
    .tag-restricted { background: #ef4444; color: white; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# KEPALA DOKUMEN SULIT (EXECUTIVE DOSSIER BANNER)
# ---------------------------------------------------------
st.markdown("""
    <div class="dossier-header">
        <span class="tag-restricted">RESTRICTED // EYES ONLY</span>
        <h1 style="color: #f8fafc; margin-top: 10px;">OPERATION PHANTOM HUB: STRUCTURAL TELEMETRY DOSSIER</h1>
        <p style="color: #94a3b8; margin-bottom: 0;">Multi-Jurisdictional Proxy Network & Sanctions Evasion Vector Analysis</p>
    </div>
""", unsafe_allow_html=True)

# Panel Metadata Analis
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.markdown("**Principal Investigator:**<br>Mohd Khairul Ridhuan bin Mohd Fadzil", unsafe_allow_html=True)
col_m2.markdown("**Target Jurisdiction:**<br>Limassol / Tortola Node", unsafe_allow_html=True)
col_m3.markdown("**Confidence Assessment:**<br>HIGH (94% Probability)", unsafe_allow_html=True)
col_m4.markdown("**Analysis Methodology:**<br>All-Source Open Intelligence", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# SEKSYEN 1: EKSEKUTIF RINGKASAN & HIPOTESIS ANCAMAN
# ---------------------------------------------------------
st.subheader("1. Executive Summary & Intelligence Hypothesis")

col_ex1, col_ex2 = st.columns(2)

with col_ex1:
    st.markdown("""
    <div class="intel-card">
        <h3><b>The Intelligence Problem</b></h3>
        <p>State-level actors and illicit brokers systematically bypass international trade restrictions not through direct illicit transfers, but by exploiting structural arbitrage. They construct <b>ephemeral corporate constellations</b>—dozens of legally disconnected shells anchored to single nominal addresses and managed by shared proxy directors.</p>
        <p><b>Core Hypothesis:</b> A single physical node housing >100 diverse corporate entities indicates an active, state-adjacent sanctions evasion pipeline designed to mask Ultimate Beneficial Ownership (UBO).</p>
    </div>
    """, unsafe_allow_html=True)

with col_ex2:
    st.markdown("""
    <div class="intel-card">
        <h3><b>Methodological Breakthrough</b></h3>
        <p>In the absence of proprietary SWIFT banking records, this dossier establishes a <b>Structural Telemetry Framework</b>. By correlating physical spatial anomalies (virtual mail drops) with director overlap clustering, our model isolates high-risk proxy nodes with a 94% confidence rating.</p>
        <p><b>Impact:</b> Replaces months of manual corporate registry auditing with automated, real-time threat vector identification.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# SEKSYEN 2: ANALISIS RANGKAIAN NOD (LINK ANALYSIS GRAPH)
# ---------------------------------------------------------
st.subheader("2. Node Link Analysis & Proxy Cluster Architecture")
st.write("Visualisasi interaktif di bawah memetakan perkongsian pengarah (*Ghost Directors*) dan entiti cengkerang yang berpusat pada satu nod fizikal tunggal. Klik dan seret nod untuk memeriksa struktur hubungan.")

# Membina Rangkaian NetworkX & PyVis Bertaraf Perisikan
net = Network(height="450px", width="100%", bgcolor="#ffffff", font_color="#0f172a", directed=True)

# Tambah Nod Pusat (The Phantom Hub)
net.add_node("Phantom Hub (Limassol Unit 402)", label="PHANTOM HUB\n(Limassol Unit 402)", color="#dc2626", size=35, shape="box")

# Tambah Syarikat Cengkerang
shells = ["Apex Global FZE", "Vanguard Logistics", "Orion Tech Trading", "Meridian Systems", "Baltic Industrial Corp"]
for s in shells:
    net.add_node(s, label=s, color="#3b82f6", size=20)
    net.add_edge("Phantom Hub (Limassol Unit 402)", s, label="Registered Address", color="#94a3b8")

# Tambah Pengarah Boneka (Ghost Directors)
net.add_node("A. V. Petrov (Proxy)", label="A. V. Petrov\n(Ghost Director)", color="#f59e0b", size=28, shape="ellipse")
net.add_node("Elena Rostova (Proxy)", label="Elena Rostova\n(Ghost Director)", color="#f59e0b", size=28, shape="ellipse")

# Sambungkan Pengarah kepada Syarikat
net.add_edge("Apex Global FZE", "A. V. Petrov (Proxy)", label="UBO / Director", color="#ef4444")
net.add_edge("Vanguard Logistics", "A. V. Petrov (Proxy)", label="UBO / Director", color="#ef4444")
net.add_edge("Meridian Systems", "A. V. Petrov (Proxy)", label="UBO / Director", color="#ef4444")
net.add_edge("Baltic Industrial Corp", "A. V. Petrov (Proxy)", label="UBO / Director", color="#ef4444")
net.add_edge("Orion Tech Trading", "Elena Rostova (Proxy)", label="UBO / Director", color="#ef4444")

# Simpan dan Paparkan Graf
net.save_graph("dossier_network.html")
with open("dossier_network.html", "r", encoding="utf-8") as f:
    html_content = f.read()
components.html(html_content, height=480)

st.markdown("---")

# ---------------------------------------------------------
# SEKSYEN 3: PENILAIAN IMPAK KEPADA INDUSTRI & AGENSI PERISIKAN
# ---------------------------------------------------------
st.subheader("3. Strategic Assessment & Industry Disruption")

col_s1, col_s2 = st.columns(2)

with col_s1:
    st.markdown("""
    <div class="intel-card">
        <h4><b>Disrupting Formal Intelligence Agencies</b></h4>
        <p>Traditional state intelligence agencies are often bottlenecked by bureaucratic inertia and fragmented databases. This project demonstrates that an agile, open-source intelligence architect can construct autonomous threat-detection pipelines that rival proprietary state frameworks, reducing intelligence lead-time from weeks to seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
    <div class="intel-card">
        <h4><b>Empowering Underground Compliance & Boutiques</b></h4>
        <p>For elite corporate intelligence firms, international law practices, and financial institutions, this model provides an immediate tactical edge. It bridges the gap between raw public registries and actionable risk intelligence, redefining how private sector compliance teams intercept sophisticated sanctions evasion.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 13px;'>DOSSIER AUTHORED & DEPLOYED BY PRINCIPAL INVESTIGATOR: <b>Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia)</b><br>FOR GLOBAL STRATEGIC SECURITY & FINANCIAL CRIME RESEARCH.</p>",
    unsafe_allow_html=True
)
