"""
main.py - Entry point and console controller for Taskagotchi.

Coordinates the application lifecycle, turn-based elapsed time calculations,
interactive menu navigation, and module dispatching.
"""

import sys
from storage import load_game_data, save_game_data
from user_input import ask_number

def print_menu():
    """Display the official Taskagotchi interactive console menu."""
    print("\n" + "=" * 45)
    print("              👾 TASKAGOTCHI 👾")
    print("=" * 45)
    print("  1) Show tasks")
    print("  2) Add task")
    print("  3) Finish task (feed!)")
    print("  4) Delete task")
    print("  5) Check on buddy")
    print("  6) Pet buddy")
    print("  7) Edit task")
    print("  8) Filter tasks by size")
    print("  9) Completed tasks")
    print("  0) Save & quit")
    print("=" * 45)

def main():
    
    """Main application loop managing game state and user navigation."""
    
    print("\nStarting Taskagotchi...")
    data = load_game_data()
    #“Using .get() to avoid a KeyError when a dictionary key is missing
    username = data.get("username", "Player")
    buddy_name = data.get("taskgochi", {}).get("name", "Bean")
    print(f"Welcome back, {username}! Your buddy {buddy_name} is waiting for you.")

    while True:
        print_menu()
        choice = ask_number("Select an option (0-9): ", 0, 9)

        if choice == 0:
            print("\nSaving your progress...")
            save_game_data(data)
            print("Goodbye! See you next coffee break. ☕")
            sys.exit(0)

        elif choice == 1:
            print("\n[Option 1] Show tasks selected (connecting to task.py)...")
            # Pending connection: task.show_tasks(data.get("tasks", []))

        elif choice == 2:
            print("\n[Option 2] Add task selected (connecting to task.py)...")
            # Pending connection: task.add_task(data)

        elif choice == 3:
            print("\n[Option 3] Finish task selected...")
            # Pending connection: task.finish_task(data)
        elif choice == 4:
            print("\n[Option 4] Delete task selected...")
            # Pending connection: task.delete_task(data)
        elif choice == 5:
            print("\n[Option 5] Check on buddy selected...")
            # Pending connection: buddy.check_buddy(data)
        elif choice == 6:
            print("\n[Option 6] Pet buddy selected...")
            # Pending connection: buddy.pet_buddy(data)
        elif choice == 7:
            print("\n[Option 7] Edit task selected...")
            # Pending connection: task.edit_task(data)
        elif choice == 8:
            print("\n[Option 8] Filter tasks selected...")
            # Pending connection: task.filter_tasks_by_size(data)
        elif choice == 9:
            print("\n[Option 9] Completed tasks selected...")
            # Pending connection: task.show_completed_tasks(data)

if __name__ == "__main__":
    main()

