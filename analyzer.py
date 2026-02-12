from openai import OpenAI
client = OpenAI()

def merge_reports(inspection, thermal):

    prompt = f"""
Combine inspection and thermal findings.

Requirements:
- Remove duplicate issues
- Mention conflicts if any
- No hallucinations
- Use only provided data

Inspection:
{inspection}

Thermal:
{thermal}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

