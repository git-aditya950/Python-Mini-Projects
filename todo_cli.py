# todo_cli.py

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added.")
        elif choice == '3':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Enter a number.")
        elif choice == '4':
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
