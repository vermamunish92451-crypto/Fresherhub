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
body_text('B.Tech CS/Data Science graduate with foundational understanding of databases, SQL, and Git/GitHub (repositories, branches, pull requests). Experienced in data wrangling, operational documentation, and cross-functional communication through 6 months of internship. Strong attention to detail with ability to follow security, approval, and change-management procedures. Troubleshooting-oriented with ability to gather evidence, document actions, and escalate appropriately. Curious and adaptable, committed to learning Snowflake administration. Seeking to contribute to access management, environment readiness, and data operations at Caterpillar.')

# SKILLS
section_title('SKILLS')
bullet('Databases and SQL: SQL querying, data operations, database manipulation, data validation')
bullet('Version Control: Git, GitHub (repositories, branches, pull requests, version-controlled documentation)')
bullet('Cloud and Tools: Jupyter Notebook, VS Code, Google Colab, basic cloud platform familiarity')
bullet('Data and Analytics: Python, Pandas, NumPy, Matplotlib, Seaborn, Power BI, Excel')
bullet('Documentation: Operational docs, knowledge articles, readiness checklists, runbooks, incident notes')
bullet('Compliance and Communication: Attention to detail, security, approval workflows, change-management, audit, customer-service orientation')
pdf.ln(1.5)

# INTERNSHIP EXPERIENCE
section_title('INTERNSHIP EXPERIENCE')

two_col('Data Science Intern', 'Jan 2026 - Jun 2026')
one_col('PySpyder (Analytics and ML Solutions Startup), Bengaluru')
bullet('Version-controlled 5+ ML scripts using Git/GitHub, creating pull requests and following review and approval procedures for all code changes.')
bullet('Documented pipelines, configurations, deployment steps, and runbooks to ensure reproducibility and support coverage.')
bullet('Performed data wrangling on 20K+ records using SQL and Pandas, validating quality, troubleshooting inconsistencies, and documenting resolution steps.')
bullet('Communicated findings and status updates to cross-functional stakeholders through structured reports and dashboards.')
bullet('Verified access permissions, dependencies, scripts, and documentation before scheduled training runs (environment readiness).')
bullet('Gathered diagnostic details during failures, documented root causes, and escalated unresolved issues with complete evidence.')
pdf.ln(1.5)

two_col('Python Intern', 'Jun 2025 - Jul 2025')
one_col('Future Finders (Ed-tech / Software Services), Mohali')
bullet('Developed Python scripts for automated data collection, reducing manual effort by 40% with documented workflows.')
bullet('Created reusable modules following change-management procedures for code deployment.')
bullet('Troubleshot routine errors by gathering logs, documenting actions, and escalating unresolved issues.')
pdf.ln(1.5)

# PROJECTS
section_title('PROJECTS')

two_col('E-Commerce Sales Analysis', 'Python, SQL, Power BI')
bullet('Analyzed 50,000+ records using SQL and Python, identifying top categories and seasonal trends.')
bullet('Built Power BI dashboards visualizing revenue, profit margins, and customer behavior across regions.')
bullet('Documented findings highlighting 23% revenue concentration in top 3 categories.')
pdf.ln(1.5)

two_col('AI-Powered Healthcare Management System', 'Python, Scikit-learn, SQL')
bullet('Built predictive system on 12,000+ records using Random Forest and Gradient Boosting, achieving 91% accuracy.')
bullet('Maintained documentation of data transformations, model parameters, and approval records.')
pdf.ln(1.5)

two_col('Customer Churn Prediction', 'Python, Scikit-learn, SQL')
bullet('Developed churn prediction model with 87% accuracy using Logistic Regression and Random Forest.')
bullet('Documented evaluation metrics, tuning results, and class imbalance handling for audit purposes.')
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
bullet('SQL for Data Analysis - HackerRank / Mode Analytics (2023)')
bullet('Python for Data Science - NPTEL / Coursera (2023)')
bullet('Power BI Data Analyst - Microsoft Learn / Udemy (2024)')
bullet('Machine Learning Fundamentals - Scikit-learn and Supervised Learning (2024)')

output_path = os.path.join(os.path.dirname(__file__), "..", "Munish_Caterpillar_Resume.pdf")
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
print(f"Final Y position: {pdf.get_y():.1f}mm (Page height: 297mm)")
