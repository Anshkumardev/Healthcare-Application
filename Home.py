import streamlit as st

# Page Configuration
st.set_page_config(page_title="Healthcare Accessibility Dashboard", layout="wide")

# ──────────────────────────────────────────────────────
# Title & Subtitle
# ──────────────────────────────────────────────────────
st.markdown("""
<h1 style='font-size: 2.8rem; margin-bottom: 0;'>🏥 Healthcare Accessibility Dashboard</h1>
<p style='font-size: 1.2rem; color: #555; margin-top: 0.4rem;'>
  Explore healthcare access, risks, and outcomes across U.S. census tracts using AI-driven insights.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ──────────────────────────────────────────────────────
# Hero / Introduction Section
# ──────────────────────────────────────────────────────
st.markdown("""
<div style="background-color: #f0f4fa; padding: 1.5rem 2rem; border-left: 5px solid #4a7bd0; border-radius: 8px; margin-bottom: 2.5rem;">
  <p style="font-size: 1.1rem; color: #333;">
  <strong>Bringing together geospatial, clinical, and socioeconomic datasets,</strong> this platform enables deep exploration of healthcare accessibility gaps at the census-tract level.
  Navigate through dynamic maps, comparative analytics, and a powerful natural language Q&A assistant to discover key disparities and opportunities for improvement.
  </p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────
# Features Overview
# ──────────────────────────────────────────────────────
st.markdown("## Platform Features")
st.markdown("")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🗺️ Interactive Health Maps")
    st.markdown("""
    - Visualize healthcare access, provider density, and population health across U.S. tracts.
    - Apply filters by city, county, or metric for targeted exploration.
    """)

    st.markdown("### 📊 Top & Bottom Rankings")
    st.markdown("""
    - Identify tracts with highest or lowest values for selected indicators.
    - View sortable tables and dynamic bar charts for benchmarking.
    """)

    st.markdown("### 🧠 AI-Powered Tract Q&A")
    st.markdown("""
    - Ask natural-language questions about health risks or resource gaps.
    - Powered by a multi-agent LangChain system combining retrieval (RAG) and pandas-based reasoning.
    """)

with col2:
    st.markdown("### 📈 Risk & Outcome Visualizations")
    st.markdown("""
    - Analyze preventive care, chronic disease prevalence, and health burdens.
    - Pinpoint high-risk tracts with poor access and outcomes.
    """)

    st.markdown("### 🔍 Metric Comparisons")
    st.markdown("""
    - Compare multiple socioeconomic and clinical metrics side-by-side.
    - Normalize by population or tract area for accurate comparisons.
    """)

# ──────────────────────────────────────────────────────
# Call to Action
# ──────────────────────────────────────────────────────
st.markdown("")

st.markdown("""
<div style="background-color: #eef3fa; padding: 1.2rem 1.8rem; border-left: 5px solid #4a7bd0; border-radius: 8px; margin-top: 2rem;">
  <h4 style="margin-bottom: 0.5rem;">🧭 How to Get Started</h4>
  <p style="font-size: 1rem; color: #333;">
    Use the <strong>sidebar</strong> to navigate between Health Maps, Rankings, Risk Visualizations, and the <strong>City Health Q&A Assistant</strong>.  
    Ask questions, explore patterns, and uncover hidden gaps in healthcare access.
  </p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Powered by GeoPandas, FAISS, HuggingFace, LangChain, and OpenAI APIs.")
