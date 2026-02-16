# Multi-Agent Resume Screening & Candidate Evaluation System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-purple)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red)
![Backend](https://img.shields.io/badge/Backend-Flask-green)
![Status](https://img.shields.io/badge/Status-Research_Prototype-orange)

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
