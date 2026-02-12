from pypdf import PdfReader
from openai import OpenAI

client = OpenAI()

# -------- READ PDF ----------
def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text


# -------- EXTRACT OBSERVATIONS ----------
def extract_observations(text):

    prompt = f"""
You are a building inspection analyst.

Extract factual observations only.

Rules:
- Do NOT guess
- If information missing write "Not Available"
- Return STRICT JSON

Format:
{{
 "areas":[
   {{
     "area_name":"",
     "observation":"",
     "evidence":""
   }}
 ]
}}

Report:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

