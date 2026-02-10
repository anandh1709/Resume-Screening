from groq import Groq

import os
from dotenv import load_dotenv
from app.prompts import EXTRACT_JD_DETAILS

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def extract_jd_data(jd_data):
    prompt = EXTRACT_JD_DETAILS.format(jd_text=jd_data)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system", "content":prompt}
        ]
    )

    print("Response from Froq LLM:", response.choices[0].message.content)
    return response.choices[0].message.content
