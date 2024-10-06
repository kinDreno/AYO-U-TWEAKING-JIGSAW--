
viewTasks = []

def exit():

    if len(viewTasks) == 0:
        print("No tasks")
    for i in range(len(viewTasks)):
        print(f"{i + 1}. {viewTasks[i]}")

def runCode():

    while True:
        task = input("Enter a task (or type exit to finish): ")
        if task.lower() == "exit":
            exit()
            break
        viewTasks.append(task)
runCode()