# Python_Projects

## Slots Game Web Launcher

A simple Flask-based launcher is included to serve the slots menu and start the
Python slot machine game. Follow these steps:

1. **Install dependencies** (Flask):
   ```bash
   python -m pip install flask
   ```
2. **Run the server** from the `PythonProjectMonth` directory:
   ```bash
   cd PythonProjectMonth
   python server.py
   ```
   The default browser will open the menu automatically.
3. **Play the game** by clicking **"Play Slots"**. The backend will start
   `SlotsProgram.py` in a separate process and display a status page. The menu
   window will attempt to close itself; if it remains open you can close it
   manually and return later using the link provided.

> ⚠️ The Python game (`SlotsProgram.py`) should contain your slot machine logic.
> Currently it is empty – fill it with whatever interactive console/GUI code
> you prefer.

You can always navigate back to the menu by reopening `http://127.0.0.1:5000/`
or restarting the server.
