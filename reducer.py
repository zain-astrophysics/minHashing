#!/usr/bin/env python3
import sys
import itertools

def jaccard_similarity(s1, s2):
    """Compute Jaccard Similarity between two sets of words."""
    intersection = len(s1 & s2)
    union = len(s1 | s2)
    return intersection / union if union else 0

# Read all reviews from the input
reviews = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Store each review (after processing)
    reviews.append(line)

# Convert reviews to sets of words for Jaccard similarity calculation
review_sets = [set(review.lower().split()) for review in reviews]

# Calculate pairwise Jaccard similarity and output pairs that meet threshold
for i in range(len(review_sets)):
    for j in range(i + 1, len(review_sets)):        
        similarity = jaccard_similarity(review_sets[i], review_sets[j])
        
        if similarity >= 0.5:  # Only emit pairs with similarity >= 0.5
            # Output as key-value pair: similarity as key, the pair of review texts as value
            print(f"{similarity:.4f}\t{reviews[i]}\t{reviews[j]}")

