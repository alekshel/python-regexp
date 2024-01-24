import re

from task_1 import get_emails_from_text


def get_name_and_domain_from_email(email):
    email_pattern = re.compile(r"(?P<name>[\w.-]+)@(?P<domain>[\w.-]+\.\w+)")
    match = email_pattern.match(email)
    return {"name": match.group("name"), "domain": match.group("domain")}


with open("source/text_with_emails.txt", "r") as f:
    text = f.read()
    emails = get_emails_from_text(text)
    for _email in emails:
        print(get_name_and_domain_from_email(_email))
