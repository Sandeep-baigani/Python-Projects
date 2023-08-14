class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Todo List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add task\n2. Remove task\n3. Display tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added.")
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
            print("Task removed.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
