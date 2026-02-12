# AI Detailed Diagnostic Report Generator (DDR AI)

This project is an AI-powered system that converts building inspection and thermal reports into a structured client-ready Detailed Diagnostic Report (DDR).

## Problem
Engineers manually read inspection reports and thermal reports and then write a diagnostic report for clients.  
This process is slow, repetitive, and may miss important details.

## Solution
This application automates the workflow using AI:
- Reads PDF inspection reports
- Extracts observations
- Combines inspection and thermal findings
- Identifies probable root causes
- Assesses severity
- Suggests recommended actions
- Marks missing information as "Not Available"

## Tech Stack
- Python
- Streamlit (UI)
- OpenAI API (LLM reasoning)
- PyPDF (PDF reading)

## Workflow
1. Upload inspection report
2. Upload thermal report
3. System extracts text from PDFs
4. AI extracts structured observations
5. AI merges findings and performs reasoning
6. Final DDR report is generated

## How to Run Locally

Install dependencies:
