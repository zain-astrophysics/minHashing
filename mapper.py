#!/usr/bin/env python3
import sys
import csv

# Open the local CSV file included in job
with open('reviews.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        # Extract review text and clothing ID from the current row
        review_text = row.get('Review Text', '')
        cloth_id = row.get('Clothing ID', '')

        # Ensure that we have both the review text and clothing ID
        if not review_text or not cloth_id:
            continue

        # Skip reviews that are float (invalid data for text reviews)
        if isinstance(review_text, float):
            review_text = str(review_text)
            continue

        try:
            # Filter reviews where the Clothing ID is greater than 25
            if int(cloth_id) > 25:
                # Clean the review text by removing tabs and extra spaces
                review_text = review_text.replace('\t', ' ').strip()
                print(f"{review_text}")  # Output the cleaned review text
        except ValueError:
            continue  # Skip rows with invalid clothing ID


    
