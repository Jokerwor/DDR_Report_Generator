# 🏢 AI Detailed Diagnostic Report Generator (DDR AI)

An AI-powered application that automates the generation of **Detailed Diagnostic Reports (DDR)** from building inspection and thermal imaging reports. The system extracts key observations, analyzes findings using Large Language Models (LLMs), and produces structured, client-ready diagnostic reports.

---

## 📖 Overview

Preparing diagnostic reports manually from inspection documents is time-consuming, repetitive, and prone to human error. This project streamlines the process by automatically extracting information from PDF reports, identifying defects, analyzing probable causes, assessing severity, and generating professional reports.

---

## ✨ Features

- 📄 Automatic PDF report processing
- 🔍 Intelligent extraction of inspection observations
- 🌡️ Thermal report analysis
- 🧠 AI-powered reasoning using OpenAI
- ⚠️ Root cause identification
- 📊 Severity assessment
- 💡 Recommendation generation
- 📝 Structured Detailed Diagnostic Report (DDR)
- 🚀 Streamlit-based interactive interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI API
- PyPDF2 / PyMuPDF
- Pandas
- Regular Expressions
- JSON

---

## 📂 Project Structure

```
DDR_Report_Generator/
│
├── app.py                  # Streamlit application
├── analyzer.py             # AI reasoning and analysis
├── extractor.py            # PDF text extraction
├── report_generator.py     # DDR report creation
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Workflow

1. Upload Inspection Report (PDF)
2. Upload Thermal Report (PDF)
3. Extract text from reports
4. Identify observations and defects
5. Analyze findings using AI
6. Determine severity and root causes
7. Generate recommendations
8. Create a structured Detailed Diagnostic Report

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Jokerwor/DDR_Report_Generator.git
```

Navigate to the project

```bash
cd DDR_Report_Generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📌 Example Use Cases

- Building Inspection Automation
- Structural Assessment
- Thermal Imaging Analysis
- Civil Engineering Reports
- Facility Maintenance
- Infrastructure Diagnostics

---

## 📊 Advantages

- Saves report preparation time
- Reduces manual effort
- Improves reporting consistency
- AI-assisted defect analysis
- Client-ready professional reports
- Easy-to-use web interface

---

## 📈 Future Improvements

- Multi-language report generation
- OCR support for scanned PDFs
- Image-based defect detection
- Cloud deployment
- Report export to DOCX/PDF
- Dashboard and analytics
- Support for multiple LLM providers

---

## 👨‍💻 Author

**Rishi Kumar Srivastav**

GitHub: https://github.com/Jokerwor

LinkedIn: https://linkedin.com/in/rishi-srivastav

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
