JOB_SKILLS = {
    "Data Scientist": {"Python", "Machine Learning", "Deep Learning", "Pandas", "NumPy"},
    "Cloud Engineer": {"AWS", "Docker", "Terraform", "Kubernetes", "Lambda"}
}

def match_resume_to_job(resume_skills, job_role):
    required_skills = JOB_SKILLS.get(job_role, set())
    matched_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills - matched_skills
    match_score = len(matched_skills) / len(required_skills) * 100 if required_skills else 0

    return match_score, matched_skills, missing_skills
