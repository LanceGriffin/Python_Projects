#!/usr/bin/env python3
"""Simple Flask backend to serve the slots menu and launch the Python game.

Usage:
    python server.py

The script will start a development server and open the default browser to the
menu page. When the Play Slots button is clicked, the /play route is invoked,
which launches `SlotsProgram.py` on a separate thread so that the web server
remains responsive. The menu page can be closed and reopened as needed.
"""

import threading
import subprocess
import sys
import webbrowser
import os
from flask import Flask, send_from_directory, redirect, url_for, Response

app = Flask(__name__, static_folder='.')

@app.route('/')
def menu():
    # serve the index redirect file (which itself points to SlotsMenu.html)
    return send_from_directory('.', 'index.html')

@app.route('/play')
def play():
    # launch the python game in a background thread
    def runner():
        # ensure the script is executed with the same python interpreter
        # use xvfb-run to provide a virtual display for tkinter
        subprocess.run(['xvfb-run', '-a', sys.executable, os.path.join(os.getcwd(), 'SlotsProgram.py')])

    threading.Thread(target=runner, daemon=True).start()
    # respond with a simple page telling the user the game has started
    content = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Game launched</title>'
        '<style>body{font-family:Arial,sans-serif;text-align:center;margin-top:2rem;}'
        'a{color:#3498db;}</style></head><body>'
        '<p>The slots game has been started in a separate window (or terminal).</p>'
        '<p><a href="/">Return to menu</a></p>'
        '</body></html>'
    )
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    port = 5000
    url = f'http://127.0.0.1:{port}/'
    print(f"Starting server at {url}")
    webbrowser.open(url)
    # run flask development server
    app.run(port=port, debug=True)
