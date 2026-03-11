# Conways-Turtle
Conway's Game of Life visualized using Turtle graphics.

## What is this?
This is an implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) that uses Turtle graphics to draw each generation. It comes pre-loaded with several classic patterns (Gliders, LWSS, Blinker, Glider Gun, and more).

There are two versions:
- **Local** – runs on your machine using Jython
- **Web** – runs in your browser using WebTigerJython

---

## Running Locally (Jython)

**File:** `conways-game-of-life_jython_turtle.py`

### Prerequisites
- [Java](https://www.java.com/en/download/) (required by Jython)
- [Jython](https://www.jython.org/download.html) – download the standalone jar

### Steps
1. Download and install Jython from https://www.jython.org/download.html
2. Open a terminal in the project folder
3. Run the script:
   ```bash
   jython conways-game-of-life_jython_turtle.py
   ```
4. When prompted, enter:
   - **Box Size** – pixel size of each cell (e.g. `10`)
   - **Time between generations (in s)** – animation delay in seconds (e.g. `0.5`)
5. A window will open and the simulation will start automatically.

---

## Running in the Browser (WebTigerJython)

**File:** `conways-game-of-life_webjython_turtle.py`

### Steps
1. Open [WebTigerJython](https://webtigerjython.ethz.ch/) in your browser
2. Copy the entire contents of `conways-game-of-life_webjython_turtle.py`
3. Paste it into the editor on the WebTigerJython page
4. Click the **Run** button
5. When prompted, enter:
   - **Box Size** – pixel size of each cell (e.g. `10`)
   - **Time between generations (in s)** – animation delay in seconds (e.g. `0.5`)
6. The simulation will start in the browser window.

> **Note:** The web version can be resource-intensive depending on box size and number of active cells.

---

## License
© 2026 XeraoXX & GitHub Contributors – Licensed under [GNU GPL v3](LICENSE)
