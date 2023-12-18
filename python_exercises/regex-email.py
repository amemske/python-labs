import re
pattern = r"\w+@\w+\.\w+"

text = "Please contact support@example.com for assistance."

match = re.search(pattern, text)
if match:
    print("Found email address:", match.group())