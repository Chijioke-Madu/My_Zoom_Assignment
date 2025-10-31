from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats

results = get_pet_labels("pet_images/")
classify_images("pet_images/", results, "resnet")
adjust_results4_isadog(results, "dognames.txt")
stats = calculates_results_stats(results)

print("\nResults Statistics Summary:\n")
for key, value in stats.items():
    print(f"{key}: {value}")
