from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from extractor import read_pdf, extract_observations
from analyzer import merge_reports
from report_generator import generate_ddr

st.set_page_config(page_title="AI DDR Generator", layout="wide")

st.title("🏠 AI Detailed Diagnostic Report Generator")

st.write("Upload the inspection and thermal reports to automatically generate a client-ready diagnostic report.")

inspection_file = st.file_uploader("Upload Inspection Report", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report", type="pdf")

if st.button("Generate DDR Report"):

    if inspection_file is None or thermal_file is None:
        st.error("Please upload BOTH reports.")
    else:
        with st.spinner("Analyzing documents... This may take 20–40 seconds ⏳"):

            # Read PDFs
            inspection_text = read_pdf(inspection_file)
            thermal_text = read_pdf(thermal_file)

            # Extract observations
            obs1 = extract_observations(inspection_text)
            obs2 = extract_observations(thermal_text)

            # Merge findings
            merged = merge_reports(obs1, obs2)

            # Generate final report
            final_report = generate_ddr(merged)

        st.success("DDR Report Generated!")

        st.subheader("Generated Diagnostic Report")
        st.text_area("", final_report, height=600)
