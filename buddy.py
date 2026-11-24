from user_input import SIZE_INFO


def feed_buddy(buddy, size):
    """US-04: Feed the buddy after completing a task."""

    reward = SIZE_INFO[size]

    buddy["caffeine"] = min(
        100, buddy["caffeine"] + reward["caffeine"]
    )

    print(
        f"You fed {buddy['name']} a {reward['name']}! "
        f"+{reward['xp']} XP, "
        f"+{reward['caffeine']}% caffeine"
    )

def finish_task(tasks, buddy):
    """US-04: Complete an open task and feed the buddy."""

    open_tasks = [
        task for task in tasks
        if not task["done"]
    ]

    if not open_tasks:
        print("No open tasks to finish.")
        return

    for number, task in enumerate(open_tasks, start=1):
        print(f"{number}. {task['title']}")

    while True:
        try:
            number = int(input("Choose task (0 to cancel): "))

            if number == 0:
                return

            if 1 <= number <= len(open_tasks):
                task = open_tasks[number - 1]
                task["done"] = True

                feed_buddy(buddy, task["size"])
                return

            print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

