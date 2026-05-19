# To-Do List Application

tasks = []

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show tasks
def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add task
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

# Remove task
def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks()
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    load_tasks()
    
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run program
main()