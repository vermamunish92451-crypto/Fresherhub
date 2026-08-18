import os
from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

pdf = ResumePDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=False)
pdf.set_margins(15, 12, 15)
pdf.add_page()

def section_title(title):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_x(15)
    pdf.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(1.5)

def body_text(text):
    pdf.set_font('Helvetica', '', 8)
    pdf.set_x(15)
    pdf.multi_cell(180, 3.8, text)
    pdf.ln(1)

def bullet(text):
    pdf.set_font('Helvetica', '', 8)
    pdf.set_x(15)
    pdf.multi_cell(180, 3.8, '  - ' + text)

def two_col(left, right):
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_x(15)
    pdf.cell(110, 4.5, left)
    pdf.set_font('Helvetica', '', 8)
    pdf.cell(70, 4.5, right, new_x="LMARGIN", new_y="NEXT")

def one_col(text):
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_x(15)
    pdf.cell(0, 4, text, new_x="LMARGIN", new_y="NEXT")

# Name
pdf.set_font('Helvetica', 'B', 20)
pdf.cell(0, 8, 'MUNISH VERMA', new_x="LMARGIN", new_y="NEXT", align='C')

# Contact
pdf.set_font('Helvetica', '', 8)
pdf.cell(0, 4, 'Bengaluru, India | vermamunish92451@gmail.com | linkedin.com/in/munishverma | github.com/munishverma', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.ln(2)

# Line
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(3)

# PROFESSIONAL SUMMARY
section_title('PROFESSIONAL SUMMARY')
body_text('B.Tech Computer Science / Data Science graduate with strong foundation in Artificial Intelligence, Machine Learning, Python, SQL, and database technologies including MySQL and PostgreSQL. Hands-on experience building ML models for regression, classification, and predictive analytics through 6 months of internship. Familiar with Generative AI, LLMs, and RAG architectures. Proficient in TensorFlow, PyTorch, Docker, and REST APIs. Strong problem-solving, analytical, and communication skills with ability to work in collaborative team environments.')

# SKILLS
section_title('SKILLS')
bullet('Programming and AI/ML: Python (Advanced), TensorFlow, PyTorch, Scikit-learn, XGBoost, Deep Learning, NLP, Computer Vision, Generative AI, LLMs, RAG')
bullet('Databases: SQL, MySQL, PostgreSQL, MongoDB')
bullet('Cloud and DevOps: AWS (Basic), Docker, REST APIs, Git, GitHub')
bullet('Data Science: Pandas, NumPy, Matplotlib, Seaborn, Power BI, Excel')
bullet('Machine Learning: Regression, Classification, Clustering, Feature Engineering, Hyperparameter Tuning, Model Evaluation')
bullet('Soft Skills: Problem-solving, analytical thinking, communication, teamwork, cross-functional collaboration')
pdf.ln(1.5)

# INTERNSHIP EXPERIENCE
section_title('INTERNSHIP EXPERIENCE')

two_col('Data Science Intern', 'Jan 2026 - Jun 2026')
one_col('PySpyder (Analytics and ML Solutions Startup), Bengaluru')
bullet('Designed, trained, and deployed 5+ ML models for regression, classification, and predictive analytics using Python, TensorFlow, and Scikit-learn.')
bullet('Built end-to-end data pipelines using Pandas, NumPy, and SQL, processing 20K+ records with MySQL and PostgreSQL databases.')
bullet('Implemented feature engineering and hyperparameter tuning techniques, improving model accuracy by 15% on test datasets.')
bullet('Developed REST APIs for model deployment using Flask, enabling real-time predictions for client applications.')
bullet('Created visualizations and dashboards using Matplotlib, Seaborn, and Power BI for cross-functional stakeholders.')
bullet('Maintained version-controlled codebase using Git and GitHub, following review and approval procedures.')
pdf.ln(1.5)

two_col('Python Intern', 'Jun 2025 - Jul 2025')
one_col('Future Finders (Ed-tech / Software Services), Mohali')
bullet('Developed and optimized Python scripts for automated data collection and processing, reducing manual effort by 40%.')
bullet('Applied OOP principles, data structures, and file handling techniques to build reusable modules for internal workflows.')
bullet('Gathered and documented requirements for data processing tasks, ensuring accuracy and completeness.')
pdf.ln(1.5)

# PROJECTS
section_title('PROJECTS')

two_col('AI-Powered Healthcare Management System', 'Python, TensorFlow, PyTorch, SQL, MongoDB')
bullet('Built an ML-powered predictive system analyzing 12,000+ patient records using Random Forest, Gradient Boosting, and Deep Learning models, achieving 91% accuracy.')
bullet('Implemented NLP-based symptom extraction and feature engineering from diagnosis codes, demographics, and treatment history.')
bullet('Developed REST API endpoints for model inference and integrated with frontend using Docker containerization.')
bullet('Stored and retrieved patient data using MongoDB and PostgreSQL databases for scalable data operations.')
pdf.ln(1.5)

two_col('RAG-Based Document Q&A System', 'Python, LLMs, RAG, LangChain, FAISS')
bullet('Built a Retrieval-Augmented Generation system using LLMs and RAG architecture for document-based question answering.')
bullet('Implemented text chunking, embeddings generation using HuggingFace models, and vector storage using FAISS database.')
bullet('Integrated with Google Gemini API for response generation, achieving accurate context-aware answers.')
bullet('Deployed using Docker containers with REST API endpoints for real-time inference.')
pdf.ln(1.5)

two_col('E-Commerce Sales Analysis', 'Python, SQL, Power BI')
bullet('Performed end-to-end EDA on 50,000+ transaction records using SQL queries and Python, identifying trends and patterns.')
bullet('Built interactive Power BI dashboards visualizing revenue, profit margins, and customer behavior across regions.')
bullet('Delivered insights highlighting 23% revenue concentration in top 3 categories, enabling data-driven recommendations.')
pdf.ln(1.5)

two_col('Customer Churn Prediction', 'Python, TensorFlow, Scikit-learn, SQL')
bullet('Developed a binary classification model predicting customer churn with 87% accuracy using Logistic Regression, Random Forest, and neural networks.')
bullet('Handled class imbalance using SMOTE and tuned hyperparameters with GridSearchCV, reducing false negatives by 18%.')
bullet('Documented model evaluation metrics, including precision, recall, F1-score, and confusion matrix analysis.')
pdf.ln(1.5)

# EDUCATION
section_title('EDUCATION')
two_col('B.Tech, Computer Science / Data Science', '2022 - 2026')
one_col('Sardar Beant Singh State University - CGPA: 7.5')
pdf.ln(0.5)
two_col('Class XII (CBSE) - 92% - DAV High School', '2021 - 2022')
pdf.ln(0.5)
two_col('Class X (CBSE) - 94% - Ananda Marga High School', '2019 - 2020')
pdf.ln(1.5)

# CERTIFICATIONS
section_title('CERTIFICATIONS')
bullet('Python for Data Science - NPTEL / Coursera (2023)')
bullet('Machine Learning Fundamentals - Scikit-learn and Supervised Learning (2024)')
bullet('Power BI Data Analyst - Microsoft Learn / Udemy (2024)')
bullet('SQL for Data Analysis - HackerRank / Mode Analytics (2023)')

output_path = os.path.join(os.path.dirname(__file__), "..", "Munish_AI_ML_Resume.pdf")
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
print(f"Final Y position: {pdf.get_y():.1f}mm (Page height: 297mm)")
