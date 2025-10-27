def init_state(secret: str, max_tries: int) -> dict:
    for i in range(len(secret)+1):
        display=i*"_"
    wrong_guesses=0
    return {"secret":secret, "display":list[str](display), "guessed": set(),"wrong_guesses":int(wrong_guesses),"max_tries":int(max_tries)}
def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str] :
    if ch in guessed:
        return True ,"Good choice"
    else:
        return False ,"This charter already exist"
def apply_guess(state: dict, ch: str) -> bool:
    if ch in state['secret']:
        return True
    else:
        return False
def is_won(state: dict) -> bool:
    if state:
        return True
    return False
def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False
def render_display(state: dict) -> str:
    return "".join(state["display"])
def render_summary(state: dict) -> str:
    return f'The secret word is {state['display']}, the guesses word is {state['guessed']}'