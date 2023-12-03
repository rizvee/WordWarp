# modules/gameplay.py
import random
from modules.ui import display_menu
from modules.utils import get_user_choice, read_word_dictionary

# ... rest of your code ...

def display_menu():
    """
    Display the game menu.
    """
    print("\nMenu:")
    print("1. Start Single Player Game")
    print("2. Multiplayer Mode (Coming Soon)")
    print("3. Exit")

    # Get user choice and set it in the queue
    choice = input("Enter your choice: ").lower()
    set_user_choice(choice)
