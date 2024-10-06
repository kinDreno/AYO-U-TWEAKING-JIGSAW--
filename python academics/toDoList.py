
todo_list = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Clear all tasks")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\n=== To-Do List ===")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    if todo_list:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            task = todo_list.pop(task_number - 1)
            print(f"Task '{task}' deleted!")
        else:
            print("Invalid task number!")

def clear_tasks():
    todo_list.clear()
    print("All tasks cleared!")


while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
