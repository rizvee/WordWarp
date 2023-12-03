# modules/utils.py
import random

def get_user_choice():
    """
    Get user choice from the console.

    Returns:
        str: User choice.
    """
    return input("Enter your choice: ").lower()

def set_user_choice(choice):
    """
    Set user choice in the console.

    Args:
        choice (str): User choice.
    """
    print(f"You entered: {choice}")

def read_word_dictionary():
    """
    Read the word dictionary from a file and return a list of words.

    Returns:
        list: List of words in the dictionary.
    """
    dictionary_path = "WordWarp\\data\\word_dictionary.txt"
    with open(dictionary_path, "r") as file:
        return [word.strip() for word in file.readlines()]

# Other utility functions can go here if needed
