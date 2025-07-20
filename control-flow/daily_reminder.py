task = input("Enter your task for today: ")
time_bound = input("Is the task time-bound? (yes or no): ").lower()
priority = input("Enter the priority level (high, medium, low): ").lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority level.")

if time_bound == "yes":
    print("This task requires immediate attention due to time sensitivity.")
else:
    print("This task can be scheduled flexibly today.")
