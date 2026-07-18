# 1.Write program demonstrates how to use regular expressions in Python to match and search for patterns in text.
import re
text = "My phone number is 9876543210 and email is user123@gmail.com"
# Search for a phone number
phone = re.search(r"\d{10}", text)
if phone:
    print("Phone Number Found:", phone.group())
# Search for an email address
email = re.search(r"\S+@\S+", text)
if email:
    print("Email Found:", email.group())
# Find all words starting with 'u'
words = re.findall(r"\bu\w*", text)
print("Words starting with 'u':", words)
print("\n")
