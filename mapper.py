#!/usr/bin/env python3
import sys
import csv

# Open the local CSV file included in job
with open('reviews.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

  # Convert reviews to a list and handle float values
    reviews = [row.get('Review Text', '') for row in reader]
    reviews = [str(review) if isinstance(review, float) else review for review in reviews]
    #cloth_data = reviews['Review Text']
    #cloth_ID = reviews['Clothing ID']

    for review in reviews:
        cloth_data = review['Review Text']
        cloth_ID = review['Clothing ID']

        if not review_text or not clothing_id:
            continue

        try:
            if int(cloth_ID) > 25:  # Filter reviews with Clothing ID > 25
                reivew_text = cloth_data.replace('\t', ' ').strip()
                print(f"{review_text}")
        except ValueError:
            continue  # Skip rows with invalid clothing ID

    
