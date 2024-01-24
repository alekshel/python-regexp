import json
import re


def validate(phone):
    phone_pattern = re.compile(r"^\+38 \(0\d{2}\) \d{3}-\d{2}-\d{2}$")
    return bool(phone_pattern.match(phone))


with open("source/phones.json", "r") as f:
    json_phones = json.load(f)
    for json_phone in json_phones:
        print(f"{json_phone}: {validate(json_phone)}")
