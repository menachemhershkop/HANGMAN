def init_state(secret: str, max_tries: int) -> dict:
    for i in range(len(secret)+1):
        display=i*"_"
    return {"secret":str(secret), "display":list[str](display), "guessed": set[str],"wrong_guesses":int,"max_tries":int(max_tries)}
def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str] :
    if ch in guessed:
        return True ,"Good choice"
    else:
        return False ,"This charter already exist"

def apply_guess(state: dict, ch: str) -> bool:
    pass
def is_won(state: dict) -> bool:
    pass
def is_lost(state: dict) -> bool:
    pass
def render_display(state: dict) -> str:
    pass
def render_summary(state: dict) -> str:
    pass