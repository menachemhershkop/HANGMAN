def prompt_guess() -> str:
    while True:
        letter=input("Enter a letter: ")
        if len(letter)==1:
            return letter
def print_status(state: dict) -> None:
    print(f'{state["display"]}\n word you guess {state['guessed']} \n guess you have {(state['max_tries']- state['wrong_guesses'])}')
def print_result(state: dict) -> None:
    if state["wrong_guesses"] >= state["max_tries"]:
        print(f'OHOOOO!!! \n the word is {state['secret']}, word you guesses {state['guessed']}')
    else:
        print(f'Wall done!!! \n the word is {state['secret']}, word you guesses {state['guessed']}')