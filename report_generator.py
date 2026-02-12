from openai import OpenAI
client = OpenAI()

def generate_ddr(merged_data):

    prompt = f"""
Create a client-friendly Detailed Diagnostic Report.

Sections required:
1 Property Issue Summary
2 Area-wise Observations
3 Probable Root Cause
4 Severity Assessment (Low/Medium/High with reason)
5 Recommended Actions
6 Additional Notes
7 Missing or Unclear Information

Rules:
- Simple language
- No technical jargon
- No invented facts
- If missing -> "Not Available"

Data:
{merged_data}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

