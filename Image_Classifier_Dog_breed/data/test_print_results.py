# test_print_results.py
# ----------------------
# This script tests your print_results() function
# to make sure it displays all the expected summary
# and optional details about classification results.

from print_results import print_results


# --- Simulated results dictionary ---
# key = filename, value = [pet_label, classifier_label, match, is_dog, classifier_is_dog]
results_dic = {
    'Beagle_01141.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1],
    'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1],
    'cat_01.jpg': ['cat', 'tabby, tabby cat', 1, 0, 0],
    'Collie_03797.jpg': ['collie', 'collie', 1, 1, 1],
    'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail rabbit', 1, 0, 0],
    'Poodle_07956.jpg': ['poodle', 'standard poodle', 1, 1, 1],
    'Fox_001.jpg': ['fox', 'red fox', 1, 0, 0]
}


# --- Simulated statistics dictionary ---
# Holds computed metrics from calculates_results_stats.py
results_stats_dic = {
    'n_images': 7,
    'n_dogs_img': 4,
    'n_notdogs_img': 3,
    'n_match': 6,
    'n_correct_dogs': 4,
    'n_correct_notdogs': 3,
    'n_correct_breed': 3,
    'pct_match': 85.7,
    'pct_correct_dogs': 100.0,
    'pct_correct_notdogs': 100.0,
    'pct_correct_breed': 75.0
}


# --- Test for model type ---
model = 'vgg'


# --- Run the test ---
print("\n*** Testing print_results() ***")
print_results(results_dic, results_stats_dic, model)

print("\n*** Testing print_results() with misclassifications printed ***")
print_results(results_dic, results_stats_dic, model,
              print_incorrect_dogs=True,
              print_incorrect_breed=True)
