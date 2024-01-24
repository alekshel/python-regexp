import json

import pytest

from task_1 import get_emails_from_text
from task_2 import validate as validate_date
from task_3 import get_name_and_domain_from_email
from task_4 import validate as validate_phone
from task_5 import get_sentences


@pytest.fixture
def sample_text_with_emails():
    with open("source/text_with_emails.txt", "r", encoding="utf-8") as f:
        return f.read()


def test_get_emails_from_text(sample_text_with_emails):
    emails = get_emails_from_text(sample_text_with_emails)

    expected_emails = [
        "john.doe123@example.com",
        "sarah.smith456@gmail.com",
        "codingmaster_89@hotmail.com",
        "webdevpro@outlook.com",
        "techgeek007@yahoo.com",
    ]

    assert len(emails) == len(expected_emails)
    assert all(email in expected_emails for email in emails)


@pytest.fixture
def sample_dates():
    with open("source/dates.json", "r") as f:
        return json.load(f)


def test_dates_validate(sample_dates):
    true_indexes = [0, 5]

    for index, date in enumerate(sample_dates):
        if index in true_indexes:
            assert validate_date(date) is True
            continue
        assert validate_date(date) is False


def test_get_name_and_domain_from_email(sample_text_with_emails):
    answers = [
        {"name": "john.doe123", "domain": "example.com"},
        {"name": "sarah.smith456", "domain": "gmail.com"},
        {"name": "codingmaster_89", "domain": "hotmail.com"},
        {"name": "webdevpro", "domain": "outlook.com"},
        {"name": "techgeek007", "domain": "yahoo.com"},
    ]

    emails = get_emails_from_text(sample_text_with_emails)

    for email in emails:
        assert get_name_and_domain_from_email(email) in answers


@pytest.fixture
def sample_phones():
    with open("source/phones.json", "r") as f:
        return json.load(f)


def test_phones_validate(sample_phones):
    true_indexes = [0]

    for index, phone in enumerate(sample_phones):
        if index in true_indexes:
            assert validate_phone(phone) is True
            continue
        assert validate_phone(phone) is False


def test_get_sentences(sample_text_with_emails):
    sentences = get_sentences(sample_text_with_emails)
    assert len(sentences) == 13
