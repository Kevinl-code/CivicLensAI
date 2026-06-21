import streamlit as st
import tempfile
from datetime import datetime
from utils.pdf_export import create_pdf_report
import os

from agents.root_agent import RootAgent

st.set_page_config(
    page_title="CivicLens AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 CivicLens AI")
st.caption("Government Notice Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="." + uploaded_file.name.split(".")[-1]
    ) as tmp:

        tmp.write(uploaded_file.read())
        file_path = tmp.name

    agent = RootAgent()

    with st.spinner("Analyzing document..."):
        result = agent.process_document(file_path)

    if "error" in result:
        st.error(result["error"])
        st.stop()

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Processed",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "Timestamp",
            datetime.now().strftime("%H:%M:%S")
        )

    st.divider()

    st.subheader("📄 Document Summary")
    st.write(result["summary"])

    st.divider()

    st.subheader("📅 Deadlines & Important Dates")
    st.json(result["dates"])

    st.divider()

    st.subheader("🎯 Eligibility Requirements")
    st.json(result["eligibility"])

    st.divider()

    st.subheader("✅ Action Checklist")
    st.write(result["action_plan"])

    st.divider()

    st.subheader("📊 Statistics")

    summary_text = str(result["summary"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Characters",
            len(summary_text)
        )

    with col2:
        st.metric(
            "Words",
            len(summary_text.split())
        )

    with col3:
        st.metric(
            "Dates Found",
            len(result["dates"])
            if isinstance(result["dates"], list)
            else 1
        )
    if st.button("Generate PDF Report"):

        pdf_path = "CivicLens_Report.pdf"

        create_pdf_report(
            result,
            pdf_path
        )

        with open(pdf_path, "rb") as f:

            st.download_button(
                "📥 Download PDF",
                f,
                file_name="CivicLens_Report.pdf",
                mime="application/pdf"
            )
        st.write("Resulting PDF:")