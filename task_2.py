import json
import re


def validate(date):
    date_pattern = re.compile(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
    return bool(date_pattern.match(date))


with open("source/dates.json", "r") as f:
    json_dates = json.load(f)
    for json_date in json_dates:
        print(f"{json_date}: {validate(json_date)}")
