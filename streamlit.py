import streamlit as st
import requests

st.title("Resume Screening App")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!", uploaded_file.name)
    print("File uploaded successfully!", uploaded_file.name)
    
    if st.button("Screen Resume"):
        files = {"resume": uploaded_file}
        response = requests.post("http://localhost:8000/screening/", files=files)
        
        if response.status_code == 200:
            st.write("Resume Details Extracted:")
            response_data = response.json()
            st.write("Candidate Status:", response_data.get("candidate_status"))
