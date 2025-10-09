#Gemini

import sys

def resource_allocator(resources, tasks):
    """
    This function simulates a simple resource allocation.
    It divides a pool of resources (e.g., cookies) among a number of tasks (e.g., people).

    Args:
        resources (int): The total number of resources available.
        tasks (int): The total number of tasks to allocate to.

    Returns:
        tuple: A tuple containing (resources_per_task, remaining_resources) if successful,
               otherwise (None, None) if the input is invalid.
    """
    # A simple check for a valid scenario
    if tasks <= 0:
        print("Error: The number of tasks must be greater than zero.")
        return None, None
    
    # Perform integer division for allocation and find the remainder
    resources_per_task = resources // tasks
    remaining_resources = resources % tasks
    
    return resources_per_task, remaining_resources

def main():
    """
    Main function to drive the resource allocation process.
    It handles user input and validates it before calling the allocator function.
    """
    print("--- Resource Allocation Optimizer ---")
    continue_optimizing = 'y'
    
    # Loop to continue optimizing as long as the user wants to
    while continue_optimizing.lower() == 'y':
        try:
            # Prompt for and get user input
            num_resources = int(input("Enter the number of resources (e.g., cookies): "))
            num_tasks = int(input("Enter the number of tasks (e.g., people): "))
            
            # Check if inputs are positive
            if num_resources <= 0 or num_tasks <= 0:
                print("Error: Both the number of resources and tasks must be positive numbers. Please try again.")
                # The continue statement will restart the loop
                continue

            # Call the resource_allocator function with user inputs
            allocation, leftover = resource_allocator(num_resources, num_tasks)
            
            # Check if the allocation was successful
            if allocation is not None:
                # Print the results in a formatted message
                print("\n--- Allocation Results ---")
                print(f"Each of the {num_tasks} tasks will receive {allocation} resource(s).")
                print(f"There will be {leftover} resource(s) left over.")
                print("------------------------\n")

        except ValueError:
            # Handle cases where the user enters a non-integer value
            print("Invalid input. Please enter whole numbers only.")
        
        # Ask the user if they want to continue
        user_choice = input("Do you want to optimize again? (y/n): ")
        continue_optimizing = user_choice

    print("Exiting optimizer. Thank you!")
    sys.exit(0)

if __name__ == "__main__":
    main()
