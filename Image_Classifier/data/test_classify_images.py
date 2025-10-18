# test_classify_images.py
from get_pet_labels import get_pet_labels
from classify_images import classify_images

# Step 1: Get the dictionary of true labels
results = get_pet_labels("pet_images/")

# Step 2: Run your classifier function using one of the CNN models
classify_images("pet_images/", results, "resnet")

# Step 3: Print a few results to check
print("\nSample Classification Results:\n")
for i, (filename, values) in enumerate(results.items()):
    print(f"Filename: {filename}")
    print(f"  True label:      {values[0]}")
    print(f"  Classifier label:{values[1]}")
    print(f"  Match:           {values[2]}")
    print()
    
    # Only show the first 10 results
    if i == 9:
        break
