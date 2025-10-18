from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog

# Step 1: Get pet labels
results = get_pet_labels("pet_images/")

# Step 2: Classify images
classify_images("pet_images/", results, "resnet")

# Step 3: Adjust for dog classification
adjust_results4_isadog(results, "dognames.txt")

# Step 4: Print sample
print("\nSample Results After Dog Classification:\n")
for i, (filename, values) in enumerate(results.items()):
    print(f"{filename}: {values}")
    if i == 5:
        break
