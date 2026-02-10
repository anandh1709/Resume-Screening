from groq import Groq

import os
from dotenv import load_dotenv
from app.prompts import EXTRACT_CANDIDATE_DETAILS

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def extract_resume_data(resume_data):
    prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text=resume_data)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system", "content":prompt}
        ]
    )

    print("Response from Froq LLM:", response.choices[0].message.content)
    return response.choices[0].message.content
