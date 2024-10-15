import csv
import json
import os

locales = [folder for folder in os.listdir("src/locales") if "." not in folder]
translations = {}

for locale in locales:
    with open(f"src/locales/{locale}/translation.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    for key, value in data.items():
        if key not in translations:
            translations[key] = {}

        translations[key][locale] = value

rows = [{"key": key, **value} for key, value in sorted(translations.items())]

with open(f"translation_template.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
