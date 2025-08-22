tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split("|") for line in file.readlines()]
    except FileNotFoundError:
        print('file is not found')

def save_tasks():
    with open("tasks.txt", "w") as file:
        for t in tasks:
            file.write(f"{t[0]}|{t}\n")

def add_task():
    task = input("Enter task: ")
    tasks.append([task, "not done"])
    save_tasks()
    print("Task added!")

def remove_task():
    show_tasks()
    remove_index = int(input("Enter the task number to remove: "))
    if 0 < remove_index <= len(tasks):
        del tasks[remove_index - 1]
        save_tasks()
        print("Task removed!")
    else:
        print("Wrong index number")

def show_tasks():
    print("___Your To Do List___")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task == "done" else "❌"
        print(f"{i}. {task} [{status}]")

def mark_done():
    show_tasks()
    task_no = int(input("Enter the task number to mark as done: "))
    if 0 < task_no <= len(tasks):
        tasks[task_no - 1] = "done"
        save_tasks()
        print(f"Task '{tasks[task_no - 1]}' is marked as ✅")
    else:
        print("Invalid input")

def print_menu():
    print("__To Do List__")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task ✅")
    print("5. Exit")

def main():
    load_tasks()
    while True:
        print_menu()
        choose = input("Choose an option: ")
        if choose == "1":
            show_tasks()
        elif choose == "2":
            add_task()
        elif choose == "3":
            remove_task()
        elif choose == "4":
            mark_done()
        elif choose == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input")

main()
