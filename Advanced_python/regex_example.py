import re

# Sample text
text = "The rain in Spain"
# Search for "ain"
match = re.search(r'ain', text)
if match:
    print("Found:", match.group())  # Outputs: Found: ain