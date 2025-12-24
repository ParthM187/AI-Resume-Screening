# jd_skill_extractor.py

from skill_vocabulary import SKILL_VOCAB

def extract_jd_skills_from_text(jd_text: str):
    jd_text = jd_text.lower()
    found_skills = set()

    for skill in SKILL_VOCAB:
        if skill.lower() in jd_text:
            found_skills.add(skill)

    return sorted(found_skills)

