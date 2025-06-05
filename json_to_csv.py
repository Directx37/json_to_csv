import json
import csv

# Ścieżki do plików
input_json_file = 'dane.json'
output_csv_file = 'dane.csv'

# Wczytaj dane JSON
with open(input_json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sprawdź, czy dane to lista słowników
if isinstance(data, dict):
    data = [data]

# Zapisz dane do CSV
with open(output_csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"Zapisano {len(data)} rekordów do {output_csv_file}")
