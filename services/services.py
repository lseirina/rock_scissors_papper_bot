import random
from lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice():
    return random.choice(['rock', 'scissors', 'papper'])


def get_winner(user_choice, bot_choice):
    rules = {
        'rock': 'scissors',
        'scissors': 'papper',
        'papper': 'rock'
    }
    if user_choice == bot_choice:
        return 'nobody_won'
    if rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'
