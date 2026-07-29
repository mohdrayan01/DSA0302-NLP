# 1.Intelligent Email and Password Validator using Regular Expressions
print ("\n Question 1 Output: \n")
import re
# Sample Inputs
email = "john_doe123@gmail.com"
password = "Pass@123"
mobile = "9876543210"
print("=" * 60)
print("INTELLIGENT EMAIL AND PASSWORD VALIDATOR")
print("=" * 60)
# Email Validation
email_pattern = r"^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$"
if re.fullmatch(email_pattern, email):
    print("Email          : Valid Email")
else:
    print("Email          : Invalid Email")
# Password Validation
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!])[A-Za-z\d@#$%&!]{8,}$"
if re.fullmatch(password_pattern, password):
    print("Password       : Strong Password")
else:
    print("Password       : Weak Password")
# Mobile Number Validation
mobile_pattern = r"^[6-9]\d{9}$"
if re.fullmatch(mobile_pattern, mobile):
    print("Mobile Number  : Valid Mobile Number")
else:
    print("Mobile Number  : Invalid Mobile Number")
print("\n")


# 2. Design a Finite State Automata (FSA) Simulator
print ("Question 2 Output: \n")
# DFA Description
states = ['q0', 'q1', 'q2']
alphabet = ['a', 'b']
# Transition Table
transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
initial_state = 'q0'
final_states = ['q2']
# Accept multiple input strings
n = int(input("Enter the number of input strings: "))
for i in range(n):
    string = input("\nEnter input string: ")
    current_state = initial_state
    path = [current_state]
    valid = True
    for ch in string:
        if ch not in alphabet:
            valid = False
            break
        current_state = transitions[current_state][ch]
        path.append(current_state)
    print("Transition Path:")
    print(" → ".join(path))
    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
print("\n")


# 3. Smart Pattern Matching Engine using Regular Expressions
print("Question 3 Output: \n")
import re
# Sample Text
text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
machine learning
network security
"""
while True:
    print("\nSMART PATTERN MATCHING ENGINE")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        result = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
        print("Dates Found:", result)
    elif choice == 2:
        result = re.findall(r"\b[6-9]\d{9}\b", text)
        print("Phone Numbers Found:", result)
    elif choice == 3:
        result = re.findall(r"#\w+", text)
        print("Hashtags Found:", result)
    elif choice == 4:
        result = re.findall(r"@\w+", text)
        print("Mentions Found:", result)
    elif choice == 5:
        prefix = input("Enter prefix: ")
        pattern = r"\b" + prefix + r"\w*"
        result = re.findall(pattern, text, re.IGNORECASE)
        if result:
            print("Matching Words:", result)
        else:
            print("No matching words found.")
    elif choice == 6:
        suffix = input("Enter suffix: ")
        pattern = r"\b\w*" + suffix + r"\b"
        result = re.findall(pattern, text, re.IGNORECASE)
        if result:
            print("Matching Words:", result)
        else:
            print("No matching words found.")
    elif choice == 7:
        word = input("Enter word to search: ")
        pattern = r"\b" + re.escape(word) + r"\b"
        result = re.findall(pattern, text, re.IGNORECASE)
        if result:
            print("Word Found:", result)
        else:
            print("Word Not Found.")
    elif choice == 8:
        print("Program Exited.")
        break
    else:
        print("Invalid Choice!")
print("\n")