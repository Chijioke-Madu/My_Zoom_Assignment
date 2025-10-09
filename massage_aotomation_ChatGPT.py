#ChatGPT

def resource_allocator(resources, tasks):
    """Example resource allocation: divide resources evenly among tasks."""
    if tasks == 0:  # avoid division by zero
        return None, None
    
    per_task = resources // tasks
    remainder = resources % tasks
    return per_task, remainder


def main():
    while True:  # loop continues until user says 'n'
        try:
            # Ask user for input
            resources = int(input("Enter the number of cookies (resources): "))
            tasks = int(input("Enter the number of people (tasks): "))

            # Check positive values
            if resources <= 0 or tasks <= 0:
                print("Error: Please enter positive numbers for both cookies and people.")
                continue  # go back to the start of the loop

        except ValueError:
            print("Error: Invalid input. Please enter integers only.")
            continue  # restart loop on error

        # Call allocator
        per_task, remainder = resource_allocator(resources, tasks)

        if per_task is not None:  # successful allocation
            print(f"\nAllocation Results:")
            print(f"Each person gets {per_task} cookie(s).")
            print(f"Remaining cookies: {remainder}\n")
        else:
            print("Resource allocation failed. Please check your inputs.")

        # Ask if the user wants to continue
        choice = input("Do you want to optimize again? (y/n): ").strip().lower()
        if choice == 'n':
            print("Exiting resource allocation. Goodbye!")
            break


# Run main
if __name__ == "__main__":
    main()
