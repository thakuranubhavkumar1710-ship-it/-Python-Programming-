# task1_todo.py
todo_list = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(todo_list):
            removed = todo_list.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
