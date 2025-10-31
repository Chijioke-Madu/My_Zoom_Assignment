# test_get_pet_labels.py

from get_pet_labels import get_pet_labels

# Test directory — make sure this matches the name of your folder
test_dir = "pet_images/"

# Run the function
results_dic = get_pet_labels(test_dir)

# Print the first few results
print("Number of Images:", len(results_dic))
print("\nSample Output:\n")

for filename, label in list(results_dic.items())[:10]:
    print(f"Filename: {filename}  -->  Label: {label[0]}")

# Run the function
results = get_pet_labels("pet_images/")

# Check one example
print(type(results["Boston_terrier_02285.jpg"]))
print(results["Boston_terrier_02285.jpg"])