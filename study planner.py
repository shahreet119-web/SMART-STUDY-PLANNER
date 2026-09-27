tasks = []

def add_task():
    print("========== ADD STUDY TASK ==========")
    subject = input("Enter subject: ")
    topic = input("Enter topic/chapter: ")
    priority = input("Enter priority (High/Medium/Low): ")
    deadline = input("Enter deadline (DD/MM/YYYY): ")
    task = {
        "subject": subject,
        "topic": topic,
        "priority": priority,
        "deadline": deadline,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("========== MY STUDY TASKS ==========")
    if len(tasks) == 0:
        print("No study tasks found.")
        return
    for i in range(len(tasks)):
        task = tasks[i]
        if task["completed"] == True:
            status = "Completed"
        else:
            status = "Pending"
        print("Task", i + 1)
        print("-------------------------")
        print("Subject  :", task["subject"])
        print("Topic    :", task["topic"])
        print("Priority :", task["priority"])
        print("Deadline :", task["deadline"])
        print("Status   :", status)

def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to complete: "))
        if number >= 1 and number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if number >= 1 and number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def show_progress():
    print("========== STUDY PROGRESS ==========")
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks available.")
        return
    completed_tasks = 0
    for task in tasks:
        if task["completed"] == True:
            completed_tasks += 1
    pending_tasks = total_tasks - completed_tasks
    progress = (completed_tasks / total_tasks) * 100
    print("Total Tasks     :", total_tasks)
    print("Completed Tasks :", completed_tasks)
    print("Pending Tasks   :", pending_tasks)
    print("Progress        :", round(progress, 2), "%")

def high_priority_tasks():
    print("========== HIGH PRIORITY TASKS ==========")
    found = False
    for i in range(len(tasks)):
        task = tasks[i]
        if task["priority"].lower() == "high" and task["completed"] == False:
            print("Task", i + 1)
            print("Subject :", task["subject"])
            print("Topic   :", task["topic"])
            print("Deadline:", task["deadline"])
            found = True
    if found == False:
        print("No high priority tasks.")

def main():
    while True:
        print("==========================================")
        print("          SMART STUDY PLANNER")
        print("==========================================")
        print("1. Add Study Task")
        print("2. View Study Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Show Study Progress")
        print("6. Show High Priority Tasks")
        print("7. Exit")
        print("==========================================")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_progress()
        elif choice == "6":
            high_priority_tasks()
        elif choice == "7":
            print("Thank you for using Smart Study Planner!")
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice!")
            print("Please enter a number from 1 to 7.")
main()
