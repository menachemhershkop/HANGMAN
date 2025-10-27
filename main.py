from hangman.game import init_state, validate_guess, apply_guess, render_summary, is_lost, render_display
from hangman.io import prompt_guess, print_status, print_result
from hangman.words import choose_secret_word
from data import word

def play(words: list[str], max_tries: int = 6) -> None:
    game=init_state(words,max_tries)
    replace_count=0
    while True:
        letter=prompt_guess()
        if not apply_guess(game, letter):
            game['guessed'].add(letter)
            game['wrong_guesses']+=1
            print_status(game)
            if is_lost(game):
                print_result(game)
                break
        else:
            index_word=[]
            for i, j in enumerate(game['secret']):
                if letter in j:
                    index_word.append(i)
                    game['display'][i]=letter
                    replace_count+=1
                    print(render_summary(game))
        if len(game['secret']) == replace_count:
            print_result(game)
            break
        print(game)




if __name__=='__main__':
    secret_word=choose_secret_word(word.words)
    play(secret_word)
