task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that should be completed when you have free time.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")