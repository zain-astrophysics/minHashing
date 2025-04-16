#!/usr/bin/env python3
import sys
import csv

# Open the local CSV file included in job
with open('reviews.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        review_text = row.get('Review Text')
        clothing_id = row.get('Clothing ID')

        if not review_text or not clothing_id:
            continue

        try:
            if int(clothing_id) > 25:
                review_text = review_text.replace('\t', ' ').strip()
                print(f"{review_text}")
        except ValueError:
            continue  # Skip rows with invalid numbers
