# modules/scoring.py

def update_score(current_score, word):
    score_multiplier = calculate_score_multiplier(word)
    score = current_score + len(word) * score_multiplier
    return score

def calculate_score_multiplier(word):
    # Implement custom scoring logic based on word properties
    # For example, you could assign higher scores for longer words or words with certain letters
    return 1  # Default multiplier for now
