
todoList = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Clear all tasks")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    todoList.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if len(todoList) == 0:
        print("No tasks in the list.")
    else:
        print("\n=== To-Do List ===")
        for i in range(len(todoList)):
            print(f"{i}. {todoList[i]}")

def delete_task():
    view_tasks()
    if todoList:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(todoList):
            task = todoList.pop(task_number - 1)
            print(f"Task '{task}' deleted!")
        else:
            print("Invalid task number!")

def clear_tasks():
    todoList.clear()
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
