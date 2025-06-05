import json
import csv

input_file = 'dane.json'
output_file = 'dane.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

items = raw_data['items']
rows = []

# Przetwarzamy każdy obiekt
for item in items:
    row = {}
    
    # Rozbij item1
    for entry in item.get('item1', []):
        key, value = entry.split(':', 1)
        row[f'item1_{key}'] = value

    # Dodaj pozostałe pola
    for k, v in item.items():
        if k != 'item1':
            row[k] = v

    rows.append(row)

# Zbierz wszystkie możliwe nagłówki
all_keys = set()
for row in rows:
    all_keys.update(row.keys())

# Zapisz do CSV
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=sorted(all_keys))
    writer.writeheader()
    writer.writerows(rows)

print(f"Zapisano {len(rows)} rekordów do {output_file}")
