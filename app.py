import streamlit as st
import os
from analyzer import audit_pitch
from prompts import FALLBACK_AUDIT_REPORT

st.set_option("client.toolbarMode", "viewer")

# Page configuration
st.set_page_config(
    page_title="RAG Grant Auditor | Lunim Film Suite",
    page_icon="🎬",
    layout="wide"
)

# Sidebar metadata and context
with st.sidebar:
    st.title("🎬 Lunim Film Suite")
    st.subheader("RAG Grant & Investor Readiness Auditor")
    st.markdown("""
    **Developer:** AI Engineer Intern Cohort  
    **Framework:** RAG (ChromaDB + Hugging Face LLM)  
    **Objective:** Help independent creators assess pitch readiness against investor and grant mandates before formal submission.
    """)
    st.divider()
    st.info("💡 **Tip for Live Demo:** Select a Pitch from the dropdown and click 'Load Selected Pitch' to populate the latest pitch treatment.")

# Main Header
st.title("📊 Grant & Investor Readiness Diagnostic Engine")
st.markdown("Paste an independent film pitch treatment below to run an automated diagnostic audit against retrieved industry compliance mandates.")

# Helper function to read sample pitch files
def load_pitch_file(filename: str) -> str:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(f"Error: `{filename}` not found in project directory.")
        return ""

# Session state initialization for pitch input
if "pitch_input" not in st.session_state:
    st.session_state["pitch_input"] = ""

# File selector controls
col_select, col_btn = st.columns([3, 1])

with col_select:
    selected_sample = st.selectbox(
        "Choose a Sample Pitch to Load:",
        options=["sample_pitch.txt", "sample_pitch_strong.txt"],
        format_func=lambda x: "✅ Strong Pitch (Compliant / High Score)" if "strong" in x else "⚠️ Weak Pitch (High Gaps / Non-Compliant)"
    )

with col_btn:
    st.write("") # Spacer for vertical alignment
    st.write("")
    if st.button("📋 Load Selected Pitch"):
        st.session_state["pitch_input"] = load_pitch_file(selected_sample)

# Input text area
pitch_text = st.text_area(
    "Filmmaker Pitch / Treatment Text:",
    value=st.session_state["pitch_input"],
    height=280,
    placeholder="Paste pitch logline, synopsis, budget breakdown, and attached crew details here..."
)

# Action button and analysis triggering
if st.button("🚀 Analyze Pitch Readiness", type="primary"):
    if not pitch_text.strip():
        st.warning("Please enter or load a pitch treatment before running the audit.")
    else:
        with st.spinner("🔍 Retrieving grant mandates & generating diagnostic audit..."):
            try:
                # Execute primary LLM pipeline call with user/loaded text
                audit_report = audit_pitch(pitch_text)
                
                st.success("Audit Complete!")
                st.divider()
                
                with st.container():
                    st.markdown(audit_report)
                    
            except Exception as e:
                # Graceful fallback on API timeout or error
                st.warning("⚠️ Live API timeout detected. Loading cached fallback audit report for demonstration...")
                st.divider()
                
                with st.container():
                    st.markdown(FALLBACK_AUDIT_REPORT)