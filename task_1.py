import re


def get_emails_from_text(txt):
    return re.findall(r"[\w.-]+@[\w.-]+\w", txt)


with open("source/text_with_emails.txt", "r") as f:
    text = f.read()
    print(get_emails_from_text(text))
