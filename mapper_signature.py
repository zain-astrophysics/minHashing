#!/usr/bin/env python3
import sys
import csv
import hashlib

# Function to generate a hash function
def hash_fn_generator(n):
    M = 1119  # Prime number for modular arithmetic
    for i in range(n):
        def hash_function(x, i=i):  # Capture 'i' in the current loop iteration
            a = 2 * i + 1  # Coefficient 'a' (must be odd for better hashing)
            b = 100 * i  # Coefficient 'b'
            return (a * x + b + 2) % M
        yield hash_function


# Generate 200 hash functions
hash_functions = list(hash_fn_generator(200))


# Function to apply minhash for a given review
def minhash(review):
    # Convert review text into shingles (individual words in this case)
    shingles = {hash(word) for word in review.split()}  # Hash each word to a number
    
    # Apply each hash function and compute the MinHash value
    minhash_values = []
    for hash_func in hash_functions:
        minhash_values.append(min(hash_func(shingle) for shingle in shingles))  # Min of hashed values
    
    return minhash_values


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
                minhash_values = minhash(review_text)
                minhash_values_str = ','.join(map(str, minhash_values))
                output_line = f"{clothing_id}\t{minhash_values_str}\n"
                # Write output using sys.stdout.write and flush immediately
                print(output_line)
                #sys.stdout.flush()  # Force flushing the output immediately 
                # Output the Review ID and its MinHash signature
                
    except ValueError:
           continue  # Skip invalid clothing IDs
