# Resume Scanner (AI-Powered Resume Matching)

This project is an AI-powered **Resume Scanner** that extracts skills and experience from a resume PDF and matches them against a desired job role using NLP techniques.

---
## **🚀 Features**
✅ Extracts text from PDFs using **PyMuPDF (pymupdf)**  
✅ Analyzes skills and experience using **spaCy NLP**  
✅ Matches resumes to a **specified job role**  
✅ Deployed as a **serverless API** using **AWS Lambda & Zappa**  
✅ **DynamoDB integration** for storing scanned resumes (Optional)  

---
## **📂 Folder Structure**
```
resume-scanner/
├── backend/               # Flask Backend (AWS Lambda)
│   ├── app.py            # Main API
│   ├── requirements.txt  # Dependencies
│   ├── zappa_settings.json  # Zappa Deployment Config
│   ├── utils/            # Helper Functions
│   │   ├── extract.py    # PDF Text Extraction
│   │   ├── nlp.py        # NLP Skill Extraction
│   │   ├── match.py      # Job Role Matching
│   ├── temp/             # Temporary folder for uploaded resumes
│
├── frontend/              # Web UI (AWS S3)
│   ├── index.html        # Frontend UI
│   ├── static/           # Static Files
│   │   ├── css/          # CSS Files
│   │   │   ├── style.css  # Main Stylesheet
│   │   ├── js/           # JavaScript Files
│   │   │   ├── script.js  # Handles API Calls
│
├── deployment/            # Deployment Config & Scripts
│   ├── s3_upload.sh      # Script to upload frontend to S3
│   ├── zappa_deploy.sh   # Script to deploy backend to AWS Lambda
│
├── lambda_layer/          # AWS Lambda Layer for dependencies
│   ├── python/           # Python Packages
│   │   ├── spacy/       # SpaCy NLP Model for AWS Lambda
│   │   │   ├── data/
│   │   │   │   ├── en_core_web_sm/
│
├── README.md              # Project Documentation
├── .gitignore             # Ignore unnecessary files
```

---
## **🔧 Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/pugazh000/resume-scanner.git
cd resume-scanner/backend
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Download NLP Model**
```sh
python -m spacy download en_core_web_sm
```

---
## **🖥️ Running the Application Locally**
```sh
python app.py
```
✅ The API will run at `http://127.0.0.1:5000`

---
## **🛠️ AWS Lambda Deployment with Zappa**

### **1️⃣ Initialize Zappa**
```sh
zappa init
```
🔹 Select AWS Region (e.g., `ap-southeast-1`)  
🔹 Choose an S3 Bucket (or let Zappa create one)  

### **2️⃣ Deploy to AWS**
```sh
zappa deploy dev
```
✅ The API will be available at: `https://your-api-url.amazonaws.com/dev`

### **3️⃣ Updating Deployment**
```sh
zappa update dev
```

### **4️⃣ Rollback (if needed)**
```sh
zappa rollback dev
```

---
## **🔗 API Endpoints**

| Method | Endpoint       | Description                    |
|--------|--------------|--------------------------------|
| `POST` | `/upload`    | Uploads a resume PDF for processing |
| `GET`  | `/`          | Health check route            |

---
## **🗂️ Sample API Usage**
### **Uploading a Resume**
```sh
curl -X POST "https://your-api-url.amazonaws.com/dev/upload" \
     -F "resume=@sample_resume.pdf" \
     -F "job_role=Data Scientist"
```
📌 **Response Example:**
```json
{
  "job_role": "Data Scientist",
  "match_score": 85,
  "matched_skills": ["Python", "Machine Learning", "NLP"],
  "missing_skills": ["Deep Learning", "Big Data"]
}
```

---
## **🛡️ Security Best Practices**
✅ **NEVER hardcode AWS credentials.** Use IAM roles instead.  
✅ **Use `.gitignore`** to exclude sensitive files like `venv/`  
✅ **Enable CORS in API Gateway** to prevent frontend issues  

---
## **📌 Contribution Guidelines**
💡 Open issues and pull requests to improve this project!  
📩 Feel free to suggest features or report bugs.  

---
## **📜 License**
This project is open-source and available under the **MIT License**.

---
🚀 **Now your project is GitHub-ready! Just upload this README.md and your code.** 🔥

