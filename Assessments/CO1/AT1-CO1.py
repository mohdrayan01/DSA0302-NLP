# 1. Regular Expressions – Resume Information Extraction
print("\nQuestion 1 Output: \n")
import re
# Sample resume data
resumes = [
"""
Name: Arjun Kumar
Email: arjun.kumar@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
""",
"""
Name: Priya Sharma
Email: priya123@yahoo.com
Phone: +91-9123456789
Skills: Java, SQL
Experience: 1 year
""",
"""
Name: Rahul Verma
Email: rahul.verma@company.in
Contact: 9988776655
Skills: Python, Java, SQL
Experience: 5 years
"""
]
# Technical skills to search
skill_list = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "NLP"
]
eligible_candidates = []
print("RESUME INFORMATION EXTRACTION")
print("=" * 60)
for resume in resumes:
    # Extract Name
    name_match = re.search(r"Name:\s*(.*)", resume)
    name = name_match.group(1) if name_match else "Not Found"
    # Extract Email
    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume
    )
    email = email_match.group() if email_match else "Not Found"
    # Extract Mobile Number
    phone_match = re.search(r"(\+91[- ]?)?[6-9]\d{9}", resume)
    phone = phone_match.group() if phone_match else "Not Found"
    # Extract Skills
    skills_found = []
    for skill in skill_list:
        if re.search(skill, resume, re.IGNORECASE):
            skills_found.append(skill)
    # Extract Experience
    exp_match = re.search(r"(\d+)\s*year", resume, re.IGNORECASE)
    experience = int(exp_match.group(1)) if exp_match else 0
    # Display Candidate Summary
    print("\nCandidate Profile")
    print("-" * 30)
    print("Name        :", name)
    print("Email       :", email)
    print("Mobile      :", phone)
    print("Skills      :", ", ".join(skills_found))
    print("Experience  :", experience, "Years")
    # Eligibility Check
    if experience >= 2 and "Python" in skills_found:
        eligible_candidates.append(name)
print("\nEligible Candidates")
print("-" * 30)
if eligible_candidates:
    for candidate in eligible_candidates:
        print(candidate)
else:
    print("No eligible candidates found.")
print("\n")

# 2. Regular Expressions – Product Search System
print("\nQuestion 2 Output: \n")
import re
# List of products
products = [
    "Python Programming Book",
    "Java Programming Guide",
    "SQL Database Handbook",
    "Machine Learning Essentials",
    "Python Basics",
    "NLP Toolkit",
    "Laptop Stand",
    "Wireless Mouse",
    "Gaming Laptop",
    "Laptop Bag",
    "Python Cookbook",
    "JavaScript for Beginners"
]
# Function to search products
def search_products(pattern, description, flags=0):
    matches = []
    for product in products:
        if re.search(pattern, product, flags):
            matches.append(product)
    print("\n" + description)
    print("-" * 40)
    if matches:
        for product in matches:
            print(product)
    else:
        print("No matching products found.")
    print("Total Matches:", len(matches))
    return len(matches)
print("=" * 60)
print("E-COMMERCE PRODUCT SEARCH SYSTEM")
print("=" * 60)
report = {}
# 1. Exact Keyword Search
report["Exact Keyword"] = search_products(
    r"^Python Basics$",
    "Exact Keyword Search"
)
# 2. Prefix Search
report["Prefix Search"] = search_products(
    r"^Python",
    "Prefix Search"
)
# 3. Suffix Search
report["Suffix Search"] = search_products(
    r"Laptop$",
    "Suffix Search"
)
# 4. Partial Keyword Search
report["Partial Search"] = search_products(
    r"Laptop",
    "Partial Keyword Search"
)
# 5. Case-Insensitive Search
report["Case-Insensitive Search"] = search_products(
    r"python",
    "Case-Insensitive Search",
    re.IGNORECASE
)
# Report
print("\n" + "=" * 60)
print("SEARCH REPORT")
print("=" * 60)
for search_type, count in report.items():
    print(f"{search_type:<30}: {count}")
print("\n")

# 3. Regular Expressions – University Registration System
print("\nQuestion 3 Output: \n")
import re
# Sample Student Details
register_no = "22CS101"
email = "john@university.edu"
course_code = "CSA0653"
semester = "Semester 5"
mobile = "9876543210"
# Validation Status
status = True
print("=" * 60)
print("UNIVERSITY STUDENT REGISTRATION VALIDATION")
print("=" * 60)
# Register Number Validation
if re.fullmatch(r"\d{2}[A-Z]{2}\d{3}", register_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False
# Institutional Email Validation
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@university\.edu", email):
    print("Institutional Email : Valid")
else:
    print("Institutional Email : Invalid")
    status = False
# Course Code Validation
if re.fullmatch(r"[A-Z]{3}\d{4}", course_code):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False
# Semester Validation
if re.fullmatch(r"Semester [1-8]", semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False
# Mobile Number Validation
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False
# Final Registration Status
print("\n" + "=" * 60)
print("FINAL REGISTRATION STATUS")
print("=" * 60)
if status:
    print("Registration Successful")
else:
    print("Registration Failed")
print("\n")