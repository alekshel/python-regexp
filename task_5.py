import re


def get_sentences(txt):
    sentence_pattern = re.compile(r"(?<=[.!?])\s+")
    return sentence_pattern.split(txt)


with open("source/text_with_emails.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(f"Кількість речень: {len(get_sentences(text))}")
    print(get_sentences(text))
