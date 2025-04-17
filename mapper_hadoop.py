#!/usr/bin/env python3
import sys
import csv

# Read input from standard input (Hadoop streaming)
reader = csv.DictReader(sys.stdin)  # Reads CSV format from Hadoop's input stream

for row in reader:
    review_text = row.get('Review Text', '').strip()  # Handle missing values safely
    cloth_id = row.get('Clothing ID', '')

    if not review_text or not cloth_id.isdigit():  # Ensure valid Clothing ID
        continue

        # Skip reviews that are float (invalid data for text reviews)
    if isinstance(review_text, float):
       review_text = str(review_text)
       continue

    try:

        clothing_id = int(cloth_id)
        if clothing_id > 25:  # Apply filtering condition
                review_text = review_text.replace('\t', ' ').strip()  # Replace tabs with spaces
                print(f"{clothing_id}\t {review_text}")  # Output processed review for reducer
    except ValueError:
           continue  # Skip invalid clothing IDs


    
