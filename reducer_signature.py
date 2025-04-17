#!/usr/bin/env python3
import sys
import itertools

def minhash_similarity(minhash1, minhash2):
    """Calculate MinHash similarity by counting matching hash values."""
    matches = sum(1 for h1, h2 in zip(minhash1, minhash2) if h1 == h2)
    return matches / len(minhash1)

# Store all reviews id and their MinHash signatures
reviews = {}

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    # Split the line into Review ID and MinHash signature
    cloth_id, minhash_signature = line.split('\t', 1)
    minhash_values = list(map(int, minhash_signature.split(',')))  # Convert the MinHash signature to a list of integers

 # Assuming you have a way to store the review text (possibly passed along with the MinHash signature)
    reviews[cloud_id] = minhash_values  # Store the MinHash signature for the review ID

# Compare all pairs of reviews to calculate the MinHash similarity
for (cloud_id1, minhash1), (cloud_id2, minhash2) in itertools.combinations(reviews.items(), 2):
    similarity = minhash_similarity(minhash1, minhash2)
    
    if similarity >= 0.5:  # Only emit pairs with similarity >= 0.5
        # Output the similarity and the two reviews
        print(f"{similarity:.4f}\t{cloud_id1}\t{cloud_id2}")
