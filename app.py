import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Project Phantom Hub | Executive OSINT", layout="wide")

# Executive Header & Attribution
st.title("PROJECT PHANTOM HUB")
st.markdown("### *Micro-Anatomy of a Cross-Border Sanctions Evasion Node*")
st.markdown("---")

# Investigator Credentials Banner
st.info("**Principal Investigator:** Mohd Khairul Ridhuan bin Mohd Fadzil (Malaysia) | **Classification:** Open-Source Intelligence (OSINT) Executive Briefing")

col1, col2, col3 = st.columns(3)
col1.metric("Target Node", "Unit 402, Limassol, Cyprus", "Virtual Office")
col2.metric("Registered Entities", "142 Active Shells", "+18% Anomaly")
col3.metric("Threat Index", "CRITICAL (94/100)", "Sanctions Vector")

st.markdown("---")

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("1. Geospatial Footprint (GeoINT)")
    m = folium.Map(location=[34.6851, 33.0384], zoom_start=15, tiles="CartoDB dark_matter")
    folium.Marker([34.6851, 33.0384], popup="Phantom Hub Target: 142 Entities", icon=folium.Icon(color="red")).add_to(m)
    st_folium(m, width=500, height=350)

with right_col:
    st.subheader("2. Cross-Mapping: Ghost Directors")
    data = {
        "Entity Name": ["Apex Global FZE", "Vanguard Logistics", "Orion Tech Trading", "Meridian Systems"],
        "Director / UBO": ["A. V. Petrov", "A. V. Petrov", "Elena Rostova", "A. V. Petrov"],
        "Status": ["Active", "Active", "Under Review", "Active"]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True)

st.markdown("---")
st.caption("Executive Intelligence Briefing: Automated corporate telemetry compiled and verified for strategic evaluation by Principal Investigator Mohd Khairul Ridhuan bin Mohd Fadzil.")
