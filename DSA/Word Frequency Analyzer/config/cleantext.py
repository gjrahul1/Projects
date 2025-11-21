import re

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]',"",text)
    return cleaned_text