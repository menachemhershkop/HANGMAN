from data import word
import random

def choose_secret_word(words: list[str]) -> str:
    rand_word=random.choice(words)
    return rand_word
