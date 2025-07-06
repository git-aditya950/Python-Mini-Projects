import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n Your To-Do List:")
        if not tasks:
            print("  (No tasks yet)")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
        
        print("\nOptions: [A]dd  [D]elete  [Q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
        elif choice == 'd':
            if tasks:
                try:
                    index = int(input("Enter task number to delete: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to delete.")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
