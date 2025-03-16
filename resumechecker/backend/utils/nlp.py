import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills_experience(resume_text):
    doc = nlp(resume_text)
    skills = []
    experience = []
    
    for token in doc:
        if token.ent_type_ == "ORG":  # Organizations can indicate past jobs
            experience.append(token.text)
        if token.pos_ in ["NOUN", "PROPN"]:  # Skills are often nouns
            skills.append(token.text)

    return set(skills), set(experience)
