def prompt_guess() -> str:
    while True:
        letter=input("Enter a letter: ")
        if len(letter)==1:
            return letter
def print_status(state: dict) -> None:
    print(f'{state["display"]}\n word you guess {state['guessed']} \n guess you have {(state['max_tries']- state['wrong_guesses'])}')
def print_result(state: dict) -> None:
    pass