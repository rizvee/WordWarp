# main.py
from flask import Flask, render_template
from threading import Thread
from queue import Queue
import os
import sys
from modules.gameplay import start_game
from modules.multiplayer import start_multiplayer
from modules.ui import display_menu

# Add the path to the directory containing your modules to the system path
project_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(project_path, "modules"))

from modules.gameplay import start_game
from modules.ui import display_menu

app = Flask(__name__)

# Use a queue to pass messages between Flask app and game loop
message_queue = Queue()

@app.route('/')
def home():
    return render_template('index.html')

def game_thread():
    print("Welcome to WordWarp!")
    while True:
        display_menu()
        choice = message_queue.get()  # Wait for user choice from Flask app

        if choice == "1":
            difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
            start_game(difficulty)
        elif choice == "2":
            print("Feature coming soon: Multiplayer mode!")
        elif choice == "3":
            print("Thanks for playing WordWarp! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game_thread = Thread(target=game_thread)
    game_thread.start()

    # Run the Flask app without reloader
    app.run(debug=True, use_reloader=False)
