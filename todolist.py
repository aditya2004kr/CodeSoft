def create_todo_list():
    return []

def add_task(todo_list, task):
    todo_list.append(task)
    print("Task added successfully!")

def update_task(todo_list, index, new_task):
    if index < 0 or index >= len(todo_list):
        print("Invalid index")
    else:
        todo_list[index] = new_task
        print("Task updated successfully!")

def show_todo_list(todo_list):
    if len(todo_list) == 0:
        print("No tasks in the to-do list")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")

todo_list = create_todo_list()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Show To-Do List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(todo_list, task)
    elif choice == "2":
        index = int(input("Enter the index of the task to update: ")) - 1
        new_task = input("Enter the new task: ")
        update_task(todo_list, index, new_task)
    elif choice == "3":
        show_todo_list(todo_list)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")