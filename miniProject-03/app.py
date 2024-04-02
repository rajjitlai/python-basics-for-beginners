# To-do list app

'''
taskList = [] # identify the task lists 

def addTask(): # to add more tasks
    return

def viewTask(): # to view the added tasks
    return

def markCompleteTask(): # to delete the completed task
    return

def main(): # to execute all the above functions
    return

if __name__ == "__main__":
    main()
    print("The application run successfully with 0 errors")
'''

# main app start
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_completed(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index. Please enter a valid index.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(task_index)
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
