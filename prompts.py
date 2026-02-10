EXTRACT_CANDIDATE_DETAILS = """
You are an expert in resume screening. Your task is to extract relevant details from a resume.
You will recieve a resume in text format and you need to identify key information such as:
Name (string)
Email (string)
Phone (string)
Education (string or null)
Work Experience (integer or null)
Skills (list of strings)
Certifications (list of strings)

Your response must be a valid JSON object.
Use 'null' if a value is missing.

Here is the resume text:
{resume_text}

Expected Response Format:
{{
    "Name": "Walter White"
    "Email": "walter.white@gmail.com"
    "Phone": "8463826482"
    "Education": "Bachelor of Technology in Computer Science"
    "Work Experience": 8
    "Skills": ["AWS", "PowerBI", "C", "Python", "SQL"]
    "Certifications": ["AWS Solutions Architect", "AWS Machine Learning Foundations"]
}}
"""

EXTRACT_JD_DETAILS = """
You are an expert in job description analysis. Your task is to extract relevant details from a job description.
You will receive a job description in text format and you need to identify key information such as:
Job Title (string)
Job Description (string)
Responsibilities (list of strings)
Requirements (list of strings)
Preferred Qualifications (list of strings)
Your response must be a valid JSON object.
Use 'null' if a value is missing.
Here is the job description text:
{jd_text}
Expected Response Format:
{{
    "Job Title": "Software Engineer",
    "Work Experience": "3+ years",
    "Job Description": "We are looking for a Software Engineer with experience in Python and AWS
    "Preferred Qualifications": ["Experience with Python", "Familiarity with AWS"]
}}
"""

CANDIDATE_EVALUATION = """"
You are an expert in candidate evaluation. Your task is to evaluate a candidate based on their resume and the job description.
You will receive the candidate's details in JSON format and the job description in JSON format.
Here is the candidate's details:
{resume_json}
Here is the job description:
{jd_json}

Evaluate the candidate based on the following criteria:
1. Relevance of skills to the job description
2. Experience level compared to the job requirements
3. Overall fit for the position 
Selected if the jd matches 50% of the resume.
Also provide a score out of 10 based on the overall fit.

While matching skills, consider the following:
-If the skills are related to the job description, For example, if the job description requires Data Analytics and resume
has PowerBI then consider it as a match 

Your response must be a valid JSON object.
Here is the expected response format:
{{
    "Evaluation": "The candidate has relevant skills and experience for the position.",
    "Score": 8
}}
"""