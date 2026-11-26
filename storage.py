"""
storage.py - JSON data management for Taskagotchi.

loading of game state using JSON files,
ensuring application state survives between sessions.
"""

import json
from pathlib import Path

# Path to the persistent JSON game state
SAVE_FILE = Path("data/save.json")


def save_game_data(data: dict):
    """Save the current game state to data/save.json."""
    # Ensure the 'data/' directory exists before writing
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_game_data():
    """Load state from data/save.json or return a fresh template if missing or corrupt."""
    default_state = {
        "username": "Player",
        "tasks": [],
        "taskgochi": {
            "name": "Bean",
            "level": 1,
            "experience_points": 0,
            "caffeine": 50,
            "last_caffeine": "2026-11-26T12:00:00"
        }
    }

    # If the file does not exist yet (first run), initialize and save the default state
    if not SAVE_FILE.exists():
        save_game_data(default_state)
        return default_state

    # Read existing file with error handling
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Notice: Corrupt or unreadable save file. Initializing fresh state.")
        save_game_data(default_state)
        return default_state
