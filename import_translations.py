import csv
import json
import os
import sys

data = {}

with open(sys.argv[1], "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")

    languages = [
        fieldname for fieldname in reader.fieldnames if fieldname and fieldname != "key"
    ]

    for row in reader:
        if row["key"].strip() == "":
            continue

        data[row["key"]] = {language: row[language].strip() for language in languages}


for language in languages:
    locale_data = dict(sorted((key, row[language]) for key, row in data.items()))

    if not os.path.exists(f"src/locales/{language}"):
        os.makedirs(f"src/locales/{language}")

    with open(
        f"src/locales/{language}/translation.json", "w+", encoding="utf-8"
    ) as file:
        json.dump(locale_data, file, ensure_ascii=False, indent=2)
