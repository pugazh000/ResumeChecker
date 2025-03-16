from flask import Flask, request, jsonify
from utils.extract import extract_text_from_pdf
from utils.nlp import extract_skills_experience
from utils.match import match_resume_to_job
import os

app = Flask(__name__)
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Resume Scanner API is running! Use /upload to analyze a resume."})


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["resume"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    resume_text = extract_text_from_pdf(file_path)
    resume_skills, experience = extract_skills_experience(resume_text)
    
    job_role = request.form.get("job_role", "Data Scientist")
    match_score, matched, missing = match_resume_to_job(resume_skills, job_role)
    
    return jsonify({
        "job_role": job_role,
        "match_score": match_score,
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    })

if __name__ == "__main__":
    app.run(debug=True)
