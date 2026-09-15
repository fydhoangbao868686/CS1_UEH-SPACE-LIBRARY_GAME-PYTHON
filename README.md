# UEH Library Escape

**A 2D educational escape game built with Python and Pygame.**

UEH Library Escape turns introductory programming exercises into a story-driven journey through a university library. Players enter a registered ID, explore interactive scenes, watch video cutscenes, and solve Python and data manipulation puzzles to progress toward the ending.

Developed as a CS1 project, the game combines programming practice with visual storytelling, background music, sound effects, and immediate answer feedback. It runs as a local desktop application.

## Features

- **Story-based progression:** A sequence of 29 numbered scenes, including the title screen, player identification, videos, puzzles, completion screens, and ending.
- **Six programming challenges:** Practice variable assignment, dictionary access, slicing, array construction, conditional updates, and mean calculation.
- **Interactive objects:** Click buttons, a laptop, and navigation controls to explore and advance.
- **Player identification:** Read an ID-to-name mapping from an Excel workbook and display a personalized greeting.
- **In-game data display:** View a scrollable Excel dataset with a highlighted clue.
- **Multimedia presentation:** Ten MP4 cutscenes, background music, click sounds, and correct/incorrect answer effects.
- **Visual feedback:** Hover effects, typewriter messages, animated completion popups, and a pixel-style font.
- **Configurable layout:** Store interface anchors and scale settings in `ui_layout.json`.

## Learning content

| Challenge | Programming concept |
| --- | --- |
| Define a constant | Variable naming and assignment |
| Recover a password using the player ID | Dictionary key access |
| Reverse a sequence | Python slicing |
| Represent a matrix | NumPy-style array construction |
| Update values that meet a condition | Boolean indexing and conditional assignment |
| Calculate an average | A data object's `mean()` method |

Answers are checked against predefined text expressions. The game does not execute submitted Python code, and equivalent expressions may be rejected if their spelling or spacing differs from the expected answer. NumPy-style and data-analysis expressions are puzzle content; NumPy and pandas are not runtime dependencies of this game.

## Technology stack

| Technology | Role |
| --- | --- |
| Python | Game logic and application entry point |
| Pygame | Window, event handling, rendering, input, music, and sound effects |
| ffpyplayer | MP4 video and audio playback |
| openpyxl | Reading player records and the in-game dataset |
| JSON | Interface layout configuration |

The window is configured at **1280 × 720**, with a target frame-rate cap of **60 FPS**. Actual performance depends on the machine and video playback environment.

## Project structure

Paths below are relative to the directory containing `main.py` (named `final_project` inside the supplied ZIP).

| Path | Contents |
| --- | --- |
| `main.py` | Game configuration, reusable UI components, scene classes, and main loop |
| `assets/` | Background images, buttons, and `context1.mp4` through `context10.mp4` |
| `assets/bgm/` | Title and gameplay background music |
| `assets/sfx/` | Click, correct-answer, wrong-answer, and transition sounds |
| `INDEX.xlsx` | Player IDs and display names |
| `dataset.xlsx` | Dataset shown in the game; see the filename correction below |
| `PressStart2P-Regular.ttf` | Pixel-style font |
| `ui_layout.json` | Saved interface positions and scales |
| `README.md` | Project overview and setup instructions |

The source archive also includes a Windows `.venv` directory. Create a fresh virtual environment for your machine; the bundled environment is not needed in the repository.

## Installation

### 1. Prepare the project

Download and extract the source ZIP, or clone the repository. Open a terminal in the directory containing `main.py`, `assets/`, and the Excel files.

You need Python, a graphical desktop session, and the three packages listed below. Package metadata in the supplied Windows environment records **Pygame 2.6.1**, **openpyxl 3.1.5**, and **ffpyplayer 4.5.3**. These are source-environment records, not a guarantee of compatibility on every platform.

### 2. Create a virtual environment

**Windows Command Prompt:**

```bat
python -m venv .venv-local
.venv-local\Scripts\activate.bat
```

**Linux / macOS:**

```bash
python3 -m venv .venv-local
source .venv-local/bin/activate
```

Install the dependencies:

```bash
python -m pip install pygame==2.6.1 openpyxl==3.1.5 ffpyplayer==4.5.3
```

The supplied source does not contain a project-level `requirements.txt`. The command above installs the versions recorded in its bundled environment.

### 3. Correct the dataset filename

The archive contains **`dataset.xlsx`**, but `main.py` looks for **`Dataset.xlsx`**. This mismatch matters on case-sensitive filesystems, including typical Linux and Codespaces environments.

Before running, change the configuration line in `main.py` to match the actual filename:

```python
DATASET_XLSX_PATH = os.path.join(BASE_DIR, "dataset.xlsx")
```

This README documents the correction; the provided source code has not been modified as part of this README deliverable.

### 4. Prepare a player ID

Open `INDEX.xlsx` and use an existing ID, or add a demo record to the active worksheet. Column A contains the ID and column B contains the display name. For example, a record you can add is:

| ID | Name |
| --- | --- |
| DEMO001 | Demo Player |

The example is not a preconfigured account. Add the row before entering `DEMO001` in the game. Store IDs as text when leading zeros must be preserved, save the workbook, and restart the game after changing it.

### 5. Run the game

```bash
python main.py
```

The game opens in a desktop window. No database server, web server, external AI service, or API key is required.

## How to play

1. Choose **Play** on the title screen. The **Project** and **Game** buttons open information screens.
2. Enter an ID registered in `INDEX.xlsx`, then continue after the greeting.
3. Watch the story cutscenes and follow the clues shown in each scene.
4. Enter the requested programming expressions or interact with the highlighted objects. Incorrect answers allow another attempt.
5. Complete the challenges to reach the final screen, then return to the title screen to play again.

| Control | Action |
| --- | --- |
| Left mouse button | Activate buttons and interactive objects |
| Keyboard typing / Backspace | Enter and edit puzzle answers |
| Enter | Submit answers or continue on supported screens |
| Space / Enter / left click during a video | Skip to the next scene |
| Mouse wheel in the dataset scene | Scroll the displayed data |
| Esc during gameplay | Return to the title screen |
| Esc on the title home screen | Open the quit confirmation; press Y to quit or N to cancel |
| Close window | Exit the application |

The backquote key also exposes a developer scene-history shortcut. It is intended for debugging rather than normal progression.

## Code organization

The implementation is contained in `main.py`, with reusable classes separating the main responsibilities:

| Class / component | Responsibility |
| --- | --- |
| `LayoutStore` | Read layout settings from JSON |
| `Fonts` | Load and cache fonts |
| `AudioManager` | Manage background music and sound effects |
| `ImageButton` | Handle button geometry, hover, clicks, and drawing |
| `Scene` and `SceneManager` | Define scene behavior, transitions, and shared player state |
| `VideoScene` | Play and release video resources |
| `TextAnswerScene` | Provide reusable text-input and answer-validation behavior |
| `ClickObjectScene` | Advance through object interaction |
| `DonePopupScene` | Display completion animations |
| `main()` | Initialize Pygame and run the event, update, and drawing loop |

To customize the game, edit layout values in `ui_layout.json`, player records in `INDEX.xlsx`, and scene logic or answer checks in `main.py`. Keep asset filenames consistent with the configured paths.

## GitHub Codespaces

This is a **Pygame desktop game**. A standard Codespaces terminal does not by itself provide a visible game window. Browser-based play requires a graphical desktop environment exposed through VNC/noVNC, together with the Python dependencies and all game assets. Audio forwarding may require additional setup.

The archive does not include `.devcontainer` configuration or a one-click Codespaces launcher. The local desktop instructions above are the primary run method. A repository link alone does not launch the game for visitors.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError` | Activate the new environment and install the three dependencies with its Python interpreter. |
| Missing background, button, or video | Preserve the full `assets/` directory and its filenames. Individual scenes display missing-asset information. |
| Dataset scene reports a missing file | Apply the `dataset.xlsx` filename correction described above. |
| Player ID is rejected | Check that the ID exists in column A of the active worksheet and has a name in column B. |
| Video does not play | Check that ffpyplayer is installed and the referenced MP4 exists. |
| No audio | Check device and application volume. The code allows the game to continue when Pygame mixer initialization fails. |
| A logically correct answer is rejected | Match the expected expression's capitalization, punctuation, and spacing; validation is based on text comparison. |

## Current scope

The project implements a fixed sequence of educational challenges. It does not include persistent progress saves, a leaderboard, multiplayer, or arbitrary Python code execution. Player identification is a local workbook lookup, not an authentication system.

This README was prepared from source inspection. A complete graphical playthrough has not been verified as part of this documentation work.

## License and assets

No project-level `LICENSE` file is included in the supplied archive. Usage and redistribution terms for the code, images, videos, audio, and font should be established by their respective owners.
