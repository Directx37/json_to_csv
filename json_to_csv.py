import json
import csv

input_file = 'dane.json'
output_file = 'dane.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

item = raw_data['item']
output_row = {}

# Parsujemy item1
for entry in item.get('item1', []):
    key, value = entry.split(':', 1)
    output_row[f'item1_{key}'] = value

# Dodajemy pozostałe pola (np. name2, name3)
for k, v in item.items():
    if k != 'item1':
        output_row[k] = v

# Zapis do CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=output_row.keys())
    writer.writeheader()
    writer.writerow(output_row)

print(f'Zapisano dane do {output_file}')
