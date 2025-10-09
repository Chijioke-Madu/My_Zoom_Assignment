# Separate lists
names = ["Alice", "Bob", "Charlie", "Diana"]
grades = [75, 60, 85, 90]
assignments = [3, 5, 1, 0]

def potential_grade(current_grade, missing_assignments):
    # Each missing assignment adds 2 points
    return current_grade + (2 * missing_assignments)

# Loop through all lists at once
for name, grade, missing in zip(names, grades, assignments):
    pot_grade = potential_grade(grade, missing)
    
    # Adjust "assignment(s)" wording
    word = "assignment" if missing == 1 else "assignments"
    
    print(f"Hi {name}, your current grade is {grade}. "
          f"You have {missing} missing {word}. "
          f"If you complete them, your potential grade could be {pot_grade}.")
