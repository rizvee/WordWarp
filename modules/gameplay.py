# modules/gameplay.py
import random
from modules.ui import display_menu

from utils import get_user_choice


def start_game(difficulty):
    global hints_left
    hints_left = 3  # Reset hints count for a new game
    print(f"Starting WordWarp game with difficulty: {difficulty}")

    while True:
        # Display game menu
        display_menu()

        # Get user choice from the queue
        choice = get_user_choice()

        # Process user choice
        if choice == "1":
            print("Starting single-player game...")
            play_single_player_game(difficulty)
        elif choice == "2":
            print("Feature coming soon: Multiplayer mode!")
        elif choice == "3":
            print("Thanks for playing WordWarp! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def play_single_player_game(difficulty):
    print(f"Single-player game started with difficulty: {difficulty}")

    # Read the word dictionary
    word_dictionary = read_word_dictionary()

    # Select a random word from the dictionary
    target_word = random.choice(word_dictionary)

    # Initialize game variables
    attempts_left = 3
    guessed_letters = set()

    # Display initial information
    print("Try to guess the word!")
    display_word_state(target_word, guessed_letters)
    print(f"Attempts left: {attempts_left}")

    while attempts_left > 0:
        # Get user input (a letter)
        guess = input("Enter a letter: ").lower()

        # Validate the input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Update guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the target word
        if guess in target_word:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            attempts_left -= 1

        # Display the current state of the word
        display_word_state(target_word, guessed_letters)

        # Display attempts left
        print(f"Attempts left: {attempts_left}")

        # Check if the player has guessed the entire word
        if set(target_word).issubset(guessed_letters):
            print("Congratulations! You guessed the word.")
            break

    else:
        print("Sorry, you've run out of attempts. The word was:", target_word)

def display_word_state(target_word, guessed_letters):
    """
    Display the current state of the word with guessed letters filled in.
    """
    display_word = ''.join(letter if letter in guessed_letters else '_' for letter in target_word)
    print("Current word:", display_word)



def read_word_dictionary():
    dictionary_path = "C:\\Users\\ACER\\Desktop\\WordWarp\\data\\word_dictionary.txt"
    with open(dictionary_path, "r") as file:
        return [word.strip() for word in file.readlines()]

if __name__ == "__main__":
    # For testing purposes, you can start the game directly
    start_game("medium")
