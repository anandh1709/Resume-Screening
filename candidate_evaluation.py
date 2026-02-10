from groq import Groq

import os
from dotenv import load_dotenv
from app.prompts import CANDIDATE_EVALUATION

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def evaluate_candidate(candidate_details: str, jd:str) -> str:
    prompt = CANDIDATE_EVALUATION.format(resume_json=candidate_details, jd_json=jd)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system", "content":prompt}
        ]
    )

    print("Response from Froq LLM:", response.choices[0].message.content)
    return response.choices[0].message.content
