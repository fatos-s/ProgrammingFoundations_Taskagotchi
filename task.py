# Task sizes and their corresponding coffee names and XP
SIZE_INFO = {
    "S": {"name": "Espresso", "xp": 10},
    "M": {"name": "Latte", "xp": 25},
    "L": {"name": "Frappe", "xp": 50}
}


def add_task(tasks):
    """US-01: Add a new task."""

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty!")
        return

    while True:
        size = input("Choose size (S/M/L): ").strip().upper()

        if size in SIZE_INFO:
            break

        print("Invalid size. Please choose S, M or L.")

    task = {
        "title": title,
        "size": size,
        "done": False
    }

    tasks.append(task)
    print(f"Added '{title}'!")


def show_tasks(tasks):
    """US-02: Display all open tasks."""

    open_tasks = [
        task for task in tasks
        if not task["done"]
    ]

    if not open_tasks:
        print("No open tasks. Your buddy is bored!")
        return

    print("\n--- Your Open Tasks ---")

    for number, task in enumerate(open_tasks, start=1):
        size_info = SIZE_INFO[task["size"]]

        print(
            f"{number}. {task['title']} "
            f"({size_info['name']}, +{size_info['xp']} XP)"
        )


def delete_task(tasks):
    """US-03: Delete an open task."""

    open_tasks = [
        task for task in tasks
        if not task["done"]
    ]

    if not open_tasks:
        print("No open tasks to delete.")
        return

    show_tasks(tasks)

    while True:
        try:
            number = int(
                input("Enter task number to delete (0 to cancel): ")
            )

            if number == 0:
                print("Deletion cancelled.")
                return

            if 1 <= number <= len(open_tasks):
                task_to_delete = open_tasks[number - 1]
                tasks.remove(task_to_delete)
                print("Poof! Gone.")
                return

            print(
                f"Please choose between 1 and "
                f"{len(open_tasks)} (0 to cancel)."
            )

        except ValueError:
            print("Please enter a valid number.")
            