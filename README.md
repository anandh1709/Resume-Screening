# Multi-Agent Resume Screening & Candidate Evaluation System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red)
![Backend](https://img.shields.io/badge/Backend-Flask-green)

## 📌 Project Overview
This repository hosts a **Multi-Agent Large Language Model (LLM) Framework** designed to automate the initial phase of recruitment. Unlike standard keyword-matching tools (ATS), this system orchestrates multiple specialized AI agents to perform distinct cognitive tasks: **Job Description (JD) Extraction**, **Resume Parsing**, and **Candidate Evaluation**.

The architecture decouples the frontend and backend, utilizing a **Streamlit** interface for user interaction and a **Flask API** for robust, scalable backend processing. This project demonstrates the application of **Agentic AI** in decision-support systems to reduce human bias and improve screening efficiency.

### Key Objectives
* **Multi-Agent Orchestration:** Decomposing the complex task of "hiring" into sub-tasks handled by specialized LLM agents (Extractor, Parser, Evaluator).
* **Automated Scoring:** A quantitative pipeline that matches candidates to requirements with zero human intervention, generating a compatibility score (0-100%).
* **System Design:** Distinct separation of concerns between the interactive UI (Streamlit) and the inference engine (Flask).

---

## 📂 Repository Structure

```bash
├── candidate_evaluation.py  # Logic for the Evaluator Agent (Scoring & Matching)
├── jd_extractor.py          # Logic for the JD Parser Agent
├── resume_extractor.py      # Logic for the Resume Parser Agent
├── main.py                  # Flask API entry point for backend processing
├── streamlit.py             # Frontend UI for file upload and result visualization
├── prompts.py               # Optimized Chain-of-Thought (CoT) prompts
├── parsepdf.py              # Utility for raw PDF text extraction
├── requirements.txt         # Project dependencies
├── Job_Description.pdf      # Sample JD data for testing
└── Sample_Resume.pdf        # Sample Candidate data for testing
```
## 🛠️ Methodology & Architecture

### 1. The Multi-Agent Workflow
The system employs a cooperative agent design where outputs from one agent serve as the context for the next:

1.  **JD Extractor Agent (`jd_extractor.py`):** Analyzes the Job Description to identify hard constraints (e.g., "5+ years Python") and soft skills, filtering out noise.
2.  **Resume Parsing Agent (`resume_extractor.py`):** Extracts structured entities from candidate PDFs, normalizing diverse formats into a standard schema (Skills, Experience, Education).
3.  **Evaluator Agent (`candidate_evaluation.py`):** Performs the final logic—comparing the structured resume against the extracted JD constraints to generate a **compatibility score**.

### 2. Technical Stack
* **Frontend:** Built with **Streamlit** to provide a reactive web interface for recruiters to upload bulk resumes and view eligibility in real-time.
* **Backend:** A **Flask API** (`main.py`) serves as the inference engine, handling the heavy lifting of PDF processing and LLM calls asynchronously.
* **LLM Integration:** Utilizes **Chain-of-Thought (CoT)** prompting (`prompts.py`) to ensure agents "reason" through their evaluation rather than just guessing.


### Prerequisites
* Python 3.8+
* OpenAI API Key (or local LLM setup)

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/anandh1709/resume-screening-agent.git](https://github.com/anandh1709/resume-screening-agent.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
**Step 1: Start the Backend (Flask)**
```bash
python main.py
# The API will start on localhost:5000 (or configured port)
```
**Step 2: Start the Frontend (Streamlit)**
```bash
streamlit run streamlit.py
```

## Quick Test

To facilitate immediate testing without requiring personal data, we have included sample files in the root directory:

* Launch the Streamlit interface.
* Upload Job_Description.pdf as the target JD.
* Upload Sample_Resume.pdf as the candidate.
* The system will generate a match score and evaluation report.
