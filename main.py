"""
main.py - Entry point and console controller for Taskagotchi.

Coordinates the application lifecycle, turn-based elapsed time calculations,
interactive menu navigation, and module dispatching.
"""

import sys
from datetime import datetime

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

if __name__ == "__main__":
    print_menu()

