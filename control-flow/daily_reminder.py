task = input("Please enter a task description: ")

priority = input("What is the priority of this task (high, medium, low)? ")

time_bound = input("Is this task time-bound (yes or no)? ")

match priority.lower():
    case "high":
        reminder = f"This high priority task '{task}' requires immediate attention today!"
    case "medium":
        reminder = f"This medium priority task '{task}' should be addressed soon."
    case "low":
        reminder = f"This low priority task '{task}' can be completed at your convenience."
    case _:
        reminder = "Invalid priority level entered."

if time_bound.lower() == "yes":
    reminder = f"{reminder} This task is time-bound and needs to be completed today."

print(reminder)