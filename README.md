# Taskagotchi – A To-Do List with a Coffee Buddy

Taskagotchi is a console to-do application written in Python. Every finished task feeds a small coffee cup buddy that lives in the terminal. If the user gets things done, the buddy is happy and full of caffeine. If the to-do list is ignored, the buddy gets sleepy.

This project was created for the module *Programming Foundations* (FHNW, BSc BIT).

## Analysis

### Problem

Students and professionals have many small and large tasks (assignments, readings, work projects, meetings, chores). Standart to-do lists are functional but lack engagement, so people stop using them after a few days. Tasks are forgotten and there is no motivation to keep the list up to date.

### Scenario

Taskagotchi solves the part of the problem where a student loses motivation to manage their tasks. The student adds tasks in the console, marks them as finished when they are done, and is rewarded by a virtual coffee buddy that gains caffeine, XP and levels. When the student stays away for a long time, the buddy loses caffeine, which gives a reason to come back regularly. All data is saved to a file so that progress is kept between sessions.

### User Roles

| Role | Description |
| --- | --- |
| **Student** | Uses the app daily to add, view, finish and delete tasks and to check on the buddy. |
| **Professional** | Uses the app at work to keep track of work tasks and expects tasks and buddy progress to still be there the next working day. |

### User Stories

Each team member owns three user stories.

| ID | Owner | Story |
| --- | --- | --- |
| US-01 | Martina Juric | Add a task |
| US-02 | Martina Juric | View my tasks |
| US-03 | Martina Juric | Delete a task |
| US-04 | Philipp Zoller | Feed my buddy by completing a task |
| US-05 | Philipp Zoller | See my buddy's mood |
| US-06 | Philipp Zoller | Get a funny reaction |
| US-07 | Federico Janzich | Earn XP and level up |
| US-08 | Federico Janzich | Watch my buddy evolve |
| US-09 | Federico Janzich | Caffeine decays over time |
| US-10 | Fatos Sallauka | Navigate a main menu |
| US-11 | Fatos Sallauka | Keep my progress (save and load) |
| US-12 | Fatos Sallauka | The app never crashes on bad input |

The task sizes used in the examples below are:

| Key | Name | XP | Caffeine |
| --- | --- | ---: | ---: |
| S | Espresso | 10 | +10 % |
| M | Latte | 25 | +20 % |
| L | Frappe | 50 | +35 % |

---

#### US-01: Add a task

**As a** student, **I want** to add a task with a title and a size, **so that** I can keep track of what I need to do.

##### US-01 acceptance criteria

- The task is added when the student selects option `2` ("Add task") in the main menu.
- The student is first asked for a title, then for a size `S`, `M` or `L`.
- The task is stored as a dictionary with the keys `title`, `size` and `done` (`done` is `False`).
- *Given* the student enters the title `Write README` and the size `M`, *when* the task is created, *then* the message `Added 'Write README'!` is displayed.
- *Given* the student enters an empty title (or only spaces), *when* the input is confirmed, *then* the message `A task with no name? Mysterious. Not allowed.` is displayed and no task is created.
- *Given* the student enters an invalid size (e.g., `X` or `big`), *when* the input is confirmed, *then* the size is asked again until `S`, `M` or `L` is entered.
- The size is accepted regardless of surrounding spaces and upper/lower case, e.g., ` m ` is accepted as `M`.

---

#### US-02: View my tasks

**As a** student, **I want** to see a numbered list of my open tasks, **so that** I know what is left to do.

##### US-02 acceptance criteria

- The list is shown when the student selects option `1` ("Show tasks") in the main menu.
- Each open task is shown on its own line in the format `<No>. <Title>  (<Size name>, +<XP> XP)`, e.g., `1. Write README  (Latte, +25 XP)`.
- Numbering starts at `1` and has no gaps.
- Finished tasks (`done` is `True`) are not shown in the list.
- *Given* there are no open tasks, *when* the list is shown, *then* the message `No open tasks. Your buddy is bored!` is displayed instead of an empty list.

---

#### US-03: Delete a task

**As a** student, **I want** to delete a task, **so that** my list stays correct and up to date.

##### US-03 acceptance criteria

- The task is deleted when the student selects option `4` ("Delete task") and enters the number of an open task.
- *Given* the open tasks `1. Write README` and `2. Read chapter 3`, *when* the student enters `1`, *then* `Write README` is removed, the message `Poof! Gone.` is displayed and `Read chapter 3` becomes task number `1`.
- Entering `0` cancels the action and no task is removed.
- *Given* there are two open tasks, *when* the student enters `3`, *then* the message `Please choose between 1 and 2 (0 to cancel).` is displayed and the number is asked again.
- Deleting a task gives no XP and no caffeine.

---

#### US-04: Feed my buddy by completing a task

**As a** student, **I want** completing a task to feed my coffee buddy, **so that** I feel rewarded for getting things done.

##### US-04 acceptance criteria

- A task is completed when the student selects option `3` ("Finish task") and enters the number of an open task.
- The task is marked as `done = True` and no longer appears in the open task list.
- The buddy's caffeine increases by the value of the task size (see table above).
- A message shows what was gained, e.g., `You fed Bean a Latte! +25 XP, +20% caffeine`.
- *Given* the buddy has 50 % caffeine, *when* a task of size `M` is completed, *then* the caffeine is 70 %.
- *Given* the buddy has 90 % caffeine, *when* a task of size `L` is completed, *then* the caffeine is 100 % (never more than 100).
- A completed task cannot be completed again, because it is no longer shown in the list (no double rewards).

---

#### US-05: See my buddy's mood

**As a** student, **I want** to see my buddy as ASCII art with a face that matches its mood, **so that** I can tell at a glance how I am doing.

##### US-05 acceptance criteria

- The buddy is shown when the student selects option `5` ("Check on buddy") and automatically at startup.
- An ASCII coffee cup is printed together with the buddy's name, level, stage and mood.
- The mood is calculated from the caffeine with `if / elif / else` and each mood has its own face (see table below).
- Caffeine and XP are shown as a number and as a text bar with 20 characters, e.g., `Caffeine [##########----------] 50%`.

| Caffeine | Mood | Example |
| ---: | --- | --- |
| 90 – 100 | hyper | 95 % → hyper |
| 50 – 89 | happy | 50 % → happy |
| 20 – 49 | sleepy | 49 % → sleepy |
| 0 – 19 | sad | 19 % → sad |

---

#### US-06: Get a funny reaction

**As a** student, **I want** my buddy to say something funny when I feed or pet it, **so that** using the app is fun.

##### US-06 acceptance criteria

- After a task is completed, the buddy says a random line in the format `Bean says: "<line>"`, chosen with `random.choice()`.
- The lines are stored in a dictionary with at least 3 lines per task size (`S`, `M`, `L`).
- Bigger tasks get more excited lines, e.g., `S` → `Thanks a latte!`, `L` → `WHOA. Frappe-sized win!`.
- At startup the buddy says a line that matches its current mood (e.g., a `sleepy` buddy says `zzz... feed me tasks...` or `Running on decaf vibes here...`).
- When the student selects option `6` ("Pet buddy"), the buddy is shown with a happy face and says one of the `pet` lines.

---

#### US-07: Earn XP and level up

**As a** student, **I want** to earn XP for finished tasks and level up my buddy, **so that** I see long-term progress.

##### US-07 acceptance criteria

- When a task is completed, the buddy gains XP depending on the task size (`S` = 10, `M` = 25, `L` = 50).
- The XP needed for the next level is `level × 50` (level 1: 50 XP, level 2: 100 XP, level 3: 150 XP).
- *Given* a level 1 buddy with 40 XP, *when* a task of size `M` is completed, *then* the buddy is level 2 with 15 XP (leftover XP carries over) and `*** LEVEL UP! Bean is now level 2! ***` is displayed.
- *Given* a level 1 buddy with 0 XP, *when* a task of size `S` is completed, *then* the buddy stays level 1 with 10 XP and no level-up message is shown.
- Multiple level-ups at once are handled with a `while` loop: *given* a level 1 buddy with 0 XP, *when* 200 XP are added, *then* the buddy is level 3 with 50 XP.

---

#### US-08: Watch my buddy evolve

**As a** student, **I want** my buddy to evolve into new stages at certain levels, **so that** I have goals to work towards.

##### US-08 acceptance criteria

- The stages are stored in a list, not in many `if` statements (see table below).
- *Given* a level 2 buddy, *when* it reaches level 3, *then* the message `*** Bean evolved into a Cappuccino Cadet! ***` is displayed.
- *Given* a level 3 buddy, *when* it reaches level 4, *then* no evolution message is displayed (the stage stays Cappuccino Cadet).
- The current stage name is shown on the buddy screen, e.g., `Bean - Lv 3 Cappuccino Cadet (mood: happy)`.

| From level | Stage |
| ---: | --- |
| 1 | Espresso Sprout |
| 3 | Cappuccino Cadet |
| 5 | Latte Legend |
| 8 | Grand Barista |

---

#### US-09: Caffeine decays over time

**As a** professional, **I want** my buddy to get sleepy when I don't use the app, **so that** I am motivated to come back regularly.

##### US-09 acceptance criteria

- The time of the last visit is saved as `last_seen` (using `datetime`).
- At startup, the caffeine is reduced by 5 % per full hour since the last visit.
- The decay rate is a single constant `CAFFEINE_LOSS_PER_HOUR = 5` that is easy to change.
- *Given* the buddy had 50 % caffeine and the last visit was 3 hours ago, *when* the app starts, *then* the caffeine is 35 % and the message `While you were away, Bean lost 15% caffeine.` is displayed.
- *Given* the buddy had 10 % caffeine and the last visit was 5 hours ago, *when* the app starts, *then* the caffeine is 0 % (never below 0).
- *Given* the last visit was less than one hour ago, *when* the app starts, *then* no caffeine is lost and no message is displayed.

---

#### US-10: Edit an existing Task

**As a** student, **I want** to edit the title or size of an open task, **so that** I can fix typos or adjust the effort without deleting or recreating the task.

##### US-10 acceptance criteria

- The student can start editing by selecting option `7` ("Edit task") in the main menu and choosing the number of an open task.
- Entering `0` cancels the action and returns to the main menu without changes.
- The student is asked for a new title. Pressing Enter without typing keeps the current title.
- The student is asked for a new size (`S`, `M`, `L`). Pressing Enter without typing keeps the current size.
- *Given* task `1` is `Write REDME (S)`, *when* the student changes the title to `Write README` and the size to `M`, *then* the confirmation message `Updated 'Write README' (Latte)!` is displayed and the task list shows the updated values.

---

#### US-11: Filter open tasks by size

**As a** professional, **I want** to filter my open tasks by size, ('S', 'M', 'L'), **so that**  I i can quickly find a task that fits my available time and energy.

##### US-11 acceptance criteria

- The student can filter tasks by selecting option `8` ("Filter tasks by size") in the main menu and entering `S`, `M` or `L` (case-insensitive).
- Only open tasks matching the chosen size are displayed, using the standard task format.
- *Given* there are two open `S` tasks and one open `L` task, *when* the student filters by `S`, *then* only the two `S` tasks are displayed.
- *Given* there are no open tasks of size `L`, *when* the student filters by `L`, *then* the message `No open Frappe (L) tasks found.` is displayed.
- *Given* the student enters an invalid size, *when* confirmed, *then* the app asks again until `S`, `M` or `L` is entered.

---

#### US-12: View completed tasks and statistics

**As a** professional, **I want** to see a list of my completed tasks and total statistics, **so that** I can review what I have already achieved.

##### US-12 acceptance criteria

The history is shown when the user selects option `9` ("Completed tasks") in the main menu.
- All completed tasks are listed with their title and size name, e.g., `[x] Write README (Latte)`.
- Below the list, a summary line displays the total number of completed tasks and total XP earned from them, e.g., `Total completed: 5 tasks (110 XP earned)`.
- *Given* no tasks have been completed yet, *when* the option is selected, *then* the message `No completed tasks yet. Time to get some coffee!` is displayed.

---

### Use Cases

- Add, show and delete tasks
- Finish a task and feed the buddy
- Check on and pet the buddy
- Save and load progress (to `data/save.json`)

## Project Requirements

Each app must meet the following three criteria in order to be accepted:

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

### 1. Interactive App (Console Input)

The application interacts with the user via the console. Users can:

- Name their coffee buddy on the first start
- Add tasks with a title and a size
- View, finish and delete tasks
- Check on the buddy (ASCII art, mood, caffeine, XP, level, stage)
- Pet the buddy and read its reactions
- Save and quit the application

Example of the main menu:

```text
  1) Show tasks   2) Add task   3) Finish task (feed!)
  4) Delete task  5) Check on buddy   6) Pet buddy   0) Save & quit
  >
```

### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main.py`, `tasks.py` and `storage.py` as follows:

- **Number input:** The helper function `ask_number()` is used whenever a task number is needed. It only returns a valid number in the allowed range or `0` (cancel):


- **Task title:** Empty titles are rejected:

- **Task size:** The size is asked again until a valid key is entered. Spaces and lower case are accepted:

- **Value limits:** Caffeine always stays between 0 and 100:

- **Save file validation:** A broken save file does not crash the app:

- **Main menu options:** The main menu handles invalid choices gracefully:


These checks prevent crashes and guide the user to provide correct input.

### 3. File Processing

The application reads and writes data using a JSON file.

**Save file:** `data/save.json` contains the buddy, all tasks and the time of the last visit, for example:


- The file is **read** at startup with `json.load()`. If it does not exist, a new game is started.
- The file is **written** with `json.dump()` after every menu action and when the user quits.
- The value `last_seen` is used to calculate how much caffeine the buddy lost while the user was away.

## Implementation

### Technology

- Python 3.10 or newer
- Environment: Visual Studio Code / GitHub Codespaces
- No external libraries

### Repository Structure

```text
taskagotchi/
├── main.py          # Entry point: main menu loop
├── tasks.py         # Add / list / edit / delete / complete tasks
├── buddy.py           # buddy stats, moods, ASCII art, reactions
├── progress.py      # XP, levels, evolution stages, caffeine decay
├── storage.py       # Save & load data (JSON)
├── data/
│   └── save.json    # Created automatically on first save
└── README.md
```

### How to Run

1. Open the repository in **Visual Studio Code** or **GitHub Codespaces**.
2. Open the **Terminal**.
3. Run the program:

   ```bash
   python3 main.py
   ```

   On Windows use `python main.py` or `py main.py`.

### Libraries Used

- `json`: Used to save and load tasks and buddy data in `data/save.json`.
- `os`: Used to check if the save file exists.
- `random`: Used to pick a random reaction line for the buddy.
- `datetime`: Used to store the time of the last visit and calculate the caffeine decay.

These libraries are part of the Python standard library, so no external installation is required.

## Team & Contributions

| Name | Contribution |
| --- | --- |
| Martina Juric | Task management: add, show and delete tasks (`tasks.py`, US-01 – US-03) |
| Philipp Zoller | Coffee buddy: feeding, moods, ASCII art and reactions (`buddy.py`, US-04 – US-06) |
| Federico Janzich | Progression: XP, levels, evolution and caffeine decay (`progress.py`, US-07 – US-09) |
| Fatos Sallauka | Extended task features: edit tasks, filter by size and completed tasks history (`tasks.py`, US-10 – US-12) |
| Whole team | App shell: main menu, saving/loading and input validation (`main.py`, `storage.py`, US-10 – US-12) |

## License

This project is provided for **educational use only** as part of the Programming Foundations module.
