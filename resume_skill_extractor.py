import pdfplumber
from skill_vocabulary import SKILL_VOCAB

def extract_resume_skills(resume_file):
    text = ""

    with pdfplumber.open(resume_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "

    text = text.lower()
    extracted = []

    for skill in SKILL_VOCAB:
        if skill in text:
            extracted.append(skill)

    return list(set(extracted))
