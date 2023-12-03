# modules/multiplayer.py
from modules.ui import display_menu
from modules.utils import set_user_choice, read_word_dictionary

def start_multiplayer():
    print("Multiplayer mode is coming soon!")

def play_multiplayer_game():
    print("Multiplayer game started!")

    # Read the word dictionary
    word_dictionary = read_word_dictionary()

    # Get the number of players
    num_players = int(input("Enter the number of players: "))

    # Assign a word to each player
    player_words = {}
    for i in range(1, num_players + 1):
        player_name = input(f"Enter the name of Player {i}: ")
        player_words[player_name] = select_word(word_dictionary)

    # Take turns for each player
    for player, word in player_words.items():
        print(f"\n{player}'s turn:")
        play_turn(word)

def select_word(word_dictionary):
    # Select a random word from the dictionary
    return random.choice(word_dictionary)

def play_turn(word):
    # Logic for each player's turn
    # For example, word guessing or word association
    pass
