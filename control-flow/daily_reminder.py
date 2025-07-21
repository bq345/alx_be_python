task = input("Enter your task: ")
prioprity = input("Enter the priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match prioprity:
    case "high":
        if time == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:  
            print(f"'{task}' is a high priority task that should be completed soon!")
    case "medium":
        if time == "yes":
            print(f"'{task}' is a medium priority task that should be completed within the week!")
        else:      
            print(f"'{task}' is a medium priority task that can be scheduled for later!")
    case "low": 
        if time == "yes":
            print(f"'{task}' is a low priority task that can be done when convenient!")
        else:      
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _: 
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
